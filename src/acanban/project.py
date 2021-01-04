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
<<<<<<< HEAD
from quart_auth import login_user, logout_user
from .db import RethinkObject


ROLES = 'student', 'supervisor'
blueprint = Blueprint('project', __name__)
=======
from quart_auth import AuthManager, AuthUser, login_user, logout_user
from .db import RethinkObject

from acanban.auth import User

ROLES = 'student', 'supervisor'
blueprint = Blueprint('project', __name__)
auth_manager = AuthManager()
>>>>>>> 25b1ef66207b3ee6ad21ed8b6b4c217d77874c05

class Project(RethinkObject):
    slots = ['name', 'description' 
             'creator', 'supervisor',
             'participants', 'tasks']

    table = 'projects'

<<<<<<< HEAD

async def create_project(self, name: str, description: str) -> None:
    async with current_app.db_pool.connection() as connection:
        project = {'name': name, 'description': description}
        await r.table('projects').insert(project).run(connection)

@blueprint.route('/p', methods=['GET', 'POST'])
async def create_projects() -> ResponseReturnValue:
=======
    def __init__(self, name: Optional[str]) -> None:
        super().__init__(name)
        self.key = '' if name is None else name


class ProjectManagement():
    project_class = Project

    def init_app(self, app: Quart) -> None:
        super().init_app(app)
        self.r = r.table('projects')

    async def create_project(self, name: str, description: str, 
                            creator: str, supervisor: str, 
                            participants: list, tasks: list) -> None:
        async with current_app.db_pool.connection() as connection:
            project = await self.r.get(name).run(connection)
            project = {'name': name, 'description': description,
                      'creator': creator, 'supervisor': supervisor,
                      'participants': participants, 'tasks': tasks}
            await self. r.insert(project).run(connection)

    async def join_project(self, name: str, username: str) -> None:
        async with current_app.db_pool.connection() as connection:
            await self.r.get(name)['participants'].append(username)


@blueprint.route('/project', methods=['GET', 'POST'])
async def create() -> ResponseReturnValue:
>>>>>>> 25b1ef66207b3ee6ad21ed8b6b4c217d77874c05
    if request.method == 'GET':
        return await render_template('project.html')
    project = await request.form
    try:
<<<<<<< HEAD
        await current_app.create_project(project['name'],
                                         project['description'])
=======
        await current_app.create_project(
            project['name'], project['description'],
            project['creator'], project['supervisor'],
            project['participants'], project['tasks'])
>>>>>>> 25b1ef66207b3ee6ad21ed8b6b4c217d77874c05
    except ValueError as e:
        return await render_template('project.html', error=str(e))
    else:
        print(project['name'])
<<<<<<< HEAD
        return redirect('/p')
=======
        return redirect('/')
>>>>>>> 25b1ef66207b3ee6ad21ed8b6b4c217d77874c05
