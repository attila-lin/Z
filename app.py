#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from Tkinter import *
import tkMessageBox
import tkFileDialog

import os
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

VERSION = '0.0.1'

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
        '''

        '''
        # menubar
        menubar = Menu(self.master)
        # self.master.createcommand("::tk::mac::ShowHelp", self.about_action)
        # remove the 'python' submenu by py2app

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

    def about_action(self):
        pass

    def creatButtons(self):
        img_day   = PhotoImage(file="res/icon_1.gif") # reference PhotoImage in local variable
        img_topic = PhotoImage(file="res/icon_2.gif")
        # img_topic = img_topic.zoom(x=0.5,y=10)
        # print ""
        # print img_topic.width()

        button_daily = Button(self, justify=LEFT, command=self.daily_cb)
        button_daily.config(compound=LEFT, text="每日推荐", image=img_day) # width="40", height="20", compound="left"
        button_daily.image = img_day # keep a reference!
        # button_daily.pack()
        # button_daily.grid(row=0, column=0, sticky=W)
        button_daily.grid(columnspan=1, sticky=W)

        button_topic = Button(self, justify=LEFT, command=self.topic_cb)
        button_topic.config(compound=LEFT, text="  主题日报", image=img_topic) # , width="40", height="20", compound="left"
        button_topic.image = img_topic # keep a reference!
        # button_topic.pack()
        # button_topic.grid(row=1, column=0, sticky=W)
        button_topic.grid(columnspan=1, sticky=W)

    def daily_cb(self):
        pass

    def topic_cb(self):
        pass

    def creatList(self):
        listbox = Listbox(self, selectmode=SINGLE)
        listbox.grid(columnspan=1, sticky=W)
        # listbox.pack(fill=BOTH, expand=1)

        for item in ["每日推荐", "主题日报"]:
            listbox.insert(END, item)

        listbox.config(borderwidth=0,height=50)


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
