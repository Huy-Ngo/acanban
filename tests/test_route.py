# Test basic routing
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

from conftest import ClientFactory, parametrize
from quart.testing import QuartClient


@parametrize(('uri', 'status_code'), (
    ('/', 200), ('/p/', 200),
    ('/register', 200), ('/login', 200), ('/logout', 302),
    ('/ipfs/QmPTWcNNxPdVwqQ939rsxJQiiditfw9YNyLMs9QZJM4gCU', 200),
    ('/ipfs/QmRW3V9znzFW9M5FYbitSEvd5dQrPWGvPvgQD6LM22Tv8D', 301),
    ('/ipns/ipfs.io', 301), ('/ipfs/ipfs.io', 404)))
async def test_status(uri: str, status_code: int, client: QuartClient) -> None:
    """Test the status of basic routes."""
    response = await client.get(uri)
    assert response.status_code == status_code
    await response.get_data()


async def test_myproject_status(user: ClientFactory) -> None:
    """Test the status of user dashboard."""
    client = await user('adaml')
    response = await client.get('/')
    assert response.status_code == 200
