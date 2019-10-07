from machine import Pin
import time

led=Pin(2,Pin.OUT)

while True:
  time.sleep(1)
  le.value(not led.value())
