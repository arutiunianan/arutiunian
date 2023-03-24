import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)

dac=[26,19,13,6,5,11,9,10]

RPi.GPIO.setup(dac,RPi.GPIO.OUT)
def dec2bin(a):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]
try:
    a10=input('Write number 0-255: ')
    while(True):
        
        if a10=='q': break
        if a10.isdigit() and int(a10)<=255 and int(a10)>=0:
            for i in range(255):
                RPi.GPIO.output(dac,dec2bin(i))
                time.sleep(int(a10)/511)
            for i in range(255,-1,-1):
                RPi.GPIO.output(dac,dec2bin(i))
                time.sleep(int(a10)/511)
        else:
            print('Wrong number')
        
        
finally:
    RPi.GPIO.output(dac,0)
    RPi.GPIO.cleanup()
