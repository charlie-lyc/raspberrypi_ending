from time import sleep
import RPi.GPIO as GPIO


MOTOR = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR, GPIO.OUT)
pwm_motor = GPIO.PWM(MOTOR, 50)
pwm_motor.start(0)

try:
    while True:
        pwm_motor.ChangeDutyCycle(7.5)  # "7.5": angular change 0 -> "90"   (counterclockwise)
        sleep(1)
        pwm_motor.ChangeDutyCycle(12.5) # "12.5": angular change 90 -> "180" (counterclockwise)
        sleep(1)
        pwm_motor.ChangeDutyCycle(2.5)  # "2.5": angular change: 180 -> "0"  (clockwise)
        sleep(1)
except KeyboardInterrupt:
    pwm_motor.stop()
    GPIO.cleanup()