# Project pages
# Copyright (C) 2020-2021  Nguyễn Gia Phong
# Copyright (C) 2021  Ngô Ngọc Đức Huy
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

from operator import itemgetter
from typing import Any, Dict, Optional, Sequence

from quart import (Blueprint, ResponseReturnValue, current_app,
                   redirect, render_template, request)
from quart.exceptions import Forbidden, NotFound
from quart_auth import current_user, login_required
from rethinkdb import r
from rethinkdb.errors import ReqlNonExistenceError

from .ipfs import add as ipfs_add

__all__ = ['blueprint']
BASIC_FIELDS = 'id', 'name', 'supervisors', 'students', 'description'

blueprint = Blueprint('project', __name__, url_prefix='/p')


@blueprint.route('/create', methods=['GET', 'POST'])
@login_required
async def create_projects() -> ResponseReturnValue:
    role = await current_user.role
    if role == 'assistant':
        raise Forbidden
    if request.method == 'GET':
        return await render_template('project-create.html')
    project = await request.form
    project = {'name': project['name'],
               'description': project['description'],
               f'{role}s': [current_user.key]}
    async with current_app.db_pool.connection() as connection:
        response = await r.table('projects').insert(project).run(connection)
        uuid = response['generated_keys'][0]
        await r.table('users').get(current_user.key).update(
            {'projects': r.row['projects'].append(uuid)}).run(connection)
    return redirect(f'/p/{uuid}')


@blueprint.route('/')
async def list_projects() -> ResponseReturnValue:
    """Return a page listing all projects."""
    project_list = r.table('projects').pluck(*BASIC_FIELDS)
    async with current_app.db_pool.connection() as connection:
        projects = await project_list.run(connection)
    return await render_template('project-list.html', projects=projects)


@blueprint.route('/<uuid>/')
@login_required
async def info_redirect(uuid: str) -> ResponseReturnValue:
    """Redirect to the project info page."""
    return redirect(f'/p/{uuid}/info')


async def pluck(uuid: str, fields: Sequence[str] = (),
                projects: Optional[Sequence[str]] = None) -> Dict[str, Any]:
    """Pluck the given fields from the project, with permission check."""
    query = r.table('projects').get(uuid).pluck(*fields)
    async with current_app.db_pool.connection() as connection:
        try:
            project = await query.run(connection)
        except ReqlNonExistenceError:
            raise NotFound

    if projects is None:
        try:
            projects = await current_user.projects
        except ReqlNonExistenceError:
            raise Forbidden
    if uuid not in projects: raise Forbidden
    return project


@blueprint.route('/<uuid>/info')
@login_required
async def info(uuid: str) -> ResponseReturnValue:
    """Return the page containing the projects' basic infomation."""
    project = await pluck(uuid, BASIC_FIELDS)
    return await render_template('project-info.html', project=project)


@blueprint.route('/<uuid>/edit', methods=['GET', 'POST'])
@login_required
async def edit(uuid: str) -> ResponseReturnValue:
    """Return the page for editting the projects' basic infomation."""
    if request.method == 'GET':
        project = await pluck(uuid, BASIC_FIELDS)
        return await render_template('project-edit.html', project=project)

    await pluck(uuid)  # check project's existence and permission
    updated = {key: value for key, value in (await request.form).items()
               if key in BASIC_FIELDS and value}
    async with current_app.db_pool.connection() as conn:
        await r.table('projects').get(uuid).update(updated).run(conn)
    return redirect(f'/p/{uuid}/info')


@blueprint.route('/<uuid>/report')
@login_required
async def report(uuid: str) -> ResponseReturnValue:
    """Return the projects' report infomation and forms."""
    user = await current_user.pluck('projects', 'role')
    project = await pluck(uuid, ('id', 'name', 'report'), user.get('projects'))
    query = r.table('files').get_all(*project['report']['revisions'])
    async with current_app.db_pool.connection() as conn:
        revisions = [file async for file in await query.run(conn)]
    revisions.sort(key=itemgetter('time'), reverse=True)
    return await render_template(
        'project-report.html', project=project, report=project['report'],
        revisions=revisions, for_student=(user['role']=='student'))


@blueprint.route('/<uuid>/report/upload', methods=['POST'])
@login_required
async def report_upload(uuid: str) -> ResponseReturnValue:
    """Handle report upload."""
    user = await current_user.pluck('role', 'projects')
    await pluck(uuid, projects=user.get('projects'))
    if user['role'] != 'student': raise Forbidden
    action = r.row['report']['revisions'].append(await ipfs_add())
    async with current_app.db_pool.connection() as conn:
        await r.table('projects').get(uuid).update(
            {'report': {'revisions': action}}).run(conn)
    return redirect(request.referrer)


@blueprint.route('/<uuid>/report/eval', methods=['POST'])
@login_required
async def report_eval(uuid: str) -> ResponseReturnValue:
    """Handle report evaluation."""
    user = await current_user.pluck('role', 'projects')
    await pluck(uuid, projects=user.get('projects'))
    if user['role'] == 'student': raise Forbidden
    form = await request.form
    updated = {'grade': float(form['grade']), 'comment': form['comment']}
    query = r.table('projects').get(uuid).update({'report': updated})
    async with current_app.db_pool.connection() as conn: await query.run(conn)
    return redirect(request.referrer)
