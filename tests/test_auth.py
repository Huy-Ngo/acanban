# Test authentication handling
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

from pytest import mark
from quart.testing import QuartClient

from acanban import Acanban
from acanban.auth import User


@mark.parametrize(('username', 'role', 'code'),
                  (('huyngo', 'student', 302), ('kiddo', 'pupil', 200),
                   ('silasl', 'supervisor', 200)))
async def test_register(username: str, role: str, code: int,
                        client: QuartClient) -> None:
    """Test successful and failed registration."""
    response = await client.post('/register', form=dict(
        username=username, password='baz',
        name='Fô Bả', email='f@o.o', role=role))
    # Successful registration redirects.
    assert response.status_code == code


@mark.parametrize(('username', 'password', 'code'),
                  (('huyngo', 'baz', 302), ('silasl', 'lsalis', 302),
                   ('opheliad', 'wrong', 200), ('ne-existe', 'pas', 200)))
async def test_login(username: str, password: str, code: int,
                     client: QuartClient) -> None:
    """Test successful and failed login."""
    response = await client.post(
        '/login', form=dict(username=username, password=password))
    # Successful login redirects.
    assert response.status_code == code


async def test_user(app: Acanban) -> None:
    """Test if properties for User object is correct."""
    async with app.app_context():
        user = User('silasl')
        digest = await user.password
        assert compare_digest(digest, crypt('lsalis', digest))
        assert await user.email == 'silasl@example.edu'
        assert await user.name == 'Silas Lehtonen'
        assert await user.role == 'assistant'
