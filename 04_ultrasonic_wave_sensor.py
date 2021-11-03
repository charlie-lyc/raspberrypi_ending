import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIG = 18
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
        ## Output for 10 micro seconds
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)
        ## Measure Time
        # while  GPIO.input(ECHO) == 0:
        while not GPIO.input(ECHO):
            start_time = time.time()
        # while  GPIO.input(ECHO) == 1:
        while  GPIO.input(ECHO):
            stop_time = time.time()
        delta_time = stop_time - start_time
        ## Calculate Distance
        distance = (delta_time * 340) / 2
        ## Print Distance
        if distance * 100 < 100:
            print('{} centi-meters'.format(int(distance * 100)))
        else:
            print('{:.2f} meters'.format(distance))
        ## Avoid Overlapped Sensing
        time.sleep(1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()

