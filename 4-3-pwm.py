import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)

dac=[26,19,13,6,5,11,9,10]

RPi.GPIO.setup(3,RPi.GPIO.OUT)

p=RPi.GPIO.PWM(3,100)
p.start(0)
                               
try:
    while(True):
        dutycycle=int(input('Write number: '))
        p.start(dutycycle)

finally:
    p.stop()
    RPi.GPIO.output(3,0)
    RPi.GPIO.cleanup()
