import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

for _ in range(1, 6): # Blink 5 times
    GPIO.output(17, GPIO.HIGH)
    print('LED ON')
    sleep(1) # Delay 1 second
    GPIO.output(17, GPIO.LOW)
    print('LED OFF')
    sleep(1)

GPIO.cleanup()
