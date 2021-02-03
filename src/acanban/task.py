# Task management pages
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

from quart import Blueprint, ResponseReturnValue, current_app, render_template
from quart_auth import login_required
from rethinkdb import r
from rethinkdb.ast import RqlQuery

from .project import pluck as pluck_project

__all__ = ['blueprint']

BASE_ROUTE = '/p/<uuid>/tasks/<int:index>'
blueprint = Blueprint('task', __name__)


def task_query(project_id: str, index: int) -> RqlQuery:
    """Return the ReQL query for retrieving the specified task."""
    project = r.table('projects').get(project_id)
    return project['tasks'].order_by('created_on')[index]


@blueprint.route(BASE_ROUTE)
@login_required
async def display(uuid: str, index: int) -> ResponseReturnValue:
    """Display task discussion."""
    project = await pluck_project(uuid, ('id', 'name'))
    async with current_app.db_pool.connection() as conn:
        task = await task_query(uuid, index).run(conn)
    return await render_template('task.html', project=project, task=task,
                                 route=f'/p/{uuid}/tasks/{index}')
