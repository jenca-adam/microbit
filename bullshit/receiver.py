from microserial import Microbit
import os
import time
cache=""
for i in Microbit():
    if i!=cache:
        print(f'{i};{time.time()}\n',file=open("data.txt",'a'))
        cache=i
