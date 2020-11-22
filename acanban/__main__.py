# Server console script
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
from argparse import ArgumentParser

from hypercorn.config import Config
from hypercorn.trio import serve
from trio import run

from . import app

if __name__ == '__main__':
    parser = ArgumentParser(prog='acanban')
    parser.add_argument('--bind', default='localhost:80')
    args = parser.parse_args()
    config = Config()
    config.bind = [f'{args.bind}')]
    run(serve, app, config)
