import time
from machine import *
from onewire import DS18X20
from onewire import OneWire
from network import WLAN      # For operation of WiFi network                  # Allows use of time.sleep() for delays
import pycom                  # Base library for Pycom devices
from mqtt import MQTTClient  # For use of MQTT protocol to talk to Adafruit IO
import ubinascii              # Needed to run any MicroPython code
            # Interfaces with hardware components
import micropython
from adafruit import *           # Needed to run any MicroPython code
# DS18B20 data line connected to pin P10
ow1 = OneWire(Pin('P10'))
temp1 = DS18X20(ow1)

ow2 = OneWire(Pin('P7'))
temp2 = DS18X20(ow2)

ow3 = OneWire(Pin('P8'))
temp3 = DS18X20(ow3)





while True:
    print(temp1.read_temp_async())

    print(temp2.read_temp_async())

    print(temp3.read_temp_async())

    time.sleep(1)
    temp1.start_conversion()
    temp2.start_conversion()
    temp3.start_conversion()
    time.sleep(1)

    client.publish(topic=AIO_CONTROL_FEED, msg=str(temp1.read_temp_async()))
    client.publish(topic=AIO_CONTROL_FEED2, msg=str(temp2.read_temp_async()))
    client.publish(topic=AIO_CONTROL_FEED3, msg=str(temp3.read_temp_async()))
    print("DONE")
    time.sleep(5)
