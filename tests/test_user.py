# Test users
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

from pytest import mark
from quart.testing import QuartClient


@mark.parametrize(('username', 'code'),
                  (('nexistepas', 404), ('kiddo', 404),
                   ('silasl', 200), ('adaml', 200)))
async def test_view(username: str, code: int,
                    client: QuartClient) -> None:
    """Test user view endpoint."""
    response = await client.get(f'/u/{username}')
    assert response.status_code == code


@mark.parametrize(('username', 'code'),
                  (('silasl', 200), ('adaml', 403)))
async def test_edit_view(username: str, code: int,
                         assistant: QuartClient) -> None:
    """Test user edit endpoint (GET method)."""
    response = await assistant.get(f'/u/{username}/edit')
    assert response.status_code == code


async def test_edit_good(assistant: QuartClient) -> None:
    """Test for user editing name (POST method)."""
    response = await assistant.post(
        '/u/silasl/edit', form=dict(name='Silas Salis',
                                    email='newemail@example.edu'))
    assert response.status_code == 302


async def test_edit_bad_1(assistant: QuartClient) -> None:
    """Test for user bad request (send empty string)."""
    response = await assistant.post(
        '/u/silasl/edit', form=dict(name='', email='newmail@example.edu'))
    assert response.status_code == 400


async def test_edit_bad_2(assistant: QuartClient) -> None:
    """Test for user sending bad request (lacking field)."""
    response = await assistant.post(
        '/u/silasl/edit', form=dict(name='Lacking Email'))
    assert response.status_code == 400
