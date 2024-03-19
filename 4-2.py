import RPi.GPIO as gp
from time import sleep

dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)

def dec2bin(hex):
    return [int(i) for i in bin(int(hex))[2:].zfill(8)]


period = float(input())
try:
    while True:
        for i in range(256):
            gp.output(dac, dec2bin(i))
            sleep(period/512)
        for i in range(255, -1, -1):
            gp.output(dac, dec2bin(i))
            sleep(period/512)
finally:
    gp.output(dac, 0)
    gp.cleanup()