## Deploying Ubuntu and Mysql Container with Docker Compose:
```
sudo docker exec -it weather_sense bash
sudo docker-compose stop app
bash script.sh
```

## Mysql Container Commands:
```
sudo docker exec -it weather_db bash
mysql -uroot -proot
```


## Mysql Commands:
```
SHOW DATABASES:
use weather_database;
show tables;
select * from weather_table;
```
