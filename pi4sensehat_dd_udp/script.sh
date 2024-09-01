#/bin/bash

echo "Starting Pi4 Sensehat Build..."
sudo docker-compose up -d

echo "Run mysql commands for dd-agent"
sudo docker exec weather_db_dd mysql --user=root --password=root --execute="CREATE USER 'datadog'@'%' IDENTIFIED BY 'dd_2024';"
sudo docker exec weather_db_dd mysql --user=root --password=root --execute="GRANT REPLICATION CLIENT ON *.* TO 'datadog'@'%'"
sudo docker exec weather_db_dd mysql --user=root --password=root --execute="ALTER USER 'datadog'@'%' WITH MAX_USER_CONNECTIONS 5;"
sudo docker exec weather_db_dd mysql --user=root --password=root --execute="GRANT PROCESS ON *.* TO 'datadog'@'%';"
sudo docker exec weather_db_dd mysql --user=root --password=root --execute="GRANT SELECT ON performance_schema.* TO 'datadog'@'%';"

echo "Done!"

