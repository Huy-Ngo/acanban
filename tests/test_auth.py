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

from http import HTTPStatus

from pytest import mark
from quart.testing import QuartClient


@mark.parametrize(('username', 'role', 'code'),
                  (('kiddo', 'pupil', 200),
                   ('silasl', 'supervisor', 200),
                   ('huyngo', 'student', 302)))
async def test_register(username: str, role: str, code: int,
                        client: QuartClient) -> None:
    """Test successful and failed registration."""
    response = await client.post('/register', form=dict(
        username=username, password='baz',
        name='Fô Bả', email='f@o.o', role=role))
    # Successful registration redirects.
    assert response.status_code == code


async def test_register_existing_email(client: QuartClient) -> None:
    """Test failed registration where the email is taken."""
    response = await client.post('/register', form=dict(
        username='notronanf', password='some-password',
        name='Ronan Franklin', email='ronanf@example.edu', role='supervisor'))
    assert response.status_code == HTTPStatus.OK


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
