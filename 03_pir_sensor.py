from time import sleep
import RPi.GPIO as GPIO


PIR = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)

try:
    while True:
        # if GPIO.input(PIR) is GPIO.HIGH:
        # if GPIO.input(PIR) == 1:
        if GPIO.input(PIR):
            print('Motion Detected!')
            sleep(3) # Avoid overlapped sensing
except KeyboardInterrupt:
    GPIO.cleanup()