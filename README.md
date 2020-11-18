# Acanban

Acanban is an academic [Kanban board].  It aims to provide
a collaboration platform for students and mentors, with first-class support
for academic evaluation.

## Prerequisites

Acanban runs on Python 3.7+ and requires [RethinkDB] and [IPFS] 0.7 or above.

## Setup

The development version of Acanban can be installed from this git repository:

```bash
python -m pip install git+https://github.com/Huy-Ngo/acanban
```

Acanban can then be evoked via `python -m acanban`.  In production,
it is typical to run it as a systemd service, configured like followed.

```ini
[Unit]
Description=The Acanban Server
After=network.target

[Service]
ExecStart=/path/to/venv/bin/python -m acanban
Restart=on-failure

[Install]
WantedBy=default.target
```

## Hacking

First clone the repository and install Acanban as editable:

```bash
git clone https://github.com/Huy-Ngo/acanban
cd acanban
python -m pip install flit
flit install --symlink
```

After playing around with the source code, one can use `tox`
to test the modified version:

```bash
python -m pip install tox
tox
```

[Kanban board]: https://en.wikipedia.org/wiki/Kanban_board
[RethinkDB]: https://rethinkdb.com/docs/install/
[IPFS]: https://ipfs.io
