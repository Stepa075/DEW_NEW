import fileinput
import os
from threading import Thread
from tkinter import *


def check_entry():
    if os.path.exists('text_file.txt'):
        entry.delete(END)
        value_entry = str(entry.get("1.0", END))

        f = open('text_file.txt', 'r')
        a = f.read()
        text_file_value = a
        f.close()

        if value_entry == text_file_value + "\n":
            pass
        else:
            f = open('text_file.txt', 'w')
            f.write(entry.get("1.0", END))
            f.close()
    root.after(1000, check_entry)


def on_start():
    if os.path.exists('text_file.txt'):
        with open("text_file.txt", "r") as f:
            for line in f.readlines():
                entry.insert(END, line)
            text = entry.get(1.0, END)[:-2]
            entry.delete(1.0, END)
            entry.insert(END, text)
        # f = open('text_file.txt', 'r')
        # a = f.read()
        # text_file_value = a
        # f.close()
        # if text_file_value == "\n":
        #     os.remove("text_file.txt")
        #     f = open('text_file.txt', 'w')
        #     f.close()
        # else:
        #     pass
    else:
        f = open('text_file.txt', 'w')
        # f.write(entry.get())
        f.close()
    check_entry()

root = Tk()

root.title("My notes")
root.geometry('300x100-0-40')
root.resizable(True, True)
f1 = LabelFrame(root)
f1.pack()
entry = Text(f1, font=("Arial Bold", 12))
entry.pack(fill=BOTH, expand=True)

# button1 = Button(f3, text='Ответить', width=10, font=("Arial Bold", 11))  # command=Variables.about
# button1.pack(column=2, row=0, sticky=N + S + W + E, padx=3, pady=6)


# th = Thread(target=Threads.control_entry_value, daemon=True)
# th.start()
root.after(0, on_start)

root.mainloop()
