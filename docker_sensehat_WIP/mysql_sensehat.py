from datetime import date, datetime
from datetime import date
import random
import time
import mysql.connector

from sense_hat import SenseHat

sense = SenseHat()
class Weather:

  def __init__(self, temp_val, humi_val, press_val):
    self.temp_val = temp_val
    self.humi_val = humi_val
    self.press_val = press_val

db2 = mysql.connector.connect(host = 'weather_db', user = 'root', password ='root', port = 3306, database='weather_database')
cursor2 = db2.cursor()
cursor2.execute("CREATE TABLE IF NOT EXISTS weather_table (date DATE, temp INT(3),humidity INT(3), pressure INT(3))")
db2.commit
cursor2.close()
db2.close()

while True:

     current = datetime.now()

     my_weather = Weather(int(sense.get_temperature()),int(sense.get_humidity()),int(sense.get_pressure()))

     print("\t", my_weather.temp_val, "\t\t", my_weather.humi_val, "\t\t", my_weather.press_val)

     time.sleep(3)

    db3 = mysql.connector.connect(host = 'weather_db', user = 'root', password ='root', port = 3306, database='weather_database')
    cursor3 = db3.cursor()

    print(current, "\t", temp_val, "\t\t", humi_val, "\t\t", press_val)


    add_weather = ("INSERT INTO weather_table "
                   "(date, temp, humidity, pressure) "
                   "VALUES ( %(date)s, %(temp)s, %(humidity)s,%(pressure)s)")

    data_weather = {
        'date': current,
        'temp': my_weather.temp_val,
        'humidity': my_weather.humi_val,
        'pressure': my_weather.press_val

    }
    cursor3.execute(add_weather, data_weather)
    weather_id = cursor2.lastrowid

    db3.commit()
    time.sleep(3)
