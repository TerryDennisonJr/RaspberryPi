from datetime import date, datetime
import random, time, mysql.connector
from sense_hat import SenseHat

sense = SenseHat()


while True:
    current = datetime.now()   
    db = mysql.connector.connect(user = 'weather_user', password ='weather2023', port = 3306, database='weather_database')
    cursor = db.cursor() 
    
    temp_val = int(sense.get_temperature())
    humi_val = int(sense.get_humidity())
    press_val = int(sense.get_pressure())  
    
    print(current, "\t", temp_val, "\t\t", humi_val, "\t\t", press_val)
    time.sleep(3)


    add_weather = ("INSERT INTO weather_table "
                   "(temp, humidity, pressure) "
                   "VALUES (%(temp)s, %(humidity)s,%(pressure)s)")

    data_weather = {
        'temp': temp_val,
        'humidity': humi_val,
        'pressure': press_val

    }
    cursor.execute(add_weather, data_weather)
    weather_id = cursor.lastrowid

    db.commit()
