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

from operator import itemgetter
from typing import Any, Dict, Iterator

from quart import (Blueprint, ResponseReturnValue, current_app,
                   redirect, render_template, request)
from quart.exceptions import NotFound
from quart_auth import current_user, login_required
from rethinkdb import r
from rethinkdb.ast import RqlQuery

from .project import pluck as pluck_project

__all__ = ['blueprint']

blueprint = Blueprint('task', __name__,
                      url_prefix='/p/<uuid>/tasks/<int:index>')


def task_query(project_id: str, index: int) -> RqlQuery:
    """Return the ReQL query for retrieving the specified task."""
    project = r.table('projects').get(project_id)
    return project['tasks'].order_by('created_on')[index]


@blueprint.route('/')
@login_required
async def display(uuid: str, index: int) -> ResponseReturnValue:
    """Display task discussion."""
    project = await pluck_project(uuid, ('id', 'name'))
    async with current_app.db_pool.connection() as conn:
        task = await task_query(uuid, index).run(conn)
    return await render_template('task.html', project=project, task=task,
                                 route=f'/p/{uuid}/tasks/{index}')


@blueprint.route('/dec')
@login_required
async def move_backward(uuid: str, index: int) -> ResponseReturnValue:
    """Move the task to the previous column."""
    await pluck_project(uuid)  # check authority
    async with current_app.db_pool.connection() as conn:
        task = await task_query(uuid, index).run(conn)
        updated = {'tasks': r.row['tasks'].order_by('created_on').change_at(
            index, {**task, 'status': max(0, task['status']-1)})}
        await r.table('projects').get(uuid).update(updated).run(conn)
    return redirect(request.referrer)


@blueprint.route('/inc')
@login_required
async def move_forward(uuid: str, index: int) -> ResponseReturnValue:
    """Move the task to the next column."""
    await pluck_project(uuid)  # check authority
    async with current_app.db_pool.connection() as conn:
        task = await task_query(uuid, index).run(conn)
        updated = {'tasks': r.row['tasks'].order_by('created_on').change_at(
            index, {**task, 'status': min(2, task['status']+1)})}
        await r.table('projects').get(uuid).update(updated).run(conn)
    return redirect(request.referrer)


def flatten_replies(comment: Dict[str, Any]) -> Iterator[Dict[str, Any]]:
    """Recursively walk through the nested replies."""
    yield comment
    for reply in comment['replies']:
        # Don't worry about maximum recursion depth here (-;
        yield from flatten_replies(reply)


@blueprint.route('/reply/<float:parent>', methods=['POST'])
@login_required
async def save_reply(uuid: str, index: int,
                     parent: float) -> ResponseReturnValue:
    """Handle replies in task discussion."""
    tasks = (await pluck_project(uuid, ['tasks']))['tasks']
    tasks.sort(key=itemgetter('created_on'))
    task = tasks[index]
    for reply in flatten_replies(task):
        if reply['created_on'].timestamp() == parent:
            reply['replies'].append(dict(
                content=(await request.form)['comment'],
                creator=current_user.key, created_on=r.now(), replies=[]))
            break
    else:
        raise NotFound

    # FIXME: RethinkDB is by design lock-free so this may overwrite
    # simultaneous updates in another session.  In our use-case,
    # it is unlikely enough to be ignored though.
    async with current_app.db_pool.connection() as conn:
        await r.table('projects').get(uuid).update({'tasks': tasks}).run(conn)
    return redirect(request.referrer)
