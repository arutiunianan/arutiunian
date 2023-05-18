import RPi.GPIO as GPIO
import time
import matplotlib as pyplot

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comparator = 4
weight = [128, 64, 32, 16, 8, 4, 2, 1]
LEDS = [21, 20, 16, 12, 7, 8, 25, 24]

            #ИНИЦИАЛИЗАЦИЯ И НАСТРОЙКИ GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)

            #ФУНКЦИЯ ПЕРЕВОДА ИЗ ДВОИЧНОЙ СИСТЕМЫ В ДЕСЯТИЧНУЮ
def decimilar2binary(value, n):
    return[int(element) for element in bin(value)[2:].zfill(n)]

            #ФУНКЦИЯ РАБОТЫ С АЦП
def adc():
    summary = 0
    for value in range(8):
        signal = decimilar2binary(summary +weight[value], 8)
        GPIO.output(dac, signal)
        time.sleep(0.01)
        if(GPIO.input(comparator) == 1):
            summary +=weight[value]
        signal = decimilar2binary(summary, 8)
        voltage = summary / levels * maxVoltage
        for value in range(8):
            if(value < summary / (levels - 1)*bits):
                GPIO.output(LEDS[value], 1)
            else: 
                GPIO.output(LEDS[value], 1)
      
        
    
try:

            #ИНИЦИАЛИЗАЦИЯ ПЕРЕМЕННЫХ И СПИСКОВ
    voltage = 0
    counter = 0
    time_of_start = time.time()
    result_of_experement = []

            #ЗАРЯДКА КОНДЕНСАТОРА И ЗАПИСЬ ПОКАЗАНИЙ В ОПЕРАТИВНУЮ ПАМЯТЬ
    print('\n Начало зарядки конденсатора')
    while voltage < 3.1 :
        summary = adc()
        voltage = summary * maxVoltage /levels
        print('voltage = {}'.format(voltage))
        result_of_experement.append(voltage)
        counter += 1
        for value in range(8):
            if(value < (summary/(levels - 1)*bits)):
                GPIO.OUTPUT(LEDS[value], 1)
            else:
                GPIO.OUTPUT(LEDS[value], 0)

    GPIO.setup(troykaModule, GPIO.OUT, initial = GPIO.LOW)

            #РАЗРЯДКА КОНДЕНСАТОРА И ЗАПИСЬ ПОКАЗАНИЙ В ОПЕРАТИВНУЮ ПАМЯТЬ
    print('\n Начало зарядки конденсатора')


    while True:
        adc()


except ValueError:
    print('Print enter number from 0 to 255\n')

except KeyboardInterrupt:
    print('\n The programm was stopped by keyboard')


finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
