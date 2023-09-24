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
echo "install curl if not there..."
sudo apt-get install -y curl


echo "Installing pip and modules/tools"
echo ""

sleep 3

sudo apt-get install python3.7 -y
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
sudo -H apt-get install python3-pip -y
python3 -m pip install --upgrade pip
sudo apt-get install sense-hat -y

  
echo "Mysql install"
echo ""

sleep 3
sudo apt-get install mariadb-server mariadb-client -y
sudo pip3 install mysql-connector-python
sudo mysql --user=$user --execute="CREATE DATABASE $database; USE $database; CREATE TABLE $table (temp INT(3), humidity INT(3), pressure INT(4)); "
sudo mysql --user=$user --execute="CREATE USER 'weather_user'@'localhost' IDENTIFIED BY 'weather2023'; GRANT ALL ON *.* TO 'weather_user'@'localhost'; FLUSH PRIVILEGES;"
  
echo "Retrieving Python file"
echo ""

sleep 3

echo ""
echo "Mysql Components Installed!"
