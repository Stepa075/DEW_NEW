import os
import pickle
import sys
from threading import Thread
from tkinter import *
from tkinter.ttk import *

import requests

import Variables
import streams


def load_settings():
    with open("settings.txt", "r", encoding="UTF8") as setings:
        f = setings.read()
        lines = f.split(';')
        print(lines[0])
        Variables.ip = lines[0]


def on_start():
    if os.path.exists('data.pickle'):
        with open('data.pickle', 'rb') as f:  # Выгружаем данные из файла пикли
            try:
                data_new = pickle.load(f)
            except:
                data_new = []
                pass
        Variables.list_of_saved_data = data_new
        for element in Variables.list_of_saved_data:
            entry.insert(1.0, element + '\n')
        print(Variables.list_of_saved_data)
    else:
        with open('data.pickle', "w"):
            pass
    load_settings()


def general_title_state():
    if Variables.code_of_response_server == 200:
        Variables.root_title = "My notes sync LAN (connected)"
        root.title(Variables.root_title)
        val = list((entry1.get(1.0, END)).split())
        val.reverse()
        print("value = " + str(val))
        if Variables.list_of_get_data != val:
            write_server_data_to_entry()

    else:
        Variables.root_title = "My notes sync LAN (no connect)"
        root.title(Variables.root_title)
        pass
    pass
    root.after(2000, general_title_state)


def write_server_data_to_entry():
    b = Variables.list_of_get_data
    entry1.delete(1.0, END)
    for element in b:
        entry1.insert(1.0, element + '\n')


def write_local_data():
    val = list((entry.get(1.0, END)).split())
    val.reverse()
    Variables.list_of_saved_data = val
    with open('data.pickle', "wb") as f:
        pickle.dump(Variables.list_of_saved_data, f)
    root.after(2000, write_local_data)


def set_data():
    try:
        r4_0 = Variables.parsing_GPIO_4relay1
        r4_1 = str(Variables.r1)
        r4_2 = str(Variables.r2)
        r4_3 = str(Variables.r3)
        r4_4 = str(Variables.r4)
        params = {'params': str(Variables.parsing_ESP1),
                  'params1': str(Variables.Sadok_Light1),
                  'params2_1': r4_1,
                  'params2_2': r4_2,
                  'params2_3': r4_3,
                  'params2_4': r4_4, 'control': 'home'}
        print(params)
        r = requests.get('http://f0555107.xsph.ru/index.php', params=params, timeout=3.0)

        mystring = ','.join(Variables.list_of_saved_data)
        url = ("http://" + str(Variables.ip) + "/data_set?data=" + mystring)
        r = requests.get(url, timeout=3.00)
        r.encoding = "UTF8"
        if r.status_code == 200:
            print("set_data " + mystring)
    except:
        print("EXcept of set data!!!")
        pass


def get_clipboard_text(event):
    from tkinter import Tk
    root = Tk()
    root.withdraw()
    s = root.clipboard_get()
    entry.insert(1.0, s)


def view_my_notes(event):
    t = Toplevel()
    t.wm_title("My notes")
    l = Text(t, font=("Arial Bold", 12))
    l.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    aaa = entry2.get(1.0, END)
    l.insert(1.0, aaa)


root = Tk()
root.iconphoto(True, PhotoImage(file='icon.png'))
root.title(Variables.root_title)
root.geometry('300x155-0-40')
root.resizable(True, True)

f_top = Frame(root)
f_bot = Frame(root)
f_my = Frame(root)
f_top.pack(fill=BOTH, expand=True)
f_bot.pack(fill=BOTH, expand=True)
f_my.pack(fill=BOTH, expand=True)
entry = Text(f_top, font=("Arial Bold", 12), height=2, width=27)
entry.bind('<Button-3>', get_clipboard_text)
entry.pack(fill=X, expand=True)
button = Button(f_top, text="Send", width=2, command=set_data)
button.pack(fill=X, expand=True)
entry1 = Text(f_bot, font=("Arial Bold", 12), height=4)
entry1.pack(fill=BOTH, expand=True)
entry2 = Text(f_bot, font=("Arial Bold", 12), height=2)
entry2.bind('<Button-3>', view_my_notes)
entry2.pack(fill=BOTH, expand=True)

th1 = Thread(target=streams.get_data, daemon=True)
th1.start()
root.after(0, on_start)
root.after(0, general_title_state)
root.after(0, write_local_data)
root.mainloop()
