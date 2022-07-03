import network      # For operation of WiFi network
#import esp32
import time                   # Allows use of time.sleep() for delays
from mqtt import MQTTClient  # For use of MQTT protocol to talk to Adafruit IO
#from wifiConnect import *
import ubinascii              # Needed to run any MicroPython code
import sys
from machine import Pin, Timer               # Interfaces with hardware components
import micropython            # Needed to run any MicroPython code


# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "xlordofpainx"
AIO_KEY = "aio_uklA80uUvC4m6nMP7WpSxsn6Ne0W"
AIO_CLIENT_ID = bytes('client_'+'12321','utf-8') #random
AIO_CONTROL_FEED = "xlordofpainx/feeds/battery-temperature"
AIO_CONTROL_FEED2 = "xlordofpainx/feeds/temp2"
AIO_CONTROL_FEED3 = "xlordofpainx/feeds/temp3"
# esp32.hall_sensor()     # read the internal hall sensor
#connect()
# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)
# Subscribed messages will be delivered to this callback
try:
    client.connect()
    print("Connected to %s, subscribed to %s topic" % (AIO_SERVER, AIO_CONTROL_FEED))

except Exception as e:
    print("count not connect to MQTT server{}{}".format(type(e)._name_,e))
    sys.exit()
