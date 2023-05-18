import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

dac=[26, 19, 13, 6, 5, 11, 9, 10]
leds=[21, 20, 16, 12, 7, 8, 25, 24]
comp=4
troyka=17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)

def decimal2binary(a):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    k = 0

    for i in range(7, -1, -1):
        k +=2**i

        GPIO.output(dac, decimal2binary(k))

        sleep(0.005)

        if GPIO.input(comp) == 0:
            k -=2**i

    return k

def volume(value):
    
    if(value) == 0:
        GPIO.output(leds, decimal2binary(0))

    elif(value > 0 and value < 12):
        GPIO.output(leds, decimal2binary(1))

    elif(value >= 12 and value < 24):
        GPIO.output(leds, decimal2binary(3))

    elif(value >=24 and value < 32):
        GPIO.output(leds, decimal2binary(7))

    elif(value >= 32 and value < 40):
        GPIO.output(leds, decimal2binary(15))

    elif(value >= 40 and value < 48):
        GPIO.output(leds, decimal2binary(31))

    elif(value >= 48 and value < 56):
        GPIO.output(leds, decimal2binary(63))

    elif(value >= 56 and value < 63):
        GPIO.output(leds, decimal2binary(127))

    else:
        GPIO.output(leds, decimal2binary(255))


try:
    while True:
        value = adc()
        volume(value)
        voltage = value * 3.3 / 256

        print('value = {:^3} --> volt {:.2f}'.format(value, voltage))

        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()