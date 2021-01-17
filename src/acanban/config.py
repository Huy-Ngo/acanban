# Configuration parser
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

from os.path import isfile, join
from typing import Any, MutableMapping, Sequence

import toml
from appdirs import site_config_dir, user_config_dir
from hypercorn.config import Config as HyperConf

TomMapping = MutableMapping[str, Any]

CONFIG_DIRS = user_config_dir('acanban'), site_config_dir('acanban')
ACANBAN_DEFAULT: TomMapping = {}
IPFS_DEFAULT: TomMapping = {
    'api': {'base': 'http://127.0.0.1:5001/api/v0'},
    'gateway': {'base': 'http://127.0.0.1:8080/ipfs',
                'fallback': 'https://ipfs.io'}}
RETHINKDB_DEFAULT: TomMapping = {'db': 'test'}


def acanban_config(dirs: Sequence[str] = CONFIG_DIRS) -> TomMapping:
    """Return Acanban configuration first found in given directories."""
    for directory in dirs:
        file = join(directory, 'acanban.toml')
        if isfile(file): return toml.load(file)
    return ACANBAN_DEFAULT


def ipfs_config(dirs: Sequence[str] = CONFIG_DIRS) -> TomMapping:
    """Return IPFS configuration first found in given directories."""
    for directory in dirs:
        file = join(directory, 'ipfs.toml')
        if isfile(file): return toml.load(file)
    return IPFS_DEFAULT


def hypercorn_config(dirs: Sequence[str] = CONFIG_DIRS) -> HyperConf:
    """Return Hypercorn configuration first found in given directories."""
    for directory in dirs:
        file = join(directory, 'hypercorn.toml')
        if isfile(file): return HyperConf.from_toml(file)
    return HyperConf()


def rethinkdb_config(dirs: Sequence[str] = CONFIG_DIRS) -> TomMapping:
    """Return RethinkDB configuration first found in given directories."""
    for directory in dirs:
        file = join(directory, 'rethinkdb.toml')
        if isfile(file): return toml.load(file)
    return RETHINKDB_DEFAULT
