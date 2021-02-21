# Test task-specific routes
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
from typing import Optional

from conftest import ClientFactory, parametrize
from pytest import param

# Some members: evelynd (student), ronanf (supervisor)
# Some nonmembers: adaml (student), silasl (assistant)
BASE_ROUTE = '/p/7fee498b-98ac-4173-b600-e94618f9ea1f/tasks/0'


@parametrize(('username', 'status_code'),
             (param(None, Status.UNAUTHORIZED, id='guest'),
              param('silasl', Status.FORBIDDEN, id='assistant'),
              param('adaml', Status.FORBIDDEN, id='nonmember'),
              param('ronanf', Status.OK, id='member')))
async def test_get(username: Optional[str], status_code: int,
                   user: ClientFactory) -> None:
    """Test task access permission."""
    client = await user(username)
    response = await client.get(f'{BASE_ROUTE}/')
    assert response.status_code == status_code


@parametrize(('username', 'status_code'),
             (param(None, Status.UNAUTHORIZED, id='guest'),
              param('silasl', Status.FORBIDDEN, id='assistant'),
              param('adaml', Status.FORBIDDEN, id='nonmember'),
              param('ronanf', Status.FOUND, id='member')))
@parametrize('direction', ('dec', 'inc'))
async def test_move(username: Optional[str], status_code: int,
                    user: ClientFactory, direction: str) -> None:
    """Test moving task across columns."""
    client = await user(username)
    response = await client.get(f'{BASE_ROUTE}/{direction}')
    assert response.status_code == status_code


@parametrize(('username', 'comment', 'status_code'),
             (param(None, 1609023842.0, Status.UNAUTHORIZED, id='guest'),
              param('silasl', 1609023842.0, Status.FORBIDDEN, id='assistant'),
              param('adaml', 1609023842.0, Status.FORBIDDEN, id='nonmember'),
              param('ronanf', 1609023842.0, Status.FOUND, id='member'),
              param('ronanf', 420.69, Status.NOT_FOUND, id='unknown comment')))
async def test_reply(username: Optional[str], comment: float,
                     status_code: int, user: ClientFactory) -> None:
    """Test replying to a comment."""
    client = await user(username)
    response = await client.post(f'{BASE_ROUTE}/reply/{comment}',
                                 form={'comment': 'Alright.'})
    assert response.status_code == status_code
