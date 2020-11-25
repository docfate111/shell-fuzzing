#!/bin/sh
echo 'Run script as root'
ls ../../shells/bin > installed_shells
mkdir -p /usr/local/bin/smoosh
chmod 777 /usr/local/bin/smoosh
cp -a ../../shells/bin/. /usr/local/bin/smoosh
chmod +x /usr/local/bin/smoosh/* 
