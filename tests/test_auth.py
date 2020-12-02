# Test authentication handling
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

from crypt import crypt

# XXX: from pytest 6.2, use pytest.MonkeyPatch
from _pytest.monkeypatch import MonkeyPatch
from pytest import fixture, mark
from quart.testing import QuartClient

from acanban import Acanban


@fixture
def user_foo(app: Acanban, monkeypatch: MonkeyPatch) -> None:
    """Provide user foo."""
    monkeypatch.setitem(
        app.auth_manager.users,
        'foo', (crypt('bar'), 'Foo Bar', 'foo@bar.baz', 'assistant'))


@mark.parametrize(('username', 'role', 'success'),
                  (('foo', 'student', False), ('bar', 'pupil', False),
                   ('bar', 'student', True)))
async def test_register(username: str, role: str, success: bool,
                        client: QuartClient, user_foo: None) -> None:
    """Test successful and failed registration."""
    response = await client.post('/register', form=dict(
        username=username, password='baz',
        name='Fô Bả', email='f@o.o', role=role))
    # Successful registration redirects.
    assert (response.status_code == 302) is success


@mark.parametrize(('username', 'password', 'success'),
                  (('foo', 'bar', True), ('foo', 'baz', False)))
async def test_login(username: str, password: str, success: bool,
                     client: QuartClient, user_foo: None) -> None:
    """Test successful and failed login."""
    response = await client.post(
        '/login', form=dict(username=username, password=password))
    # Successful login redirects.
    assert (response.status_code == 302) is success
