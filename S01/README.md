# S01: The Airlock Lamp

Cleanroom gowning room: a lamp shows the airlock state and a button asks to enter. Every cleanroom you have worked in has one.

Built on a Raspberry Pi Pico 2 with MicroPython, with a custom PCB designed in KiCad 9.

## What it does

- **Light the airlock lamp**: Before any code: make the lamp glow straight from the power rail.
- **Control the lamp from code**: The airlock controller decides when the lamp is on.
- **The heartbeat**: A slow blink tells the operator "the controller is alive".
- **The door button**: Read the request-to-enter button.
- **The interlock**: The lamp lights only while someone holds the request button.
- **The toggle latch**: Press once: lamp on. Press again: off. Like the cleanroom light switch.
- **Boss: the airlock sequence**: No hints. Show what you can build alone.

## Skills

- LED polarity: long leg to +
- Why an LED needs a series resistor (Ohm's law)
- Breadboard columns and rails
- The Pico's 3V3 and GND pins
- from machine import Pin
- Output pins: Pin(n, Pin.OUT)
- value(1) and value(0)
- Using the Shell to test one line
- while True: loops and indentation
- import time and time.sleep_ms()
- Frequency from on and off times
- toggle() to write less code
- Input pins and Pin.PULL_UP
- Active-low: pressed reads 0
- print() to see what the Pico sees
- if / else and ==
- Writing a loop from a goal
- Combining inputs and outputs
- not to invert a value
- Falling-edge detection
- Keeping state in a variable (last)
- Debouncing with a short wait
- and in conditions
- Building a program from a plain-English spec
- Mixing input checks with timing
- Creating a KiCad project in your repo
- Placing symbols, power symbols and wires
- Net labels and no-connect flags
- Running ERC and fixing power warnings

## Code

The final program is `main.py`; each mission's version is in `code/`.

## PCB

- Schematic: symbols and wires

Add your KiCad project, Gerber zip and screenshots to `kicad/` and `fab/`.

## Photos

Add your breadboard photo and board screenshots here.
