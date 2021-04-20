#!/usr/bin/python3
from flask import *
app=Flask(__name__)
@app.route('/')
def index():
        data=[]
        c=0
        h=1005
        with open('data.txt') as f :
            for line in f:
                if line=='\n':
                    continue
                temp,time=tuple(line.split(';'))
                if not temp:
                    continue

                data.append([round(c),(h-int(temp)*5)-h//2,temp])
                c+=0.25
        return render_template('index.html',data=data)
app.run()
    
