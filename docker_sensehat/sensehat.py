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

with open("/data/myfile.csv", "a") as f:
    write = csv.writer(f)
    write.writerow(fields)
    while True:
        current = datetime.now()

        my_weather = Weather(int(sense.get_temperature()),int(sense.get_humidity()),int(sense.get_pressure()))

        print("\t", my_weather.temp_val, "\t\t", my_weather.humi_val, "\t\t", my_weather.press_val)
        rows = [[current,str(my_weather.temp_val), str(my_weather.humi_val), str(my_weather.press_val)]]

        write.writerows(rows)
        time.sleep(3)
