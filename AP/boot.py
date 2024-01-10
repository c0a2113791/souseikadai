import network
import socket
import time
from machine import Pin

p2 = Pin(2,Pin.OUT)
ssid = "cdslT"

ap = network.WLAN(network.AP_IF)
ap.active(True)

ap.config(essid=ssid,txpower=21)
print(ap.ifconfig())

print("AP boot")
time.sleep(10)
p2.on()

execfile("main.py")
