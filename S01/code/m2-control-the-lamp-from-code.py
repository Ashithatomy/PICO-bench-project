# S01 · mission 2: Control the lamp from code
# The Airlock Lamp · Pico Bench Quest

from machine import Pin
led = Pin(16, Pin.OUT)
led.value(0)
