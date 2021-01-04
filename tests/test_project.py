# Test project management handling
# Copyright (C) 2020  Ngô Xuân Minh
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


@mark.parametrize(('name', 'code'),
                  (('minigh', 302),
                   ('acanban', 302)))
async def test_create(name: str, code: int, client: QuartClient) -> None:
    """Test successful and failed create project."""
    response = await client.post('/p', form=dict(
        name=name, description='MAD',
        creator='Fô Bả', supervisor='f@o.o',
        participants=['huy', 'phong', 'minh'],
        tasks=['login', 'menu', 'repo']))

    assert response.status_code == code
