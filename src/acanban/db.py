# RethinkDB wrappers
# Copyright (C) 2020-2021  Nguyễn Gia Phong
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

from typing import Any, Awaitable, Dict, Tuple

from quart import current_app
from rethinkdb import r

__all__ = ['RethinkObject']


async def get(table: str, key: str, field: str) -> Any:
    """Return DB[table][key][field]."""
    async with current_app.db_pool.connection() as conn:
        return await r.table(table).get(key)[field].run(conn)


class RethinkObject:
    """RethinkDB object wrapper mixin.

    Exceptions raised by RethinkDB are expected to be handled by caller.
    """

    slots: Tuple[str, ...]
    table: str
    key: str

    def __getattr__(self, name: str) -> Awaitable:
        if name not in self.slots:
            cls = self.__class__.__name__
            raise AttributeError(f'{cls!r} object has no attribute {name!r}')
        return get(self.table, self.key, name)

    def __setattr__(self, name: str, value: Any) -> None:
        if name in self.slots:
            cls = self.__class__.__name__
            raise AttributeError(
                f'{cls}.update must be used for dynamic attribute {name!r}')
        super().__setattr__(name, value)

    async def pluck(self, *fields: str) -> Dict[str, Any]:
        """Return the plucked fields from the wrapped object."""
        query = r.table(self.table).get(self.key).pluck(*fields)
        async with current_app.db_pool.connection() as conn:
            return await query.run(conn)

    async def update(self, **kwargs: Any) -> None:
        """Update the RethinkDB object from given keys and values.

        This is defined instead of `__setattr__` because
        it is impossible to await an assignment statement.

        Raise
        -----
        ValueError
            If one or more field name in kwargs undeclared in slots.
        """
        invalid = ', '.join(repr(field) for field in kwargs
                            if field not in self.slots)
        if invalid:
            cls = self.__class__.__name__
            raise ValueError(f'cannot dynamically set {invalid} in {cls!r}')
        async with current_app.db_pool.connection() as conn:
            await r.table(self.table).get(self.key).update(kwargs).run(conn)
