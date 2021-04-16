#!/usr/bin/env python3

from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self,foo=None):
        print(foo)
        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        data=[]
        c=0
        with open('data.txt') as f :
            for line in f:
                if line=='\n':
                    continue
                temp,time=tuple(line.split(';'))
                data.append(c)

                data.append(1005-int(temp)*5)
                c+=10
        
        
        canvas.create_line(*data,width=3)
        self.master.bind('<Key>',self.initUI)
        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example()
    root.geometry("1920x1005")
    root.mainloop()


if __name__ == '__main__':
    main()
