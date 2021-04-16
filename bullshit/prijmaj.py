from microbit import *
import speech
on=True
while True:
    if button_a.is_pressed():
        on=not on
    if on:
        value=pin2.read_analog()**2
        if value>1023:
            value=1023
        pin1.write_analog(value)
        display.show(value)
        speech.say(str(value))

    else:
        pin1.write_analog(0)
        display.show(' ')
