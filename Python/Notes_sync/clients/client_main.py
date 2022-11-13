import os
import sys
from threading import Thread
from tkinter import END, LabelFrame, Text, BOTH
from tkinter import Tk
from tkinter.ttk import Frame

import requests

import Variables
import streams

flag1 = 1


def on_start():
    global flag1
    if os.path.exists('data_file.txt'):
        with open('data_file.txt', "r") as f:
            for line in f.readlines():
                entry.insert(END, line)
            text = ''.join((str(entry.get("1.0", END))).split())
            Variables.text_file_value = text
    else:
        with open('data_file.txt', "w"):
            pass
    if os.path.exists('my_data.txt'):
        with open('my_data.txt', "r") as f:
            for line in f.readlines():
                entry1.insert(END, line)
    else:
        with open('my_data.txt', "w"):
            pass
    flag1 = 0

    load_settings()
    check_entry()


def load_settings():
    with open("settings.txt", "r", encoding="UTF8") as setings:
        f = setings.read()
        lines = f.split(';')
        print(lines[0])
        Variables.ip = lines[0]


def check_entry():
    global flag1
    val = ''.join((str(entry.get("1.0", END))).split())
    value_entry = val
    # print("",value_entry.split())
    if value_entry == str(Variables.text_file_value):
        Variables.list_of_set_data = list((entry.get("1.0", END)).split())
        print("in check entry if ;  " + str(Variables.list_of_set_data))
    else:
        try:
            if os.path.exists('data_file.txt'):
                with open('data_file.txt', 'w') as f:
                    f.write(entry.get("1.0", END))
                Variables.text_file_value = ''.join((str(entry.get("1.0", END))).split())
                Variables.list_of_set_data = list((entry.get("1.0", END)).split())
                set_data()
                print("in check entry else ;  " + str(Variables.list_of_set_data))
        except:
            sys.exit()
    root.after(2000, check_entry)


def check_my_entry():
    if os.path.exists('my_data.txt'):
        with open('my_data.txt', 'w') as f:
            f.write(entry1.get("1.0", END))
    root.after(5000, check_my_entry)


def set_data():
    try:
        myString = ','.join(Variables.list_of_set_data)
        url = ("http://" + str(Variables.ip) + "/data_set?data=" + myString)
        r = requests.get(url, timeout=3.00)
        r.encoding = "UTF8"
        if r.status_code == 200:
            print("set_data " + myString)
    except:
        print("EXcept of set data!!!")
        pass


root = Tk()

root.title("My notes")
root.geometry('300x155-0-40')
root.resizable(True, True)
root.minsize(300, 100)

f_top = Frame(root)
f_bot = Frame(root)
f_top.pack(fill=BOTH, expand=True)
f_bot.pack(fill=BOTH, expand=True)
entry = Text(f_top, font=("Arial Bold", 12), height=4, )
entry.pack(fill=BOTH, expand=True)
entry1 = Text(f_bot, font=("Arial Bold", 12), height=4)
entry1.pack(fill=BOTH, expand=True)

th1 = Thread(target=streams.get_data, daemon=True)
th1.start()
root.after(0, on_start)

root.after(0, check_my_entry)
root.mainloop()
