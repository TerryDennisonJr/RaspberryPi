#!/bin/bash

sudo mkdir update_logs
sudo cd update_logs
sudo touch {update_dkpg.log,update_logs.log,update_script.sh}
sudo chmod 777 /home/td_pi4/update_logs
cd ~/td_pi4
git clone https://github.com/TerryDennisonJr/github_RaspberryPi.git
sudo curl -fsSL https://get.docker.com -o get-docker.sh

#sh get-docker.sh
#crontab -e
#sudo echo "0 5 * * 1  /bin/bash ~/update_logs/update_script.sh" >> /etc/crontab 
