#!/usr/bin/env python
from Tkinter import *
import tkMessageBox
import tkFileDialog

counter = 0


class Controller(Frame):
    '''
    App's controller
    '''
    def __init__(self, master=None):

        Frame.__init__(self, master, relief=SUNKEN, bd=2, width=800, height=400)
        self.pack()
        self.pack_propagate(0)

        self.master = master

        # menu
        self.creatMenu()

        # close
        self.master = master
        master.protocol("WM_DELETE_WINDOW", self.handler)

        
    def creatMenu(self):
        # menubar
        self.menubar = Menu(self.master)

        # menu
        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=menu)
        menu.add_command(label="About", command=self.showAbout)
        menu.add_command(label="Donate", command=self.showDonate)
        menu.add_command(label="Exit", command=self.exit)

        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            self.master.tk.call(master, "config", "-menu", self.menubar)


    def showAbout(self):
        pass

    def showDonate(self):
        pass

    def exit(self):
        self.quit()

    def handler(self):
        self.quit()

class ZhihuApp(object):
    def __init__(self, master=None):
        master.title("Zhihi Daily")
        self.controller = Controller(master)

def main():
    root = Tk()
    app = ZhihuApp(root)
    root.mainloop()
    root.destroy()

if __name__ == '__main__':
    main()
