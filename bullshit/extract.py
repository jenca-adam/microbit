#!/usr/bin/env python3

from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self,root,):
        super().__init__()
        self.root=root
        self.initUI()
    def _reset(self,foo=None):
        del self.canvas
        self.__init__(self.root)
    def initUI(self,foo=None,h=None):
        if h is None:
            h=self.winfo_screenheight()
        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)

        data=[]
        c=0
        with open('data.txt') as f :
            for line in f:
                if line=='\n':
                    continue
                temp,time=tuple(line.split(';'))
                data.append(c)

                data.append((h-int(temp)*5))
                c+=5
        
        
        self.canvas.create_line(*data,width=3)
        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.bind('<t>',self._reset)

def main(foo=None):

    root = Tk()
    ex = Example(root)
    root.geometry("1920x1005")
    root.mainloop()


if __name__ == '__main__':
    main()
