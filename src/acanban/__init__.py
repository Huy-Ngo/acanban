# Initialization code
# Copyright (C) 2020  Nguyễn Gia Phong
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

from quart import render_template
from quart_trio import QuartTrio
from rethinkdb import r
from rethinkdb.trio_net.net_trio import TrioConnectionPool

__all__ = ['app']
__doc__ = 'Academic Kanban'
__version__ = '0.0.1'


class Acanban(QuartTrio):
    db_pool: TrioConnectionPool


app = Acanban(__name__)


@app.before_serving
async def create_db_pool() -> None:
    """Create RethinkDB connection pool."""
    r.set_loop_type('trio')
    app.db_pool = r.ConnectionPool(db='test', nursery=app.nursery)


@app.after_serving
async def close_db_pool() -> None:
    """Close RethinkDB connection pool."""
    await app.db_pool.close()


@app.route('/')
async def index() -> str:
    """Return the index page."""
    return await render_template('index.html')
