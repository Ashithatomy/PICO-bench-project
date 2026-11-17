# S01 · mission 6: The toggle latch
# The Airlock Lamp · Pico Bench Quest

from machine import Pin
import time
led = Pin(16, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)
last = 1

while True:
    now = button.value()
    if last == 1 and now == 0:
        led.toggle()
    last = now
    time.sleep_ms(20)
