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
from quart.exceptions import NotFound
from rethinkdb import r

__all__ = ['blueprint']

blueprint = Blueprint('ipfs', __name__)


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
        cid_orig = make_cid(path.split('/', 1)[0])
    except ValueError:
        raise NotFound
    cid = cid_orig if isinstance(cid_orig, CIDv1) else cid_orig.to_v1()
    content = r.table('files').get(cid.encode().decode())
    async with current_app.db_pool.connection() as connection:
        if await content.run(connection) is None: return fallback()

    client = current_app.ipfs_gateway
    proxied_request = client.build_request(
        'GET', path, params=request.args,
        headers={**request.headers, 'Host': client.base_url.netloc})
    response = await client.send(proxied_request, stream=True)
    return stream(response), response.status_code, response.headers.items()
