# S01 · mission 4: The door button
# The Airlock Lamp · Pico Bench Quest

from machine import Pin
import time
button = Pin(14,Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        print("pressed")
    else:
        print("released")
    time.sleep_ms(200)
