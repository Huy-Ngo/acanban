# Initialization code
# Copyright (C) 2020-2021  Nguyễn Gia Phong
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

from __future__ import annotations

from contextlib import asynccontextmanager
from secrets import token_urlsafe
from typing import Any, AsyncIterator
from urllib.parse import urlsplit

from httpx import AsyncClient
from quart import ResponseReturnValue, current_app, render_template
from quart_auth import current_user
from quart_trio import QuartTrio
from rethinkdb import r
from rethinkdb.trio_net.net_trio import TrioConnectionPool
from trio import open_nursery

from .auth import Authenticator, blueprint as auth
from .config import IPFS_DEFAULT, RETHINKDB_DEFAULT
from .ipfs import blueprint as ipfs
from .project import blueprint as project
from .user import blueprint as user

__all__ = ['app']
__doc__ = 'Academic Kanban'
__version__ = '0.0.5'


class Acanban(QuartTrio):
    """Acanban web application."""

    auth_manager: Authenticator
    db_config = RETHINKDB_DEFAULT
    db_pool: TrioConnectionPool
    ipfs_config = IPFS_DEFAULT
    ipfs_gateway: AsyncClient
    ipfs_api: AsyncClient

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.secret_key = token_urlsafe(16)
        Authenticator().init_app(self)

    @asynccontextmanager
    async def test_app(self) -> AsyncIterator[Acanban]:
        """Return a context manager startup and shutdown the app."""
        async with open_nursery() as nursery:
            self.nursery = nursery
            await self.startup()
            try:
                yield self
            finally:
                await self.shutdown()
        self.nursery = None


app = Acanban(__name__)
app.register_blueprint(auth)
app.register_blueprint(ipfs)
app.register_blueprint(user)
app.register_blueprint(project)


@app.before_serving
async def create_db_pool() -> None:
    """Create RethinkDB connection pool."""
    r.set_loop_type('trio')
    app.db_pool = r.ConnectionPool(nursery=app.nursery, **app.db_config)


@app.after_serving
async def close_db_pool() -> None:
    """Close RethinkDB connection pool."""
    await app.db_pool.close()


@app.before_serving
async def open_ipfs_clients() -> None:
    """Open HTTPX client for IPFS gateway and HTTP API."""
    app.ipfs_gateway = AsyncClient(base_url=app.ipfs_config['gateway']['base'])
    api_url = app.ipfs_config['api']['base']
    app.ipfs_api = AsyncClient(base_url=api_url, headers={
        'Accept': 'application/json', 'Host': urlsplit(api_url)[1],
        'User-Agent': f'acanban/{__version__}'})


@app.after_serving
async def close_ipfs_clients() -> None:
    """Close HTTPX client for IPFS gateway and HTTP API."""
    await app.ipfs_gateway.aclose()
    await app.ipfs_api.aclose()


@app.route('/')
async def index() -> ResponseReturnValue:
    """Return the index page."""
    if await current_user.is_authenticated:
        uuids = await current_user.projects
        my_project_list = r.table('projects').get_all(*uuids)
        async with current_app.db_pool.connection() as connection:
            projects = await my_project_list.run(connection)
        return await render_template('myproject.html', projects=projects)
    else:
        return await render_template('index.html')
