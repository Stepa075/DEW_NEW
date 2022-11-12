import os
import sys
from tkinter import END, LabelFrame, Text, BOTH
from tkinter import Tk

text_file_value = ""


def on_start():
    if os.path.exists('data_file.txt'):
        with open('data_file.txt', "r") as f:
            for line in f.readlines():
                entry.insert(END, line)
            text = entry.get(1.0, END)[:-2]
            entry.delete(1.0, END)
            entry.insert(END, text)
            a = f.read()
            global text_file_value
            text_file_value = a
    else:
        with open('data_file.txt', "w"):
            pass
    load_settings()
    check_entry()

def load_settings():
    with open("settings.txt", "r", encoding="UTF8") as setings:
        lines = setings.split(';')



def check_entry():
    value_entry = str(entry.get("1.0", END))
    if value_entry == text_file_value + "\n":
        pass
    else:
        try:
            if os.path.exists('data_file.txt'):
                with open('data_file.txt', 'w') as f:
                    f.write(entry.get("1.0", END))
        except:
            sys.exit()
    print(value_entry)
    root.after(2000, check_entry)


root = Tk()

root.title("My notes")
root.geometry('300x100-0-40')
root.resizable(True, True)
f1 = LabelFrame(root)
f1.pack()
entry = Text(f1, font=("Arial Bold", 12))
entry.pack(fill=BOTH, expand=True)

root.after(0, on_start)

root.mainloop()
