#/bin/bash

sudo docker-compose build && sudo docker-compose up -d
while ! sudo docker exec weather_db mysqladmin --user=root --password=root --host 127.0.0.1 ping --silent &> /dev/null ; do     echo Waiting for database connection...;      sleep 2; done
sudo docker-compose run app
