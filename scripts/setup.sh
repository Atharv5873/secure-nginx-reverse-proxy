#!/bin/bash

set -e

DOMAIN="atharvdevops.ddns.net"
EMAIL="atharv5873@gmail.com"

echo "Updating system..."
apt update && apt upgrade -y

echo "Installing dependencies..."
apt install -y nginx certbot python3-certbot-nginx ufw

echo "Configuring firewall..."
ufw allow 'OpenSSH'
ufw allow 'Nginx Full'
ufw --force enable

echo "Obtaining SSL certificate for $DOMAIN..."
certbot --nginx -d $DOMAIN --non-interactive --agree-tos -m $EMAIL || {
    echo "Certbot failed! Check if your domain is pointing to this server."
    exit 1
}

echo "Reloading Nginx..."
systemctl reload nginx

echo "Setup complete! Visit: https://$DOMAIN"