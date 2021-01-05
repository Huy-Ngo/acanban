# Project pages
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

from quart import Blueprint, ResponseReturnValue, current_app, render_template
from rethinkdb import r

__all__ = ['blueprint']
BASIC_FIELDS = 'id', 'name', 'supervisors', 'students', 'description'

blueprint = Blueprint('project', __name__, url_prefix='/p')


@blueprint.route('/')
async def list_projects() -> ResponseReturnValue:
    """Return a page listing all projects."""
    project_list = r.table('projects').pluck(*BASIC_FIELDS)
    async with current_app.db_pool.connection() as connection:
        projects = await project_list.run(connection)
    return await render_template('projects.html', projects=projects)
