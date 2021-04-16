from microbit import *
import radio
radio.on()
while True:
    sleep(10000)
    radio.send(str(temperature()))
