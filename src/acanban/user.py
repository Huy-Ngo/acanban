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

from quart import (Blueprint, ResponseReturnValue, current_app,
                   redirect, render_template, request)
from quart.exceptions import Forbidden, NotFound
from quart_auth import current_user
from rethinkdb import r

__all__ = ['blueprint']
MUTABLE_FIELDS = 'name', 'email', 'student-id', 'department'

blueprint = Blueprint('user', __name__, url_prefix='/u')
users = r.table('users')


@blueprint.app_template_filter()
def userlink(username: str) -> str:
    """Generate the link to the given user."""
    return f'<a href=/u/{username}>{username}</a>'


@blueprint.route('/<username>', methods=['GET'])
async def view_user_profile(username: str) -> ResponseReturnValue:
    """Handle the user profile page."""
    async with current_app.db_pool.connection() as conn:
        user = await users.get(username).run(conn)
        if user is None:
            raise NotFound
        project_uuids = user.get('projects', None)
        if project_uuids is None:
            return await render_template('user.html', user=user)
        project_list = r.table('projects').get_all(*project_uuids)
        projects = await project_list.run(conn)
        return await render_template('user.html', user=user, projects=projects)


@blueprint.route('/<username>/edit', methods=['GET', 'POST'])
async def edit_user_profile(username: str) -> ResponseReturnValue:
    """Handle the profile edit page."""
    if username != current_user.key: raise Forbidden
    if request.method == 'GET':
        async with current_app.db_pool.connection() as conn:
            user = await users.get(username).run(conn)
        return await render_template('user-edit.html', user=user)
    updated = {key: value for key, value in (await request.form).items()
               if key in MUTABLE_FIELDS and value}
    async with current_app.db_pool.connection() as conn:
        await users.get(username).update(updated).run(conn)
    return redirect(f'/u/{username}')
