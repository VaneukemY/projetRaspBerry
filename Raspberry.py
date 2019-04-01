#Bibliothèque
import RPi.GPIO as GPIO
from time import GPIO

#Déclaration des pins ou de variable générale

def setup():
    GPIO.setmode(GPIO.BOARD) #Correspond au numéro physique des ports
    #Sinon si on aurait choisi BCM ça serait la numérotation GPIO
    GPIO.setup(OuputPin,GPIO.OUT) #Définis un Pin de sortie
    GPIO.setup(SensorPinIn,GPIO.IN,pull_up_down=GPIO.PUD_UP) #définis une entrée PULL UP OU DOWN
    GPIO.output(OutputPin,GPIO.HIGH) #Allume la sortie sinon si on l'éteint c'est LOW



def loop():
    while True:
        


def destroy():
    GPIO.output(OutputPin, GPIO.HIGH)
    GPIO.cleanup()



if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    
