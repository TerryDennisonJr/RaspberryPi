#!/bin/bash

user=root
database=weather_database
table=weather_table 
sandbox_OS=$(uname)


echo "Provisioning!"
echo ""

echo "apt-get updating"
sudo apt-get update -y
sudo apt-get upgrade -y

echo "Installing dd-agent"
DD_API_KEY=<API_KEY> DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script_agent7.sh)"

echo "Adding Agent Configs to dd-agent"
echo ""

sudo sed -i.yaml "s/# hostname: <HOSTNAME_NAME>/hostname: $HOSTNAME/1" /etc/datadog-agent/datadog.yaml
sudo sed -i.yaml "s/# env: <environment name>/env: $(uname)/1" /etc/datadog-agent/datadog.yaml
sudo sed -i.yaml "s/# use_dogstatsd: true/use_dogstatsd: true/1" /etc/datadog-agent/datadog.yaml
sudo sed -i.yaml "s/# dogstatsd_port: 8125/dogstatsd_port: 8125/1" /etc/datadog-agent/datadog.yaml

sudo cp -R "/etc/datadog-agent/conf.d/mysql.d/conf.yaml.example" "/etc/datadog-agent/conf.d/mysql.d/conf.yaml"

sudo sed -i.yaml "s/    password: <PASSWORD>/    password: Datadog2023/1" /etc/datadog-agent/conf.d/mysql.d/conf.yaml
sudo sed -i.yaml "s/    # dbm: false:/    dbm: true/1" /etc/datadog-agent/conf.d/mysql.d/conf.yaml

sudo /etc/init.d/datadog-agent stop
sudo /etc/init.d/datadog-agent start

echo "Installing pip and Python datadog module"
echo ""

sleep 3

sudo -h $HOSTNAME pip3 install datadog
sudo -u root pip3 install datadog
  
echo "Mysql install"
echo ""

sleep 3
sudo mysql --user=$user --execute="CREATE USER datadog@'%' IDENTIFIED WITH mysql_native_password by 'Datadog2023'; ALTER USER datadog@'%' WITH MAX_USER_CONNECTIONS 5; GRANT REPLICATION CLIENT ON *.* TO datadog@'%';GRANT PROCESS ON *.* TO datadog@'%';"
sudo mysql --user=$user --execute="GRANT SELECT ON performance_schema.* TO datadog@'%'; CREATE SCHEMA IF NOT EXISTS datadog;"
sudo mysql --user=$user --execute="GRANT EXECUTE ON datadog.* to datadog@'%'; GRANT CREATE TEMPORARY TABLES ON datadog.* TO datadog@'%';"

sudo mysql --user=$user --execute="DELIMITER $$
CREATE PROCEDURE datadog.explain_statement(IN query TEXT)
    SQL SECURITY DEFINER
BEGIN
    SET @explain := CONCAT('EXPLAIN FORMAT=json ', query);
    PREPARE stmt FROM @explain;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ; "


sudo mysql --user=$user --execute="DELIMITER $$
CREATE PROCEDURE datadog.enable_events_statements_consumers()
    SQL SECURITY DEFINER
BEGIN
    UPDATE performance_schema.setup_consumers SET enabled='YES' WHERE name LIKE 'events_statements_%';
    UPDATE performance_schema.setup_consumers SET enabled='YES' WHERE name = 'events_waits_current';
END $$
DELIMITER ;"


sudo mysql --user=$user --execute="GRANT EXECUTE ON PROCEDURE datadog.enable_events_statements_consumers TO datadog@'%';"
  
sleep 3

sudo systemctl stop datadog-agent && sudo systemctl start datadog-agent
echo ""
echo "Waiting/Restarting Agent for myql to enable '"performance-schema-consumer-events-waits-current"' for metrics... "
sleep 10
sudo systemctl stop datadog-agent && sudo systemctl start datadog-agent
echo ""
echo "Dogstatsd/Mysql Completed!"
