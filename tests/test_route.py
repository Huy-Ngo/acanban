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

from pytest import mark
from quart.testing import QuartClient


@mark.parametrize(('uri', 'status_code'),
                  (('/', 200), ('/register', 200), ('/login', 200),
                   ('/logout', 302), ('/foobar', 404)))
async def test_status(uri: str, status_code: int, client: QuartClient) -> None:
    """Test the status of basic routes."""
    response = await client.get(uri)
    assert response.status_code == status_code
