# User profile endpoints
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

from quart import (Blueprint, ResponseReturnValue, abort,
                   redirect, render_template, request, url_for)
from quart_auth import current_user
from rethinkdb.errors import ReqlNonExistenceError
from werkzeug.exceptions import BadRequestKeyError

from .auth import User

__all__ = ['blueprint']

blueprint = Blueprint('user', __name__, url_prefix='/u')


@blueprint.app_template_filter()
def userlink(username: str) -> str:
    """Generate the link to the given user."""
    return f'<a href=/u/{username}>{username}</a>'


@blueprint.route('/<username>', methods=['GET'])
async def view_user_profile(username: str) -> ResponseReturnValue:
    """Handle the user profile page."""
    user = User(username)
    try:
        return await render_template('user_profile.html',
                                     username=user.key,
                                     email=await user.email,
                                     role=await user.role,
                                     name=await user.name)
    except ReqlNonExistenceError:
        abort(HTTPStatus.NOT_FOUND)


@blueprint.route('/<username>/edit', methods=['GET', 'POST'])
async def edit_user_profile(username: str) -> ResponseReturnValue:
    """Handle the profile edit page."""
    user = User(username)
    if user.key != current_user.key:
        abort(HTTPStatus.FORBIDDEN)
    if request.method == 'GET':
        return await render_template('user_profile_edit.html',
                                     email=await user.email,
                                     name=await user.name)
    info = await request.form
    try:
        data = {'name': info['name'],
                'email': info['email']}
    except BadRequestKeyError:
        abort(HTTPStatus.BAD_REQUEST)
    if data['name'] == '' or data['email'] == '':
        abort(HTTPStatus.BAD_REQUEST)
    await user.update(**data)
    return redirect(url_for('user.view_user_profile', username=username))
