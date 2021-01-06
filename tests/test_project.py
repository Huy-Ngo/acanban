# Test project pages
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

from http import HTTPStatus as Status

from quart.testing import QuartClient

PROJECT = '/p/be7a04b8-650f-41dc-912b-10d225baff29/'
PROJECT_INFO = f'{PROJECT}info'
PROJECT_EDIT = f'{PROJECT}edit'


async def test_info_nonexist(student: QuartClient) -> None:
    """Test accessing a nonexistent project info page."""
    response = await student.get('/p/this-project-does-not-exist/info')
    assert response.status_code == Status.NOT_FOUND


async def test_redirect(client: QuartClient) -> None:
    """Test the redirect for the client."""
    response = await client.get(PROJECT)
    assert response.status_code == Status.PERMANENT_REDIRECT


async def test_info_access_guest(client: QuartClient) -> None:
    """Test project info page access by a guest."""
    response = await client.get(PROJECT_INFO)
    assert response.status_code == Status.UNAUTHORIZED


async def test_info_access_assistant(assistant: QuartClient) -> None:
    """Test project info page access by an assistant."""
    response = await assistant.get(PROJECT_INFO)
    assert response.status_code == Status.UNAUTHORIZED


# This supervisor is not a member of PROJECT.
async def test_info_access_nonmember(supervisor: QuartClient) -> None:
    """Test project info page access by a non-member user."""
    response = await supervisor.get(PROJECT_INFO)
    assert response.status_code == Status.UNAUTHORIZED


# This student is a member of PROJECT.
async def test_info_access_member(student: QuartClient) -> None:
    """Test project info page access by a member."""
    response = await student.get(PROJECT_INFO)
    assert response.status_code == Status.OK
