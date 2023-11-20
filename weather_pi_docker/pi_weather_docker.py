from datetime import date, datetime
from datetime import date
import random
import time
import mysql.connector



current = datetime.now().date()
print("Date", "\t\tTemperatue", "\tHumidity", "\tPressure")


db2 = mysql.connector.connect(host = 'weather_db', user = 'root', password ='root', port = 3306, database='weather_database')    
cursor2 = db2.cursor()
cursor2.execute("CREATE TABLE IF NOT EXISTS weather_table (date DATE, temp INT(3),humidity INT(3), pressure INT(3))")
db2.commit
cursor2.close()
db2.close()

while True:
   
    db3 = mysql.connector.connect(host = 'weather_db', user = 'root', password ='root', port = 3306, database='weather_database')
    cursor3 = db3.cursor() 

    #cursor = db.cursor()
    #temp_val = int(sense.get_temperature())
    #humi_val = int(sense.get_humidity())
    #press_val = int(sense.get_pressure())
     
    temp_val = random.randrange(15, 55)
    humi_val = random.randrange(30, 40)
    press_val = random.randrange(850, 1050)    
    
    print(current, "\t", temp_val, "\t\t", humi_val, "\t\t", press_val)


    add_weather = ("INSERT INTO weather_table "
                   "(date, temp, humidity, pressure) "
                   "VALUES ( %(date)s, %(temp)s, %(humidity)s,%(pressure)s)")

    data_weather = {
        'date': current,
        'temp': temp_val,
        'humidity': humi_val,
        'pressure': press_val

    }
    cursor3.execute(add_weather, data_weather)
    weather_id = cursor2.lastrowid

    db3.commit()
    time.sleep(3)
