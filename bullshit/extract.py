#!/usr/bin/env python3

from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        with open('data.txt') as f :
            for line in f
        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example()
    root.geometry("1920x1005")
    root.mainloop()


if __name__ == '__main__':
    main()
