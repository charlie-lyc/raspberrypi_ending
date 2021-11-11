import time
import RPi.GPIO as GPIO


TRIG = 18
ECHO = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
        ## Output for 10 micro seconds
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)
        ## Measure time
        # while GPIO.input(ECHO) == 0:
        while not GPIO.input(ECHO):
            start_time = time.time()
        # while GPIO.input(ECHO) == 1:
        while GPIO.input(ECHO):
            stop_time = time.time()
        delta_time = stop_time - start_time
        ## Calculate distance
        distance = (delta_time * 340) / 2
        ## Print distance
        if distance * 100 < 100:
            print('{} centi-meters'.format(int(distance * 100)))
        else:
            print('{:.2f} meters'.format(distance))
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()