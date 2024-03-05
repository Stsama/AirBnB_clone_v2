#!/bin/bash
# sets up your web servers for the deployment of web_static
sudo apt update
sudo apt install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

sudo chown -R $USER:$USER /data/web_static/releases/test/
sudo chmod -R 755 /data/web_static/releases/

echo "alx is bae" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current


sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

sudo service nginx restart