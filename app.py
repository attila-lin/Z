#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from Tkinter import *
import tkMessageBox
import tkFileDialog

import os



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

        # button
        self.creatButtons()

        # list: Daily
        self.creatList()

        # close
        self.master = master
        master.protocol("WM_DELETE_WINDOW", self.handler)


    def creatMenu(self):
        # menubar
        menubar = Menu(self.master)

        # menu
        menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=menu)
        menu.add_command(label="About", command=self.showAbout)
        menu.add_command(label="Donate", command=self.showDonate)
        menu.add_command(label="Exit", command=self.exit)

        try:
            self.master.config(menu=menubar)
        except AttributeError:
            self.master.tk.call(master, "config", "-menu", menubar)

    def creatButtons(self):
        img_day = PhotoImage(file="res/a2.gif") # reference PhotoImage in local variable
        img_topic = PhotoImage(file="res/a1.gif")

        button_day = Button(self, justify=LEFT)
        button_day.config(text="每日推荐", image=img_day, width="40", height="20", compound="left")
        button_day.pack(side=LEFT)

        button_topic = Button(self, justify=LEFT)
        button_topic.config(text="主题日报", image=img_topic, width="40", height="20", compound="left")
        button_topic.pack(side=LEFT)


    def creatList(self):
        listbox = Listbox(self, selectmode=SINGLE)
        listbox.pack(fill=BOTH, expand=1)

        # for item in ["每日推荐", "主题日报"]:
        #     listbox.insert(END, item)


    def showAbout(self):
        self.aboutentry = Toplevel()
        self.aboutentry.title("")

        namelabel = Label(self.aboutentry, text="知乎日报")
        namelabel.place(x=20, y=20)
        versionlabel = Label(self.aboutentry, text="Version 0.0.1")
        versionlabel.place(x=20, y=40)


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
