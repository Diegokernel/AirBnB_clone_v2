#!/usr/bin/env bash
# sets up your web servers for the deployment

sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/releases/test/
echo "test" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu:ubuntu -R /data/
sudo sed -i '52i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default
sudo service nginx restart
