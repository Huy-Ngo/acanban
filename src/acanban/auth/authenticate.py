# Authentication handler
# Copyright (C) 2020  Nguyễn Gia Phong
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

from crypt import crypt
from hmac import compare_digest

from quart import Quart, current_app
from quart_auth import AuthManager
from rethinkdb import r
from rethinkdb.errors import ReqlNonExistenceError

from . import User

ROLES = 'assistant', 'student', 'supervisor'


class Authenticator(AuthManager):
    user_class = User

    def init_app(self, app: Quart) -> None:
        """Embed auth_manager attribute into app."""
        super().init_app(app)
        self.r = r.table('users')

    async def add_user(self, username: str, password: str,
                       name: str, email: str, role: str) -> None:
        """Try to add user to database."""
        # This never happens through browser, but via manual requests.
        if role not in ROLES: raise ValueError('unknown role')
        async with current_app.db_pool.connection() as connection:
            user = await self.r.get(username).run(connection)
            user = {'username': username, 'password': crypt(password),
                    'name': name, 'role': role}
            if (await self.r.insert(user).run(connection))['errors']:
                raise ValueError('username taken')

    async def log_user(self, username: str, password: str) -> User:
        """Try to log the given user in."""
        user = User(username)
        try:
            digest = await user.password
        except ReqlNonExistenceError:
            raise ValueError('user does not exist')
        if not compare_digest(digest, crypt(password, digest)):
            raise ValueError('bad login')
        return user
