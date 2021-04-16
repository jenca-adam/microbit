from microbit import *
import music
import speech
pin1.write_digital(1)
pin2.write_digital(1)
auta=False
chodci=True
while True:
    if button_a.is_pressed():
        if auta:
            pin12.write_digital(0)
            pin8.write_digital(1)
            sleep(1000)
            pin8.write_digital(0)
            pin1.write_digital(1)
        else:
            pin1.write_digital(0)
            pin8.write_digital(1)
            sleep(1000)
            pin8.write_digital(0)
            pin12.write_digital(1)
            music.play('c6:3')
        auta=not auta
    if button_b.is_pressed():
        if chodci:
            pin2.write_digital(0)
            pin16.write_digital(1)
            sleep(1000)
        else:
            pin16.write_digital(0)
            pin2.write_digital(1)
            music.play('c5:2')
            sleep(1000)
        chodci=not chodci
    if auta and chodci:
        sleep(100)
        music.play('c6:7',wait=False)

        for i in range(10):
            pin2.write_digital(0)
            sleep(50-i)
            pin2.write_digital(1)
            sleep(50-i)
            pin12.write_digital(0)
            sleep(50-i)
            pin12.write_digital(1)
            sleep(50-i)
        
        music.play(music.WAWAWAWAA)
        
        pin12.write_digital(0)
        pin2.write_digital(0)
        break
        
