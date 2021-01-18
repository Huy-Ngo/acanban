# Test users
# Copyright (C) 2020  Ngô Ngọc Đức Huy
# Copyright (C) 2021  Nguyễn Gia Phong
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

from http import HTTPStatus as Status

from conftest import ClientFactory, parametrize
from pytest import param
from quart.testing import QuartClient


@parametrize(('username', 'status_code'),
             (param('nexistepas', Status.NOT_FOUND, id='not exist'),
              param('adaml', Status.OK, id='can have projects'),
              param('silasl', Status.OK, id='cannot have projects')))
async def test_get(username: str, status_code: int,
                   client: QuartClient) -> None:
    """Test GET user root endpoint."""
    response = await client.get(f'/u/{username}')
    assert response.status_code == status_code


@parametrize(('username', 'profile', 'status_code'),
             (('adaml', 'silasl', Status.FORBIDDEN),
              ('adaml', 'adaml', Status.OK)))
async def test_edit_get(username: str, profile: str,
                        status_code: int, user: ClientFactory) -> None:
    """Test GET user edit endpoint."""
    client = await user(username)
    response = await client.get(f'/u/{profile}/edit')
    assert response.status_code == status_code


@parametrize(('username', 'profile', 'status_code'),
             (('adaml', 'silasl', Status.FORBIDDEN),
              ('adaml', 'adaml', Status.FOUND)))
async def test_edit_post(username: str, profile: str,
                         status_code: int, user: ClientFactory) -> None:
    """Test POST user edit endpoint."""
    client = await user(username)
    info = {'name': 'Silas Salis', 'email': 'newemail@example.edu'}
    response = await client.post(f'/u/{profile}/edit', form=info)
    assert response.status_code == status_code
