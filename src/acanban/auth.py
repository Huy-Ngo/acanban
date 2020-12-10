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
from hmac import compare_digest
from typing import Dict, Optional, Tuple

from quart import (Blueprint, Quart, ResponseReturnValue,
                   current_app, redirect, render_template, request)
from quart_auth import AuthManager, AuthUser, login_user, logout_user

__all__ = ['Authenticator', 'blueprint']

ROLES = 'assistant', 'student', 'supervisor'
blueprint = Blueprint('auth', __name__)


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
    role : Optional[str]
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
    users: Dict[Optional[str], Tuple[Optional[str], Optional[str],
                                     Optional[str], Optional[str]]]
    user_class = User

    def init_app(self, app: Quart) -> None:
        """Embed auth_manager attribute into app."""
        super().init_app(app)
        # TODO: wrap the database instead
        self.users = {None: (None, None, None, None)}

    def add_user(self, username: str, password: str,
                 name: str, email: str, role: str) -> None:
        """Try to add user to database."""
        if username in self.users: raise ValueError('username taken')
        # This never happens through browser, but via manual requests.
        if role not in ROLES: raise ValueError('unknown role')
        self.users[username] = crypt(password), name, email, role

    def log_user(self, username: str, password: str) -> User:
        """Try to log the given user in."""
        digest, *info = self.users[username]
        assert digest is not None
        if not compare_digest(digest, crypt(password, digest)):
            raise ValueError('bad login')
        return User(username)


@blueprint.route('/register', methods=['GET', 'POST'])
async def register() -> ResponseReturnValue:
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
        print(info['role'])
        return redirect('/')


@blueprint.route('/login', methods=['GET', 'POST'])
async def login() -> ResponseReturnValue:
    """Handle the login page."""
    if request.method == 'GET': return await render_template('login.html')
    info = await request.form
    username, password = info['username'], info['password']
    try:
        user = current_app.auth_manager.log_user(username, password)
    except ValueError as e:
        return await render_template('login.html', error=str(e))
    else:
        remember = info.get('remember') is not None
        login_user(user, remember)
        return redirect('/')


@blueprint.route("/logout")
async def logout() -> ResponseReturnValue:
    """Handle logout."""
    logout_user()
    return redirect('/')
