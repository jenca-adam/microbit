from microserial import Microbit
import os
import time
cache=""
for i in Microbit():
    if (i!='\n') and i:
        print (f'got packet {repr(i)} from /dev/ACM0')
        print(f'{i[:-1]};{time.time()}\n',file=open("data.txt",'a'))
