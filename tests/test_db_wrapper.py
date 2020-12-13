# Test RethinkDB wrapper
# Copyright (C) 2020  Ngô Ngọc Đức Huy
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

from crypt import crypt
from hmac import compare_digest

from pytest import raises

from acanban import Acanban
from acanban.auth import User


async def test_object_get(app: Acanban) -> None:
    """Test object get attributes."""
    async with app.app_context():
        user = User('silasl')
        digest = await user.password
        assert compare_digest(digest, crypt('lsalis', digest))
        assert await user.email == 'silasl@example.edu'
        assert await user.name == 'Silas Lehtonen'
        assert await user.role == 'assistant'
        with raises(AttributeError): await user.kink


async def test_object_set(app: Acanban) -> None:
    """Test object set attributes."""
    async with app.app_context():
        user, monty = User('silasl'), 'Monty Python'
        name = await user.name
        with raises(AttributeError): user.name = monty

        await user.update(name=monty)
        assert await user.name == monty
        await user.update(name=name)

        with raises(ValueError): await user.update(kink='DBMS')
