import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

try:
    while True:
        sleep(0.5)
        # if GPIO.input(18) is 1:
        if GPIO.input(18):
            print('Input was HIGH')
        else:
            print('Input was LOW')
except KeyboardInterrupt: # Not Interrupted by Any Keys, Except for Ctrl + C
    pass

GPIO.cleanup()
