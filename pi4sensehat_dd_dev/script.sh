#/bin/bash

sudo docker-compose build && sudo docker-compose up -d
while ! sudo docker exec weather_db_dd mysqladmin --user=root --password=root --host 127.0.0.1 ping --silent &> /dev/null ; do     echo Waiting for database connection...;      sleep 2; done

sudo docker exec weather_db_dd mysql --user=root --password=root --execute="CREATE USER 'datadog'@'%' IDENTIFIED BY 'dd_2024';"
sudo docker exec weather_db_dd mysql --user=root --password=root --execute="GRANT REPLICATION CLIENT ON *.* TO 'datadog'@'%'"
sudo docker exec weather_db_dd mysql --user=root --password=root --execute="ALTER USER 'datadog'@'%' WITH MAX_USER_CONNECTIONS 5;"
sudo docker exec weather_db_dd mysql --user=root --password=root --execute="GRANT PROCESS ON *.* TO 'datadog'@'%';"
sudo docker exec weather_db_dd mysql --user=root --password=root --execute="GRANT SELECT ON performance_schema.* TO 'datadog'@'%';"

sudo docker-compose run app

