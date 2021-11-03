import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)

try:
    while True:
        # if GPIO.input(6) is GPIO.HIGH:
        if GPIO.input(6):
            print('Movement Detected!')
            sleep(5) # Avoid Overlapped Sensing
except KeyboardInterrupt:
    pass

GPIO.cleanup()
