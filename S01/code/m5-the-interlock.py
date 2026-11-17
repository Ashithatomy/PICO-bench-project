# S01 · mission 5: The interlock
# The Airlock Lamp · Pico Bench Quest

from machine import Pin
import time
led = Pin(16, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)
while True:
    led.value(not button.value())
    time.sleep_ms(500)
