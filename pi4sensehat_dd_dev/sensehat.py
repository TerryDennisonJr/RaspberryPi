from datetime import date, datetime
import random, time, mysql.connector
from sense_hat import SenseHat

sense = SenseHat()

class Weather:

  def __init__(self, temp_val, humi_val, press_val):
    self.temp_val = temp_val
    self.humi_val = humi_val
    self.press_val = press_val

#TABLES={}
#TABLES['weather_table'] = (
#  "CREATE TABLE 'weather_table' ("
#  " 'temp' int(3) NOT NULL,"
#  " 'humidity' int(3) NOT NULL,"
#  " 'pressure' int(3) NOT NULL,")

db = mysql.connector.connect(user = 'root', password ='root', host = 'weather_db_dd', port = '3306', database = 'weather_database')
cursor = db.cursor()
    
cursor.execute("CREATE TABLE IF NOT EXISTS weather_table (temp int(3), humidity int(3), pressure int(3))")
while True:
    current = datetime.now()
    db = mysql.connector.connect(user = 'root', password ='root', host = 'weather_db_dd', port = '3306', database = 'weather_database')
    cursor = db.cursor()
    
#    cursor.execute("CREATE TABLE weather_table (temp int(3), humidity int(3), pressure int(3))")
    my_weather = Weather(int(sense.get_temperature()),int(sense.get_humidity()),int(sense.get_pressure()))

    print(current, "\t", my_weather.temp_val, "\t\t", my_weather.humi_val, "\t\t", my_weather.press_val)
    time.sleep(3)



    add_weather = ("INSERT INTO weather_table"
                   "(temp, humidity, pressure) "
                   "VALUES (%(temp)s, %(humidity)s,%(pressure)s)")

    data_weather = {
        'temp': my_weather.temp_val,
        'humidity': my_weather.humi_val,
        'pressure': my_weather.press_val

    }
    cursor.execute(add_weather, data_weather)
    weather_id = cursor.lastrowid

    db.commit()
