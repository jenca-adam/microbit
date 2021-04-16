from microbit import *
#tuna je dolezity hlavne obvod, takze kod moze byt aj takyto jednoduchy.
value=0
while True:
    if value:
        value=0
    else:
        value=1023
    pin16.write_analog(value)
    sleep(1000)
