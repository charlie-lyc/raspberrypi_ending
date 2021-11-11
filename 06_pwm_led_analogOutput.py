from time import sleep
import RPi.GPIO as GPIO


LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

### GPIO.PWM(param1, param2)
## Param1: pin
## Param2: frequency(Hz)
pwm_led = GPIO.PWM(LED, 50)

### Duty cycle(0 ~ 100) start
pwm_led.start(0)
for _ in range(5):               # Softly blink 5 times
    for i in range(101):         # Duty cycle change: 0 -> 100
        pwm_led.ChangeDutyCycle(i)
        sleep(0.02)
    for j in range(100, -1, -1): # Duty cycle change: 100 -> 0
        pwm_led.ChangeDutyCycle(j)
        sleep(0.02)

GPIO.cleanup() 