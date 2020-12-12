# User model
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

from typing import Optional

from quart import current_app
from quart_auth import AuthUser
from rethinkdb import r


class User(AuthUser):
    """Acanban user.

    Properties needs to be awaited and ReqlNonExistenceError
    might be raised if the property or the user itself does not exist.

    Parameters
    ----------
    username : Optional[str]
        User's authentication identification.

    Attributes
    ----------
    username : Optional[str]
        Pseudonym to refer to the user.
    password : Optional[str]
        Hash of the user's password.
    name : Optional[str]
        Real name of the user.
    email : Optional[str]
        Email of the user.
    role : Optional[str]
        Role of the user.
    """

    def __init__(self, username: Optional[str]) -> None:
        super().__init__(username)
        self.username = username
        self.r = r.table('users').get(self.username)

    @property
    async def password(self) -> str:
        async with current_app.db_pool.connection() as connection:
            return await self.r['password'].run(connection)

    @property
    async def name(self) -> str:
        async with current_app.db_pool.connection() as connection:
            return await self.r['name'].run(connection)

    @property
    async def email(self) -> str:
        async with current_app.db_pool.connection() as connection:
            return await self.r['email'].run(connection)

    @property
    async def role(self) -> str:
        async with current_app.db_pool.connection() as connection:
            return await self.r['role'].run(connection)
