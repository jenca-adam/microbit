#!/usr/bin/env python3

from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self,root,w=1920,h=1005):
        super().__init__()
        self.root=root
        self.w=w
        self.h=h
        self.initUI()
    def _reset(self,foo=None):
        a=Example(self.root,foo.width,foo.height)
    def initUI(self,foo=None):
        print(foo)
        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        print(self.root.winfo_screenheight())

        data=[]
        c=0
        with open('data.txt') as f :
            for line in f:
                if line=='\n':
                    continue
                temp,time=tuple(line.split(';'))
                data.append(c)

                data.append((self.h-int(temp)*5))
                c+=5
        
        
        canvas.create_line(*data,width=3)
        canvas.pack(fill=BOTH, expand=1)
        self.master.bind('<Configure>',self._reset)


def main(foo=None):

    root = Tk()
    ex = Example(root)
    root.geometry("1920x1005")
    root.mainloop()


if __name__ == '__main__':
    main()
