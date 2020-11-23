# Test configuration parsing
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

from os.path import abspath, dirname, join
from typing import Any, Mapping, Sequence

import toml
from pytest import mark, param

from acanban.config import hypercorn_config

CONFIG_DIR = abspath(join(dirname(__file__), 'assets'))
EMPTY_DIR = 'this directory does not exist'

HYPERCORN_MOCK = toml.load(join(CONFIG_DIR, 'hypercorn.toml'))
HYPERCORN_DEFAULT = {'bind': ['127.0.0.1:8000']}


@mark.parametrize(('dirs', 'mapping'), (
    param([CONFIG_DIR], HYPERCORN_MOCK, id='load'),
    param([EMPTY_DIR, CONFIG_DIR], HYPERCORN_MOCK, id='load'),
    param([EMPTY_DIR], HYPERCORN_DEFAULT, id='fallback')))
def test_hypercorn_config(dirs: Sequence[str],
                          mapping: Mapping[str, Any]) -> None:
    """Test loading Hypercorn configuration."""
    config = hypercorn_config(*dirs)
    for key, value in mapping.items(): assert getattr(config, key) == value
