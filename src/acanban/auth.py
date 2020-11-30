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

from crypt import crypt
from enum import Enum, auto
from hmac import compare_digest
from typing import Dict, Optional, Tuple, Union

from quart import (Blueprint, Quart, Response, current_app,
                   redirect, render_template, request)
from quart_auth import AuthManager, AuthUser

__all__ = ['Authenticator', 'blueprint']

blueprint = Blueprint('auth', __name__)


class Role(Enum):
    STUDENT = auto()
    SUPERVISOR = auto()
    STAFF = auto()
    ADMIN = auto()


UserData = Tuple[Optional[str], Optional[str], Optional[str], Optional[Role]]


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

    def init_app(self, app: Quart) -> None:
        """Embed auth_manager attribute into app."""
        super().init_app(app)
        # TODO: wrap the database instead
        self.users: Dict[Optional[str], UserData] = {
            None: (None, None, None, None),
            'foo': (crypt('bar'), 'Foo Bar', 'foo@bar.baz', Role.STUDENT)}

    def add_user(self, username: str, password: str,
                 name: str, email: str, role: Role) -> None:
        """Try to add user to database."""
        if username in self.users: raise ValueError('username taken')
        self.users[username] = crypt(password), name, email, role


@blueprint.route('/register', methods=['GET', 'POST'])
async def register() -> Union[str, Response]:
    """Handle the registration page."""
    if request.method == 'GET': return await render_template('register.html')
    info = await request.form
    try:
        current_app.auth_manager.add_user(
            info['username'], info['password'],
            info['name'], info['email'], info['role'])
    except ValueError as e:
        return await render_template('register.html', error=str(e))
    else:
        return redirect('/')
