# Initialization code
# Copyright (C) 2020  Ngô Xuân Minh
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

from typing import Optional
from rethinkdb import r
from quart import (Blueprint, Quart, ResponseReturnValue,
                   current_app, redirect, render_template, request)
from quart_auth import login_user, logout_user
from .db import RethinkObject


ROLES = 'student', 'supervisor'
blueprint = Blueprint('project', __name__)

class Project(RethinkObject):
    slots = ['name', 'description' 
             'creator', 'supervisor',
             'participants', 'tasks']

    table = 'projects'


async def create_project(self, name: str, description: str) -> None:
    async with current_app.db_pool.connection() as connection:
        project = {'name': name, 'description': description}
        await r.table('projects').insert(project).run(connection)

@blueprint.route('/p', methods=['GET', 'POST'])
async def create_projects() -> ResponseReturnValue:
    if request.method == 'GET':
        return await render_template('project.html')
    project = await request.form
    try:
        await current_app.create_project(project['name'],
                                         project['description'])
    except ValueError as e:
        return await render_template('project.html', error=str(e))
    else:
        print(project['name'])
        return redirect('/p')
