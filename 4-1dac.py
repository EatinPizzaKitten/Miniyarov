import RPi.GPIO as gp
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)

def dec2bin(hex):
    return [int(i) for i in bin(int(hex))[2:].zfill(8)]

try:
    while True:
        n = input()
        if n == 'q':
            break
        number = dec2bin(n)[::-1]
        gp.output(dac, number[::-1])
        bins = [2**(-i-1) for i in range(8)]
        voltage = [number[i]*bins[i] for i in range(8)]
        print('Напряжение: ', 3.3 * sum(voltage))
except ValueError:
    print('Ошибка: Не целое положительное число')
except RuntimeError:
    print('Ошибка: Число больше 255')
finally:
    gp.output(dac, 0)
    gp.cleanup()