from time import sleep
import RPi.GPIO as GPIO


BUZZER = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
pwm_buzzer = GPIO.PWM(BUZZER, 100)
pwm_buzzer.start(10)

## Frequencies from 4 Octave 'Do' to 5 Octave 'Do'
FRQ = [261.6, 293.7, 329.6, 349.2, 392.0, 440.0, 493.9, 523.3]

try:
    while True:
        for frq in FRQ:
            pwm_buzzer.ChangeFrequency(frq)
            sleep(0.5)
except KeyboardInterrupt:
    pwm_buzzer.stop()
    GPIO.cleanup()