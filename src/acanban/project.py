# Project pages
# Copyright (C) 2020  Ngô Xuân Minh
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

from quart import (Blueprint, ResponseReturnValue,
                   current_app, redirect, render_template, request)
from rethinkdb import r
from .db import RethinkObject


__all__ = ['blueprint']
ROLES = 'student', 'supervisor'
BASIC_FIELDS = 'name', 'supervisor', 'participants', 'description'
blueprint = Blueprint('project', __name__, url_prefix='/p')


class Project(RethinkObject):
    slots = ('name', 'description', 'creator',
             'supervisor', 'participants', 'tasks')

    table = 'projects'


@blueprint.route('/create', methods=['GET', 'POST'])
async def create_projects() -> ResponseReturnValue:
    if request.method == 'GET':
        return await render_template('project_create.html')
    project = await request.form
    async with current_app.db_pool.connection() as connection:
        project = {'name': project['name'],
                    'description': project['description']}
        await r.table('projects').insert(project).run(connection)
    return redirect('/p')


@blueprint.route('/')
async def list_projects() -> ResponseReturnValue:
    """Return a page listing all projects."""
    project_list = r.table('projects').pluck(*BASIC_FIELDS)
    async with current_app.db_pool.connection() as connection:
        projects = await project_list.run(connection)
    return await render_template('project_list.html', projects=projects)
