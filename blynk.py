import BlynkLib
import Adafruit_DHT
import serial
import os
import sys

BLYNK_AUTH = '3e37ac6b948b41e5b3ff847e7947037e'


# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)


humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
@blynk.VIRTUAL_READ(2)
def v2_read_handler():
 blynk.virtual_write(2, humidity)






@blynk.VIRTUAL_READ(4)


def v4_read_handler():
 ser = serial.Serial('/dev/ttyACM0',9600)
 read_serial=ser.readline()
 blynk.virtual_write(4, read_serial)



# Register virtual pin handler

# Start Blynk (this call should never return)
blynk.run()
