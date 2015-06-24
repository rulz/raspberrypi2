# Activación del servicio SSH en el Raspberry Pi

para poder controlar los puertos de GPIO, se de installar la siguiente librería para python.

***1. Instalar python-dev***
```
sudo apt-get install python-dev
```
***2. Instalar RPi.GPIO***
``` 
pip install RPi.GPIO
```
asumiendo que usarán un entorno virtual [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)



encender un led
```
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)

try:
    while(True):
        GPIO.output(27, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(27, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

'''GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) ## GPIO 17 como salida
GPIO.setup(27, GPIO.OUT) ## GPIO 27 como salida

def game_led():
    print "Ejecutando el script game_led()"
    for iteracion in range(1,31):
        GPIO.output(17, True) ## Enciendo el 17
        GPIO.output(27, False) ## Apago el 27
        time.sleep(1) ## Esperamos 1 segundo
        GPIO.output(17, False) ## Apago el 17
        GPIO.output(27, True) ## Enciendo el 27
        time.sleep(1) ## Esperamos 1 segundo
    print "Finalizado script"

game_led()'''
```


