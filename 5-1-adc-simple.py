import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup (dac, GPIO.OUT)
GPIO.setup (troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)

def decimal2binary (value):
    return [int (element) for element in bin (value)[2:].zfill(8)]

def binary2list(array, value):
    for i in range (0, 8):
        if (value & pow(2, i) == pow(2, i)):
            array[7 - i] = 1
        else:
            array[7 - i] = 0
    return array

array = [0, 0, 0, 0, 0, 0, 0, 0]

def adc(array):
    for i in range  (1, 256):
        decimal2binary(i)
        binary2list(array, i)
        GPIO.output (dac, array)
        time.sleep(0.005)

        j = GPIO.input(comp)
        if (j == 0):
            print(3.3 * i / 255)
            return i

        time.sleep (0.001)
    return
    
command = 1

while (command):
    try:
        while (1):
            adc (array)

    finally:
        GPIO.output (dac, 0)
        GPIO.cleanup()
        command = 0