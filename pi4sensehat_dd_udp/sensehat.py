from datetime import date, datetime
import random, time, mysql.connector, os
from sense_hat import SenseHat
from datadog import initialize, statsd

ip = os.environ.get("DD_AGENT_HOST")
options = {
    'statsd_host':ip,
    'statsd_port':8125
}

initialize(**options)

sense = SenseHat()

# Create weather class
class Weather:

  def __init__(self, temp_val, humi_val, press_val):
    self.temp_val = temp_val
    self.humi_val = humi_val
    self.press_val = press_val

# Establish Connection to mysql database container
db = mysql.connector.connect(user = 'root', password ='root', host = 'weather_db_dd', port = '3306', database = 'weather_database')
cursor = db.cursor()

# Create the weather_table object
cursor.execute("CREATE TABLE IF NOT EXISTS weather_table (temp int(3), humidity int(3), pressure int(3))")

while True:
    current = datetime.now()
    db = mysql.connector.connect(user = 'root', password ='root', host = 'weather_db_dd', port = '3306', database = 'weather_database')
    cursor = db.cursor()

    # Instantiate my_wether instance from Weather class
    my_weather = Weather(int(sense.get_temperature()),int(sense.get_humidity()),int(sense.get_pressure()))

    # print(current, "\t", my_weather.temp_val, "\t\t", my_weather.humi_val, "\t\t", my_weather.press_val)
    time.sleep(300)

    add_weather = ("INSERT INTO weather_table"
                   "(temp, humidity, pressure) "
                   "VALUES (%(temp)s, %(humidity)s,%(pressure)s)")

    data_weather = {
        'temp': my_weather.temp_val,
        'humidity': my_weather.humi_val,
        'pressure': my_weather.press_val
    }

    # Add data_weather object into weather_table in weather_database
    cursor.execute(add_weather, data_weather)
    weather_id = cursor.lastrowid
    db.commit()

    # Submit Dogstatsd Gauge Metrics
    statsd.gauge('temperature.gauge', my_weather.temp_val,tags=["environment:raspi4"])
    statsd.gauge('humidity.gauge',  my_weather.humi_val, tags=["environment:raspi4"])
    statsd.gauge('pressure.gauge', my_weather.press_val, tags=["environment:raspi4"])
