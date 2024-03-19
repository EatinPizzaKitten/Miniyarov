import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BCM)
gp.setup(21, gp.IN)
gp.setup(2, gp.OUT)


frequency = 1000
duty = 0
pwm_out = gp.PWM(2, frequency)
pwm_out.start(duty)

try:
    while True:
        duty_user = int(input())
        pwm_out.ChangeDutyCycle(duty_user)
finally:
    gp.output(21, 0)
    gp.cleanup()
