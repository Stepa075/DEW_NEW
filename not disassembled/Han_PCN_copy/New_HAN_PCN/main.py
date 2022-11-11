import time
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox as mbox
# from PIL import image
import os

import Functions, Variables

Font = "Tahoma 13"
Padx = 2
Pady = 2
Bg = "#e1e1e1"
Bw = 5


def ent_1_f(event):
    ent1.focus()


def ent_2_f(event):
    ent2.focus()


def analiz_run(event):
    analiz()


def run():
    Functions.date_for_session()
    Functions.create_directorys_and_files()

    print("I am start")


def analiz():
    log = ent1.get()
    pas = ent2.get()
    if Functions.autorization_user(log, pas):
        mbox.showinfo("Удача", "Вход подтвержден!")
        events = "Login successful. Login= " + log + ", " "Password= " + pas + "."
        place = 'bin/logging/' + str(Variables.date_current) + '_session.txt'
        Functions.logging_session(events, place)
        root_main.destroy()
        Functions.run_anyway()
    else:
        mbox.showerror("Ошибка", "Не верный логин или пароль!")
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent1.focus()


def setwindow(root_main):
    root_main.title("HAN Pult Вход в систему")
    root_main.resizable(False, False)

    w = 350
    h = 200
    ws = root_main.winfo_screenwidth()
    wh = root_main.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root_main.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))


root_main = Tk()
setwindow(root_main)
frame = Frame(master=root_main, bg="#3333ff")
frame.pack(fill=BOTH, expand=True)
frame_top = Frame(master=frame, bg="#3333ff")
frame_top.pack(fill=BOTH)

frame_1 = Frame(master=frame, bg="#3333ff")
frame_1.pack(padx=Padx, pady=Pady)
frame_2 = Frame(master=frame, bg="#3333ff")
frame_2.pack()
frame_3 = Frame(master=frame, bg="#3333ff")
frame_3.pack(fill=BOTH, side=BOTTOM)
lbl_top = Label(master=frame_top, text="Введите ваш логин и пароль \n для идентификации и входа в систему ", font=Font,
                bg=Bg, borderwidth=Bw)
lbl_top.pack(fill=BOTH, expand=True, padx=Padx, pady=Pady)
lbl1 = Label(master=frame_1, text="Логин  ", font=Font, bg=Bg, borderwidth=Bw)
lbl1.pack(fill=BOTH, side=LEFT, padx=Padx, pady=Pady)
ent1 = Entry(master=frame_1, font=Font, bg=Bg, borderwidth=Bw)
ent1.pack(fill=BOTH, side=RIGHT, padx=Padx, pady=Pady)
ent1.focus()
lbl2 = Label(master=frame_2, text="Пароль", font=Font, bg=Bg, borderwidth=Bw)
lbl2.pack(fill=BOTH, side=LEFT, padx=Padx, pady=Pady)
ent2 = Entry(master=frame_2, font=Font, bg=Bg, borderwidth=Bw)
ent2.pack(fill=BOTH, side=RIGHT, padx=Padx, pady=Pady)

button1 = Button(master=frame_3, text="Войти", font=Font, bg=Bg, borderwidth=Bw, command=analiz)
button1.pack(fill=BOTH, side=RIGHT, padx=Padx, pady=Pady)
# button1.bind("<Button-1>", analiz)
root_main.bind("<Return>", analiz_run)
root_main.bind("<Up>", ent_1_f)
root_main.bind("<Down>", ent_2_f)

root_main.after(0, run)
root_main.mainloop()
