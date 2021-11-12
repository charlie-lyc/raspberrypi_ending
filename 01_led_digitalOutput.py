from time import sleep

## Install package (or library)
# $ sudo apt install python3-dev
# $ sudo apt install python3-rpi.gpio

## Use module
import RPi.GPIO as GPIO


LED = 17
GPIO.setmode(GPIO.BCM)    # Set mode: 'GPIO.BCM' or 'GPIO.BOARD'
GPIO.setup(LED, GPIO.OUT) # Set pin: 'GPIO.OUT' or 'GPIO.IN'

for _ in range(5):        # Blink 5 times
    GPIO.output(LED, GPIO.HIGH)
    print('LED ON')
    sleep(1)              # Delay 1 second
    GPIO.output(LED, GPIO.LOW)
    print('LED OFF')
    sleep(1)

GPIO.cleanup()            # Clear all resource on GPIO

## Run
# python 01_led_digitalOutput.py