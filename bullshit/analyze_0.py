from microbit import *

while True:
    val=pin0.read_digital()
    if not val:
        display.show(Image.SAD)
    else:
        display.show(Image.HAPPY)
