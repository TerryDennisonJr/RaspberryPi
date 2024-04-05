import os
import time

def get_temp():
        f = open("/home/td_pi4/Weather_pi/data/temp.txt","r")
        temp_data = f.readline()
        return (temp_data)
        f.close()

def get_humi():
        f = open("/home/td_pi4/Weather_pi/data/humidity.txt","r")
        humi_data = f.readline()
        return (humi_data)
        f.close()

def get_press():
        f = open("/home/td_pi4/Weather_pi/data/pressure.txt","r")
        press_data = f.readline()
        return (press_data)
        f.close()
try:
    # first, try to import the base class from new versions of the Agent...
    from datadog_checks.base import AgentCheck
except ImportError:
    # ...if the above failed, the check is running in Agent version < 6.6.0
    from checks import AgentCheck

# content of the special variable __version__ will be shown in the Agent status page
__version__ = "1.0.0"

class SystemTemperature(AgentCheck):
    def check(self, instance):
        self.gauge('temp.celsius.raspi', get_temp())
        self.gauge('temp.fahrenheit.raspi', float(get_temp()) * (9/5) + 32)
        self.gauge('humidity.raspi', get_humi())
        self.gauge('pressure.raspi', get_press())