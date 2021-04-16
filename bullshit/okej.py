from microbit import *
import radio
radio.on()
while True:
    print(radio.receive())
