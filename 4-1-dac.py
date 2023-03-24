import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

dac=[26,19,13,6,5,11,9,10]

RPi.GPIO.setup(dac,RPi.GPIO.OUT)
def translate(a):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]
try:
    a10=input('Write number 0-255: ')
    while(a10!='q'):
        if a10.isdigit() and int(a10)<=255:
            RPi.GPIO.output(dac,translate(int(a10)))
            print("{:.4f}".format(int(a10)/256*3.3))
        else:
            print('Wrong number')
        a10=input('Write number 0-255: ')
        
finally:
    RPi.GPIO.output(dac,0)
    RPi.GPIO.cleanup()
