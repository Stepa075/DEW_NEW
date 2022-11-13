import os
import sys
from threading import Thread
from tkinter import *
from tkinter.ttk import *

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
                entry2.insert(END, line)
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
    check_changes_on_server()
    root.after(2000, check_entry)


def check_my_entry():
    if os.path.exists('my_data.txt'):
        with open('my_data.txt', 'w') as f:
            f.write(entry2.get("1.0", END))
    root.after(5000, check_my_entry)


def check_changes_on_server():
    if Variables.code_of_response_server == 200:
        server_data = Variables.list_of_get_data
        local_data = ','.join((str(entry1.get("1.0", END))).split())
        print(server_data)
        print(local_data)
        if server_data == local_data:
            pass
        else:
            entry1.delete(1.0, END)
            b = Variables.list_of_get_data.split(',')
            for element in b:
                entry1.insert(END, element + '\n')
    else:
        pass


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

def view_my_notes(event):
    t = Toplevel()
    t.wm_title("My notes")
    l = Text(t, font=("Arial Bold", 12))
    l.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    aaa = entry2.get(1.0, END)
    l.insert(1.0, aaa)



root = Tk()
root.iconphoto(True, PhotoImage(file='icon.png'))
root.title("My notes sync LAN")
root.geometry('300x155-0-40')
root.resizable(True, True)

f_top = Frame(root)
f_bot = Frame(root)
f_my = Frame(root)
f_top.pack(fill=BOTH, expand=True)
f_bot.pack(fill=BOTH, expand=True)
f_my.pack(fill=BOTH, expand=True)
entry = Text(f_top, font=("Arial Bold", 12), height=2)
entry.pack(fill=BOTH, expand=True)
entry1 = Text(f_bot, font=("Arial Bold", 12), height=4)
entry1.pack(fill=BOTH, expand=True)
entry2 = Text(f_bot, font=("Arial Bold", 12), height=2)
entry2.bind('<Button-3>', view_my_notes)
entry2.pack(fill=BOTH, expand=True)

th1 = Thread(target=streams.get_data, daemon=True)
th1.start()
root.after(0, on_start)
root.after(0, check_my_entry)

root.mainloop()
