#!/bin/bash
sudo apt-get install -y apache2
rm /var/www/html/index.html
service apache2 start