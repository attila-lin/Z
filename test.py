import os
import Tkinter

root = Tkinter.Tk()
L = Tkinter.Listbox(selectmode=Tkinter.SINGLE)
gifsdict = {}

dirpath = './res/'
for gifname in os.listdir(dirpath):
    if gifname[0].isdigit():
       continue
    gifpath = os.path.join(dirpath, gifname)
    gif = Tkinter.PhotoImage(file=gifpath)
    gifsdict[gifname] = gif
    L.insert(Tkinter.END, gifname)

L.pack()
img = Tkinter.Label()
img.pack()
def list_entry_clicked(*ignore):
    imgname = L.get(L.curselection()[0])
    img.config(image=gifsdict[imgname])
L.bind('<ButtonRelease-1>', list_entry_clicked)
root.mainloop()