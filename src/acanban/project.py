# Project pages
# Copyright (C) 2020-2021  Nguyễn Gia Phong
# Copyright (C) 2021  Ngô Ngọc Đức Huy
# Copyright (C) 2021  Ngô Xuân Minh
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

from functools import partial
from operator import itemgetter
from typing import Any, Dict, Sequence

from quart import (Blueprint, ResponseReturnValue, current_app,
                   redirect, render_template, request)
from quart.exceptions import Forbidden, NotFound
from quart_auth import current_user, login_required
from rethinkdb import r
from rethinkdb.errors import ReqlNonExistenceError

from .ipfs import add as ipfs_add

__all__ = ['PREVIEW_FIELDS', 'blueprint']

INFO_FIELDS = 'id', 'name', 'description'
MEMBERS_FIELDS = 'id', 'name', 'supervisors', 'students'
PREVIEW_FIELDS = 'id', 'name', 'description', 'supervisors', 'students'

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
    project = {
        'name': project['name'], 'description': project['description'],
        'students': [], 'supervisors': [], f'{role}s': [current_user.key],
        'tasks': [], 'report': {'revisions': []}, 'slides': {'revisions': []}}
    async with current_app.db_pool.connection() as connection:
        response = await r.table('projects').insert(project).run(connection)
        uuid = response['generated_keys'][0]
    return redirect(f'/p/{uuid}')


@blueprint.route('/')
async def list_projects() -> ResponseReturnValue:
    """Return a page listing all projects."""
    project_list = r.table('projects').pluck(*PREVIEW_FIELDS)
    async with current_app.db_pool.connection() as connection:
        projects = await project_list.run(connection)
    return await render_template('project-list.html', projects=projects)


@blueprint.route('/<uuid>/')
@login_required
async def info_redirect(uuid: str) -> ResponseReturnValue:
    """Redirect to the project info page."""
    return redirect(f'/p/{uuid}/info')


async def pluck(uuid: str, fields: Sequence[str] = ()) -> Dict[str, Any]:
    """Pluck the given fields from the project, with permission check."""
    async with current_app.db_pool.connection() as connection:
        try:
            project = await r.table('projects').get(uuid).pluck(
                'students', 'supervisors', *fields).run(connection)
        except ReqlNonExistenceError:
            raise NotFound

    members = project['students'] + project['supervisors']
    if current_user.key not in members: raise Forbidden
    return {key: value for key, value in project.items() if key in fields}


@blueprint.route('/<uuid>/info')
@login_required
async def info(uuid: str) -> ResponseReturnValue:
    """Return the page containing the projects' basic infomation."""
    project = await pluck(uuid, INFO_FIELDS)
    return await render_template('project-info.html', project=project)


@blueprint.route('/<uuid>/edit', methods=['GET', 'POST'])
@login_required
async def edit(uuid: str) -> ResponseReturnValue:
    """Return the page for editting the projects' basic infomation."""
    if request.method == 'GET':
        project = await pluck(uuid, INFO_FIELDS)
        return await render_template('project-edit.html', project=project)

    await pluck(uuid)  # check project's existence and permission
    updated = {key: value for key, value in (await request.form).items()
               if key in INFO_FIELDS and value}
    async with current_app.db_pool.connection() as conn:
        await r.table('projects').get(uuid).update(updated).run(conn)
    return redirect(f'/p/{uuid}/info')


@blueprint.route('/<uuid>/members')
@login_required
async def member_list(uuid: str) -> ResponseReturnValue:
    """Return the page listing the member of a project."""
    project = await pluck(uuid, MEMBERS_FIELDS)
    return await render_template('project-members.html', project=project)


@blueprint.route('/<uuid>/invite', methods=['POST'])
@login_required
async def member_invite(uuid: str) -> ResponseReturnValue:
    """Add a member to the project."""
    username = (await request.form)['new-user']
    project = await pluck(uuid, MEMBERS_FIELDS)
    render = partial(render_template, 'project-members.html', project=project)

    async with current_app.db_pool.connection() as conn:
        try:
            role = await r.table('users').get(username)['role'].run(conn)
        except ReqlNonExistenceError:
            return await render(error=f'{username} has not registered')
    if role == 'assistant':
        return await render(error=f'{username} is an assistant')
    mem_field = f'{role}s'
    if username in project[mem_field]:
        return await render(error=f'{username} is already a member')

    async with current_app.db_pool.connection() as conn:
        await r.table('projects').get(uuid).update(
            {mem_field: r.row[mem_field].append(username)}).run(conn)
        await r.table('users').get(username).update(
            {'projects': r.row['projects'].append(uuid)}).run(conn)
    return redirect(request.referrer)


async def artifact_view(tab: str, uuid: str) -> ResponseReturnValue:
    """Return the tab with artifact upload and evaluation."""
    await pluck(uuid)  # check project's existence and permission
    project = await pluck(uuid, ('id', 'name', tab))
    query = r.table('files').get_all(*project[tab]['revisions'])
    async with current_app.db_pool.connection() as conn:
        revisions = [file async for file in await query.run(conn)]
    revisions.sort(key=itemgetter('time'), reverse=True)
    variables = {'project': project, tab: project[tab], 'revisions': revisions,
                 'for_student': (await current_user.role)=='student'}
    return await render_template(f'project-{tab}.html', **variables)


async def artifact_upload(tab: str, uuid: str) -> ResponseReturnValue:
    """Handle file upload to the corresponding tab."""
    await pluck(uuid)  # check project's existence and permission
    if await current_user.role != 'student': raise Forbidden
    action = r.row[tab]['revisions'].append(await ipfs_add())
    async with current_app.db_pool.connection() as conn:
        await r.table('projects').get(uuid).update(
            {tab: {'revisions': action}}).run(conn)
    return redirect(request.referrer)


async def artifact_eval(tab: str, uuid: str) -> ResponseReturnValue:
    """Handle evaluation of the work in the corresponding tab."""
    await pluck(uuid)  # check project's existence and permission
    if await current_user.role == 'student': raise Forbidden
    form = await request.form
    updated = {'grade': float(form['grade']), 'comment': form['comment']}
    query = r.table('projects').get(uuid).update({tab: updated})
    async with current_app.db_pool.connection() as conn: await query.run(conn)
    return redirect(request.referrer)


def add_artifact_tab(blueprint: Blueprint, tab: str) -> None:
    """Add tab of the given name to the blueprint.

    Raise ValueError if tab is neither report nor slides.
    """
    if tab not in ('report', 'slides'):
        raise ValueError(f'tab is neither report nor slides: {tab}')
    blueprint.add_url_rule(
        f'/<uuid>/{tab}', methods=['GET'], endpoint=f'{tab}_view',
        view_func=login_required(partial(artifact_view, tab)))
    blueprint.add_url_rule(
        f'/<uuid>/{tab}/upload', methods=['POST'], endpoint=f'{tab}_upload',
        view_func=login_required(partial(artifact_upload, tab)))
    blueprint.add_url_rule(
        f'/<uuid>/{tab}/eval', methods=['POST'], endpoint=f'{tab}_eval',
        view_func=login_required(partial(artifact_eval, tab)))


add_artifact_tab(blueprint, 'report')
add_artifact_tab(blueprint, 'slides')
