from machine import Pin
import time
led = Pin(16, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)
while True:
    if button.value() == 0:
        led.toggle()
    else:
        led.value(1)
    time.sleep_ms(250)
