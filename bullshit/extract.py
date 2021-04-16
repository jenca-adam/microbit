#!/usr/bin/env python3

from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self,root):
        super().__init__()
        self.r=root
        self.initUI()

    def initUI(self,foo=None):
        print(foo)
        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        print(self.root.winfo_height())

        data=[]
        c=0
        with open('data.txt') as f :
            for line in f:
                if line=='\n':
                    continue
                temp,time=tuple(line.split(';'))
                data.append(c)

                data.append((self.root.winfo_height()-int(temp)*5))
                c+=5
        
        
        canvas.create_line(*data,width=3)
        canvas.pack(fill=BOTH, expand=1)
        self.master.bind('<Key>',lambda foo:eval('self=Example()'))


def main():

    root = Tk()
    ex = Example(root)
    root.geometry("1920x1005")
    root.mainloop()


if __name__ == '__main__':
    main()
