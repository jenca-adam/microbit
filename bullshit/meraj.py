from microbit import *
import radio
display.scroll('bla')
radio.on()
while True:
    radio.send(chr(temperature()))
