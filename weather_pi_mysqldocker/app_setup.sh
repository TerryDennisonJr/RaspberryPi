#!/bin/bash

sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt install docker.io -y
sudo apt-get install mariadb-client -y
sudo apt install docker-compose -y


# pwd needs to be in the path where .yaml file is located
#sudo docker-compose up
#sudo docker-compose run app




