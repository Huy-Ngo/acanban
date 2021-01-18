# Common test fixtures
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

from typing import AsyncIterator, Awaitable, Callable, Optional

from pytest import fixture, mark
from quart.testing import QuartClient

from acanban import Acanban, app

ClientFactory = Callable[[Optional[str]], Awaitable[QuartClient]]
parametrize = mark.parametrize


@fixture(name='app')
async def acanban() -> AsyncIterator[Acanban]:
    async with app.test_app() as test_app: yield test_app


@fixture
def client(app: Acanban) -> QuartClient:
    """Return a Quart test client."""
    return app.test_client()


@fixture
async def user(client: QuartClient) -> ClientFactory:
    """Return a coroutine which gives a logged client."""
    async def login(username: Optional[str]) -> QuartClient:
        """Return the logged client if username is not None."""
        if username is None: return client  # I'm sorry Nathaniel!
        form = {'username': username, 'password': username[::-1]}
        await client.post('/login', form=form)
        return client

    return login
