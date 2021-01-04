# Test configuration parsing
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

from os.path import abspath, dirname, join
from typing import Any, Mapping, Sequence

import toml
from pytest import mark, param

from acanban.config import (ACANBAN_DEFAULT, IPFS_DEFAULT, RETHINKDB_DEFAULT,
                            acanban_config, hypercorn_config, ipfs_config,
                            rethinkdb_config)

CONFIG_DIR = abspath(join(dirname(__file__), 'assets'))
EMPTY_DIR = 'this directory does not exist'

ACANBAN_MOCK = toml.load(join(CONFIG_DIR, 'acanban.toml'))
HYPERCORN_MOCK = toml.load(join(CONFIG_DIR, 'hypercorn.toml'))
HYPERCORN_DEFAULT = {'bind': ['127.0.0.1:8000']}
IPFS_MOCK = toml.load(join(CONFIG_DIR, 'ipfs.toml'))
RETHINKDB_MOCK = toml.load(join(CONFIG_DIR, 'rethinkdb.toml'))


@mark.parametrize(('dirs', 'mapping'), (
    param([CONFIG_DIR], ACANBAN_MOCK, id='load'),
    param([EMPTY_DIR, CONFIG_DIR], ACANBAN_MOCK, id='find'),
    param([EMPTY_DIR], ACANBAN_DEFAULT, id='fallback')))
def test_acanban_config(dirs: Sequence[str],
                        mapping: Mapping[str, Any]) -> None:
    """Test loading Acanban configuration."""
    assert acanban_config(dirs) == mapping


@mark.parametrize(('dirs', 'mapping'), (
    param([CONFIG_DIR], HYPERCORN_MOCK, id='load'),
    param([EMPTY_DIR, CONFIG_DIR], HYPERCORN_MOCK, id='find'),
    param([EMPTY_DIR], HYPERCORN_DEFAULT, id='fallback')))
def test_hypercorn_config(dirs: Sequence[str],
                          mapping: Mapping[str, Any]) -> None:
    """Test loading Hypercorn configuration."""
    config = hypercorn_config(dirs)
    for key, value in mapping.items(): assert getattr(config, key) == value


@mark.parametrize(('dirs', 'mapping'), (
    param([CONFIG_DIR], IPFS_MOCK, id='load'),
    param([EMPTY_DIR, CONFIG_DIR], IPFS_MOCK, id='find'),
    param([EMPTY_DIR], IPFS_DEFAULT, id='fallback')))
def test_ipfs_config(dirs: Sequence[str], mapping: Mapping[str, Any]) -> None:
    """Test loading IPFS configuration."""
    assert ipfs_config(dirs) == mapping


@mark.parametrize(('dirs', 'mapping'), (
    param([CONFIG_DIR], RETHINKDB_MOCK, id='load'),
    param([EMPTY_DIR, CONFIG_DIR], RETHINKDB_MOCK, id='find'),
    param([EMPTY_DIR], RETHINKDB_DEFAULT, id='fallback')))
def test_rethinkdb_config(dirs: Sequence[str],
                          mapping: Mapping[str, Any]) -> None:
    """Test loading RethinkDB configuration."""
    assert rethinkdb_config(dirs) == mapping
