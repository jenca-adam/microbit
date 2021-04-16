from microserial import Microbit
import os
import time
cache=""
for i in Microbit():
    if (i!=cache or i!='\n') and i:

        print(f'{i[:-1]};{time.time()}\n',file=open("data.txt",'a'))
        cache=i
