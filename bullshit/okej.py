from microbit import *
import radio
radio.on()
def wait_r():
    r=radio.receive()
    while not r:
        r=radio.receive()
    return r
while True:
    print(wait_r())
