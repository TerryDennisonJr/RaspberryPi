from datetime import date, datetime
import random, time, csv
from sense_hat import SenseHat

sense = SenseHat()
fields = ['Timestamp', 'Temperature', 'Pressure', 'Humidity']
class Weather:

  def __init__(self, temp_val, humi_val, press_val):
    self.temp_val = temp_val
    self.humi_val = humi_val
    self.press_val = press_val

    current = datetime.now()

    my_weather = Weather(int(sense.get_temperature()),int(sense.get_humidity()),int(sense.get_pressure()))

    print("\t", my_weather.temp_val, "\t\t", my_weather.humi_val, "\t\t", my_weather.press_val)

    time.sleep(3)
