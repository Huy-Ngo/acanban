# Common test fixtures
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

from typing import AsyncIterator

from pytest import fixture
from quart.testing import QuartClient

from acanban import Acanban, app


@fixture(name='app')
async def acanban() -> AsyncIterator[Acanban]:
    async with app.test_app() as test_app: yield test_app


@fixture
def client(app: Acanban) -> QuartClient:
    """Return a Quart test client."""
    return app.test_client()
