# Configuration parser
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

from os.path import isfile, join

from hypercorn.config import Config


def hypercorn_config(*directories: str) -> Config:
    """Return Hypercorn configuration first found in given directories."""
    for directory in directories:
        file = join(directory, 'hypercorn.toml')
        if isfile(file): return Config.from_toml(file)
    return Config()
