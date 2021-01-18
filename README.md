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

## Configuration

Acanban's configuration files are looked for
in [user and site config dir][appdirs] (in that order),
with `acanban` namespace.

With third-party configuration separated to dedicated files,
`acanban.toml` may define the following keys:

```toml
# Used for HTTP to HTTPS redirection if defined
domain = 'example.com'
```

### Hypercorn

[Hypercorn configuration][hypercorn.toml] is loaded from `hypercorn.toml`.
Acanban does not override any of the server's defaults.

### RethinkDB

Values defined in `rethinkdb.toml` will be passed to the RethinkDB client.
Below are some of the fields that commonly need to be configured
and their default values:

```toml
host = 'localhost'
port = 28015
user = 'admin'
timeout = 20
db = 'test'
```

### IPFS

Custom `ipfs.toml` must define the following keys,
whose default values are listed as follows:

```toml
[api]
base = 'http://127.0.0.1:5001/api/v0'

[gateway]
base = 'http://127.0.0.1:8080/ipfs'
fallback = 'https://ipfs.io'
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
[appdirs]: https://pypi.org/project/appdirs/
[hypercorn.toml]: https://pgjones.gitlab.io/hypercorn/how_to_guides/configuring.html
