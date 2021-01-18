# Authentication handler
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
from typing import Optional

from quart import (Blueprint, ResponseReturnValue, current_app,
                   redirect, render_template, request)
from quart_auth import AuthManager, AuthUser, login_user, logout_user
from rethinkdb import r
from rethinkdb.errors import ReqlNonExistenceError

from .db import RethinkObject

__all__ = ['Authenticator', 'blueprint']

ROLES = 'assistant', 'student', 'supervisor'
blueprint = Blueprint('auth', __name__)


class User(AuthUser, RethinkObject):
    """Acanban user.

    Properties needs to be awaited and ReqlNonExistenceError
    might be raised if the property or the user itself does not exist.

    Parameters
    ----------
    username : Optional[str]
        User's authentication identification.

    Attributes
    ----------
    username : str
        Pseudonym to refer to the user.
    password : str
        Hash of the user's password.
    name : str
        Real name of the user.
    email : str
        Email of the user.
    role : str
        Role of the user.
    """

    slots = 'username', 'password', 'name', 'email', 'role', 'projects'
    table = 'users'

    def __init__(self, username: Optional[str]) -> None:
        super().__init__(username)
        self.key = '' if username is None else username


class Authenticator(AuthManager):
    user_class = User


async def add_user(username: str, password: str,
                   name: str, email: str, role: str) -> None:
    """Try to add user to database."""
    # This never happens through browser, but via manual requests.
    if role not in ROLES: raise ValueError('unknown role')
    user = {'username': username, 'password': crypt(password),
            'name': name, 'email': email, 'role': role}
    async with current_app.db_pool.connection() as connection:
        user_with_mail = await r.table('users').filter(
            {'email': email}).count().run(connection)
        if user_with_mail > 0:
            raise ValueError('email taken')
        if (await r.table('users').insert(user).run(connection))['errors']:
            raise ValueError('username taken')


@blueprint.route('/register', methods=['GET', 'POST'])
async def register() -> ResponseReturnValue:
    """Handle the registration page."""
    if request.method == 'GET': return await render_template('register.html')
    info = await request.form
    try:
        await add_user(info['username'], info['password'],
                       info['name'], info['email'], info['role'])
    except ValueError as e:
        return await render_template('register.html', error=str(e))
    else:
        return redirect('/')


async def log_user(username: str, password: str) -> User:
    """Try to log the given user in."""
    user = User(username)
    try:
        digest = await user.password
    except ReqlNonExistenceError:
        raise ValueError('user does not exist')
    if not compare_digest(digest, crypt(password, digest)):
        raise ValueError('bad login')
    return user


@blueprint.route('/login', methods=['GET', 'POST'])
async def login() -> ResponseReturnValue:
    """Handle the login page."""
    if request.method == 'GET': return await render_template('login.html')
    info = await request.form
    username, password = info['username'], info['password']
    try:
        user = await log_user(username, password)
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
