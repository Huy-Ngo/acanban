# Authentication handler
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

from enum import Enum, auto
from typing import Optional, Type

from quart import current_app
from quart_auth import AuthManager, AuthUser

__all__ = ['Authenticator']


class Role(Enum):
    STUDENT = auto()
    SUPERVISOR = auto()
    STAFF = auto()
    ADMIN = auto()


class User(AuthUser):
    """Acanban user.

    Parameters
    ----------
    username : Optional[str]
        User's authentication identification.

    Attributes
    ----------
    username : Optional[str]
        Pseudonym to refer to the user.
    password : Optional[str]
        Hash of the user's password.
    name : Optional[str]
        Real name of the user.
    email : Optional[str]
        Email of the user.
    role : Optional[Role]
        Role of the user.
    """

    def __init__(self, username: Optional[str]) -> None:
        super().__init__(username)
        password, name, email, role = current_app.auth_manager.users[username]
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.role = role


class Authenticator(AuthManager):
    user_class = User
