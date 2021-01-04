# Server console script
# Copyright (C) 2020-2021  Nguyễn Gia Phong
# Copyright (C) 2020  Ngô Ngọc Đức Huy
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

from hypercorn.middleware import HTTPToHTTPSRedirectMiddleware
from hypercorn.trio import serve
from hypercorn.typing import ASGIFramework
from trio import run

from . import app as acanban
from .config import (acanban_config, hypercorn_config,
                     ipfs_config, rethinkdb_config)

if __name__ == '__main__':
    domain = acanban_config().get('domain')
    acanban.db_config = rethinkdb_config()
    acanban.ipfs_config = ipfs_config()
    if domain is None:
        app: ASGIFramework = acanban
    else:
        app = HTTPToHTTPSRedirectMiddleware(acanban, domain)
    run(serve, app, hypercorn_config())
