from tkinter import *
from tkinter.filedialog import *
import os
import Variables

def directory_out():
    op = askdirectory()
    Variables.dir1 = op



def directory_in():
    op1 = askdirectory()
    Variables.dir2 = op1



def copy_dir():
    print(Variables.dir1)
    print(Variables.dir2)
    x = os.listdir(Variables.dir1)
    y = os.listdir(Variables.dir2)
    os.path.supports_unicode_filenames.
    print(x)
    print(y)


def setwindow(root_main):
    root_main.title("Sinchronizator")
    root_main.resizable(False, False)

    w = 350
    h = 70

    ws = root_main.winfo_screenwidth()
    wh = root_main.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root_main.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))


root_main = Tk()
setwindow(root_main)
frame_upper = Frame(root_main)
frame_upper.pack(fill=BOTH, expand=True)
frame_main = Frame(frame_upper)
frame_main.pack(fill=BOTH, expand=True)
frame_bottom = Frame(frame_upper)
frame_bottom.pack(fill=BOTH, expand=True)
but1 = Button(frame_main, text="Open directory out", command=directory_out)
but1.pack(fill=BOTH, side=LEFT)
ent1 = Entry(frame_main)
ent1.insert(0, "     Enter a time period")
but2 = Button(frame_main, text="Open directory in", command=directory_in)
but2.pack(fill=BOTH, side=RIGHT)
ent1.pack(fill=BOTH, expand=True)
ent1.focus()
but3 = Button(frame_bottom, text="Sinchronizate now!", command=copy_dir)
but3.pack(fill=BOTH, expand=True)

root_main.mainloop()
