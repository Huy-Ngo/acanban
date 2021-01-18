# IPFS proxy
# Copyright (C) 2021  Nguyễn Gia Phong
#
# This file is part of Acanban.
#
# Acanban is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Acanban is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Acanban.  If not, see <https://www.gnu.org/licenses/>.

from typing import AsyncIterator
from urllib.parse import urlsplit, urlunsplit

from cid import CIDv1, make_cid
from httpx import Response
from quart import (Blueprint, ResponseReturnValue,
                   current_app, redirect, request)
from quart.exceptions import NotFound, RequestTimeout
from quart_auth import current_user
from rethinkdb import r
from rethinkdb.errors import ReqlNonExistenceError
from trio import TooSlowError, fail_after

__all__ = ['add', 'blueprint']

blueprint = Blueprint('ipfs', __name__)


def ensure_cidv1(multihash: str) -> str:
    """Return the given multihash encoded as base58 in CIDv1."""
    cid = make_cid(multihash)
    return (cid if isinstance(cid, CIDv1) else cid.to_v1()).encode().decode()


async def add() -> str:
    """Proxy file upload to IPFS add and return UUID in table files."""
    headers = {'Content-Length': request.headers['Content-Length'],
               'Content-Type': request.headers['Content-Type']}
    try:
        with fail_after(current_app.config['BODY_TIMEOUT']):
            response = await current_app.ipfs_api.post(
                '/add', headers=headers, data=request.body)
    except TooSlowError:  # pragma: no cover
        raise RequestTimeout
    response.raise_for_status()

    file = response.json()
    async with current_app.db_pool.connection() as conn:
        result = await r.table('files').insert(dict(
            cid=ensure_cidv1(file['Hash']),
            name=file['Name'], size=int(file['Size']),
            time=r.now(), user=current_user.key)).run(conn)
    return result['generated_keys'][0]


def fallback() -> ResponseReturnValue:
    """Redirect the current request to the fallback IPFS gateway."""
    base = urlsplit(current_app.ipfs_config['gateway']['fallback'])
    url = urlsplit(request.url)
    elements = base.scheme, base.netloc, url.path, url.query, url.fragment
    return redirect(urlunsplit(elements), 301)


@blueprint.route('/ipns/<path:path>')
async def redirect_ipns(path: str) -> ResponseReturnValue:
    """Redirect IPNS URLs to the fallback gateway."""
    return fallback()


async def stream(response: Response) -> AsyncIterator[bytes]:
    """Return the response's raw stream."""
    try:
        async for chunk in response.aiter_raw(): yield chunk
    finally:
        await response.aclose()


@blueprint.route('/ipfs/<path:path>')
async def proxy_gateway(path: str) -> ResponseReturnValue:
    """Proxy IPFS gateway.

    If the file was not added through Acanban,
    redirect to the fallback gateway instead.
    """
    try:
        cid = ensure_cidv1(path.split('/', 1)[0])
    except ValueError:
        raise NotFound
    query = r.table('files').get_all(cid, index='cid')[0].pluck()
    async with current_app.db_pool.connection() as connection:
        try:
            await query.run(connection)
        except ReqlNonExistenceError:
            return fallback()

    client = current_app.ipfs_gateway
    proxied_request = client.build_request(
        'GET', path, params=request.args,
        headers={**request.headers, 'Host': client.base_url.netloc})
    response = await client.send(proxied_request, stream=True)
    return stream(response), response.status_code, response.headers.items()
