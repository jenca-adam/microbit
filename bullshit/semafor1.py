from microbit import *
import music
beeps=[]
w=True
c=False
gameover=False
def gameover_beeps():
    music.play(['c7:3','c7:7'])
    music.play(music.WAWAWAWAA)
    gameover=True
while True:
    if button_a.is_pressed():
        if button_b.is_pressed():
            break
        beeps.append('c')
        c=not c
        sleep(1000)
    if button_b.is_pressed():
        if button_a.is_pressed():
            break
        elif w:
            beeps.append('w')        
            w=not w
    beeps.append('b')
    sleep(50)
w=True
c=False
while not gameover:
    for move in beeps:
        if not gameover:
            if w and c:
                gameover_beeps()
                gameover=True
                break
            type=move[0]
            if type=='c':
                c=not c
                pin8.write_digital(1)
                sleep(843)
                pin8.write_digital(0)
            elif type=='w':
                w=not w
            if c:
                pin1.write_digital(0)
                pin12.write_digital(1)
            if not c:
                pin1.write_digital(1)
                pin12.write_digital(0)
            if w:
                pin2.write_digital(1)
                pin15.write_digital(0)
            if not w:
                pin2.write_digital(0)
                pin15.write_digital(1)
            sleep(50)


for pin in(pin8,pin1,pin12,pin2,pin15):
    pin.write_digital(0)
display.show(Image.HAPPY)
