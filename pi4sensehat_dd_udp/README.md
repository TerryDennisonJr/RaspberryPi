# Raspberry Pi 4 Docker Sensehat

## Prerequisites:

- mysql (on Host)
  -  `sudo apt-get install mysql-shell`
- docker
- docker-compose

## Deploying:
```
bash script.sh
```

# Notes:

### Deploying Ubuntu and Mysql Container with Docker Compose:
```
sudo docker-compose up -d
sudo docker-compose kill

```

### Mysql Container Commands:
```
mysql -uroot -proot
```


### Mysql Commands:
```
SHOW DATABASES:
use weather_database;
show tables;
select * from weather_table;
```
