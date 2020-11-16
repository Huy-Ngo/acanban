# Group Project Management System

# Deployment

## Requirements

### Python packages

These packages should be installed in a Python virtual environment.

- Quart-Trio
- HyperCorn

### Server requirements

- NGINX
- IPFS
- RethinkDB

## Configuration

### Configure NGINX file

Add following file as `/etc/nginx/sites-available/gpms`

```nginx
server {
	listen 80;
	server_name <IP address or domain name>;
	location / {
		include proxy_params;
		proxy_pass http://unix:/var/www/gpms/gpms.sock;
	}
}
```

Make a symlink to `/etc/nginx/sites-enabled/`

### Configure files for RethinkDB

We use init.d to run RethinkDB on startup.
Configuration file should be put at `/etc/rethinkdb/instances.d/`.
A sample file can be found on [RethinkDB's GitHub repo][1].

More configuration for security can be found on [RethinkDB's Doc][2].
However, at this point the security decision haven't been made

### Configure systemd service

We use systemd to run GPMS.

```ini
[Unit]
Description=Instance to serve GPMS
After=network.target

[Service]
User=username
WorkingDirectory=/home/username/gpms
ExecStart=/home/username/gpms/venv/bin/python -m hypercorn -w 5 -k trio gpms:app

[Install]
WantedBy=multi-user.target
```

Start the service:

```bash
systemctl start gpms.service
```

[1]: https://github.com/rethinkdb/rethinkdb/blob/next/packaging/assets/config/default.conf.sample
[2]: https://rethinkdb.com/docs/security/
