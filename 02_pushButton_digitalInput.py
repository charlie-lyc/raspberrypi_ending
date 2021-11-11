from time import sleep
import RPi.GPIO as GPIO


BUTTON = 18
GPIO.setmode(GPIO.BCM)

## Pull down resistor out of raspberrypi
GPIO.setup(BUTTON, GPIO.IN)

## Pull down resistor within raspberrypi
# GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # pull up: 'GPIO.PUD_UP'

try:
    while True:
        sleep(0.5)
        # if GPIO.input(18) == 1: # Pushing button
        if GPIO.input(BUTTON):
            print('Input is HIGH')
        else:                     # Not pushing button    
            print('Input is LOW')
except KeyboardInterrupt:         # Stopped by Ctrl + C
    GPIO.cleanup()