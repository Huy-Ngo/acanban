# Routes for authentication
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

from quart import (Blueprint, ResponseReturnValue, current_app,
                   redirect, render_template, request)
from quart_auth import login_user, logout_user

blueprint = Blueprint('auth', __name__)


@blueprint.route('/register', methods=['GET', 'POST'])
async def register() -> ResponseReturnValue:
    """Handle the registration page."""
    if request.method == 'GET': return await render_template('register.html')
    info = await request.form
    try:
        await current_app.auth_manager.add_user(
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
        user = await current_app.auth_manager.log_user(username, password)
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
