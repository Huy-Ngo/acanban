# Group Project Management System

# Deployment

## Requirements

### Python packages

These packages are 

- Flask
- Gunicorn

### Server requirements

- IPFS
- NGINX

## Steps

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

### Configure systemd service

```toml
[Unit]
Description=Instance to serve GPMS
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/gpms
Environment="PATH=/var/www/gpms/venv/bin"
ExecStart=/var/www/gpms/venv/bin/gunicorn --workers <number of workers> --bind unix:gpms.sock wsgi:app

[Install]
WantedBy=multi-user.target
```

Start the service:

```bash
systemctl start gpms.service
```
