# S01 · mission 3: The heartbeat
# The Airlock Lamp · Pico Bench Quest

from machine import Pin
import time
led = Pin(16, Pin.OUT)
while True: 
    led.toggle()
    time.sleep_ms(500)
