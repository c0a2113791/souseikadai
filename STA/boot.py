import os
import network
import machine
from machine import Pin, SoftI2C
import utime
import webrepl

p2 = Pin(2, Pin.OUT)

ap_ssid = "cdslT"

print('boot is ok')

execfile("exa.py")
