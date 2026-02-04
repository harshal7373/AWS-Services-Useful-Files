#!/bin/bash
set -e

echo "=== Starting Deployment ==="

# Update and install Apache
apt-get update -y
apt-get install -y apache2

# Disable directory listing (THIS IS CRITICAL)
sed -i 's/Options Indexes FollowSymLinks/Options -Indexes FollowSymLinks/g' /etc/apache2/apache2.conf

# Start and enable Apache
systemctl start apache2
systemctl enable apache2

echo "=== Deployment Complete ==="
