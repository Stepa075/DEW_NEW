import fileinput
import os
from threading import Thread
from tkinter import *
from tkinter import messagebox as mbox
from tkinter.filedialog import askopenfilenames

import Functions
import Streams
import Variables


def exit():
    Functions.logging_session("Session Logging Out. Exit program", 'bin/logging/' + str(Variables.date_current) + '_session.txt')
    root.destroy()


def run_active_alert():
    frame_one()

    lbl1['text'] = "Активные стработки"


def run_catalog():
    frame_two()

    lbl1['text'] = "Каталог объектов"


def run_append():
    frame_three()
    add_object()
    lbl1['text'] = "Добавление объекта в базу"


def run_delete():
    frame_four()
    delete_object()
    lbl1['text'] = "Удаление объекта из базы"


def run_settings():
    frame_five()
    settings()
    lbl1['text'] = "Settings"


def onSelect(val):
    sender = val.widget
    idx = sender.curselection()
    print("idx= " + str(idx))
    value = sender.get(idx)
    # print(value)
    win_active_alarm(value, idx)

def win_active_alarm(list, idx):
    win = Toplevel(root)
    win.title("Han Pult Окно активной сработки")
    win.resizable(False, False)
    w = 800
    h = 640
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2) - 20
    win.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

    part_one = list[:list.find(";")]
    part_two_1 = list.split(';')
    part_two = part_two_1[1]
    number_of_alert = list[:list.find(",")]
    time_for_start_working = str(Functions.update_time_for_writing_files())
    time_for_start_working_this = str(Functions.update_time())
    idx = idx
    def open_cart():
        card_object_view(win, number_of_alert)

    def outgouing_gbr():
        lst_alarm.insert(END, " " + Functions.update_time() + ". ГБР выслана  на объект.")

    def incomming_gbr():
        lst_alarm.insert(END, " " + Functions.update_time() + ". ГБР прибыла  на объект.")

    def inspect_object_ok():
        lst_alarm.insert(END, " " + Functions.update_time() + ". Объект осмотрен, все ОК!.")

    def inspect_object_problem():
        lst_alarm.insert(END, " " + Functions.update_time() + ". Объект осмотрен, проблема.")

    def otboy():
        lst_alarm.insert(END, " " + Functions.update_time() + ". Отбой ГБР по объекту.")

    def not_action():
        lst_alarm.insert(END, " " + Functions.update_time() + ". Реагирование на объект отключено.")

    def ended_alarm():
        lst_alarm.insert(END, " " + Functions.update_time() + ". Тревога завершена.")
        ended_list = []
        ended_list = lst_alarm.get(0, END)
        Functions.writing_alert(time_for_start_working, ended_list, str(number_of_alert))
        lst.delete(idx)
        win.destroy()
    frame_main_frame_alarm = Frame(master=win, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame_main_frame_alarm.pack(fill=BOTH, expand=True)

    frame_top_alarm = Frame(master=frame_main_frame_alarm, relief=RAISED, borderwidth=2, bg='Gray')
    frame_top_alarm.pack(fill=BOTH, padx=4, pady=4, side=TOP, expand=True)

    frame_center_alarm = Frame(master=frame_main_frame_alarm, relief=RAISED, borderwidth=2, bg='Gray')
    frame_center_alarm.pack(fill=BOTH, padx=4, pady=4, side=TOP, expand=True)

    frame_bottom_alarm = Frame(master=frame_main_frame_alarm, relief=RAISED, borderwidth=2, bg='Gray')
    frame_bottom_alarm.pack(fill=BOTH, padx=4, pady=4, side=BOTTOM, expand=True)

    frame_left_alarm = Frame(master=frame_center_alarm, relief=RAISED, borderwidth=2, bg='Gray')
    frame_left_alarm.pack(fill=BOTH, padx=4, pady=4, side=LEFT)

    frame_right_alarm = Frame(master=frame_center_alarm, relief=RAISED, borderwidth=2, bg='Gray')
    frame_right_alarm.pack(fill=BOTH, padx=4, pady=4, side=RIGHT, expand=True)

    lab_name_of_alarm = Label(master=frame_top_alarm, text=part_one, width=16, height=1, font="Tahoma 12")
    lab_name_of_alarm.pack(fill=BOTH, padx=4, pady=4, expand=True)

    list_of_alarm = part_two
    lst_alarm = Listbox(master=frame_right_alarm, selectmode=SINGLE, font="Tahoma 12")
    scr_alarm = Scrollbar(master=frame_right_alarm, command=lst.yview)
    lst_alarm.configure(yscrollcommand=scr.set)
    scr_alarm.pack(fill=BOTH, side=RIGHT)
    lst_alarm.pack(fill=BOTH, padx=4, pady=4, expand=True)
    lst_alarm.insert(END, " " + time_for_start_working_this + ". Прием тревоги и начало обработки.")
    lst_alarm.insert(END, list_of_alarm)

    lbl1 = Label(frame_left_alarm, text="Этапы обработки", width=15, font="Tahoma 14")
    lbl1.grid(padx=5, pady=5, row=0)
    btn1 = Button(frame_left_alarm, text="Отправить ГБР", width=15, bg="Green", activebackground="Yellow",
                  font="Tahoma 14", command=outgouing_gbr)
    btn1.grid(padx=5, pady=5, row=1)
    btn2 = Button(frame_left_alarm, text="Прибытие ГБР", width=15, bg="Green", activebackground="Yellow",
                  font="Tahoma 14", command=incomming_gbr)
    btn2.grid(padx=5, pady=5, row=2)
    btn3 = Button(frame_left_alarm, text="Осмотрено Ок!", width=15, bg="Green", activebackground="Yellow",
                  font="Tahoma 14", command=inspect_object_ok)
    btn3.grid(padx=5, pady=5, row=3)
    btn4 = Button(frame_left_alarm, text="Осм., проблема", width=15, bg="Red", activebackground="Yellow",
                  font="Tahoma 14", command=inspect_object_problem)
    btn4.grid(padx=5, pady=5, row=4)
    btn5 = Button(frame_left_alarm, text="Отбой", width=15, bg="Green", activebackground="Yellow", font="Tahoma 14", command=otboy)
    btn5.grid(padx=5, pady=5, row=5)
    btn6 = Button(frame_left_alarm, text="Не реагировать", width=15, bg="Purple", activebackground="Yellow",
                  font="Tahoma 14", command=not_action)
    btn6.grid(padx=5, pady=5, row=6)
    btn7 = Button(frame_left_alarm, text="Завершить", width=15, bg="Green", activebackground="Yellow", font="Tahoma 14", command=ended_alarm)
    btn7.grid(padx=5, pady=5, row=7)
    btn8 = Button(frame_left_alarm, text="Карточка объекта", width=15, bg="Green", activebackground="Yellow",
                  font="Tahoma 14", command=open_cart)
    btn8.grid(padx=5, pady=5, row=8)

    lbl1 = Label(master=frame_bottom_alarm, text="Краткий\n комментарий \nк сработке", width=17, height=1,
                 font="Tahoma 12")
    lbl1.pack(fill=BOTH, padx=4, pady=4, ipadx=4, ipady=4, side=LEFT)
    text_comment = Text(master=frame_bottom_alarm, width=150, height=1, font="Tahoma 14", wrap=WORD)
    text_comment.pack(fill=BOTH, padx=4, pady=4, ipadx=4, ipady=4, side=RIGHT, expand=True)



def add_object():
    def onWrite_to_base():
        list_add = [entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get(), entry8.get(),
                    entry9.get(), entry10.get(), entry11.get(), entry12.get(), entry13.get(), entry14.get(),
                    entry15.get(), entry16.get()]
        print(list_add)
        if entry2.get() == "":
            mbox.showerror("Ошибка", "Не введен пультовый номер!")
        else:
            dir = "Base/"

            try:
                path = dir + str(list_add[0]) + "/"
                os.makedirs(path)
                for i in Variables.Variable_op:
                    z = Variables.Variable_op.index(i)
                    image = Image.open(i)

                    # sa = asksaveasfilename()
                    image.save(dir + str(list_add[0]) + "/" + str(list_add[0]) + "_" + str(z) + ".jpg")

            except FileExistsError:
                for i in Variables.Variable_op:
                    z = Variables.Variable_op.index(i)
                    image = Image.open(i)
                    item = 0
                    while os.path.exists(dir + str(list_add[0]) + "/" + str(list_add[0]) + "_" + str(z) + ".jpg"):
                        var = item + 1
                        z += 1
                    image.save(dir + str(list_add[0]) + "/" + str(list_add[0]) + "_" + str(z) + ".jpg")
                pass

            f = open("Base/" + str(list_add[0]) + "/" + str(list_add[0]) + ".txt", 'w')
            for e in list_add:
                f.write(e + "\n")
            f.close()

    def add_images():
        zyx = 0
        print("Adding images to card of object")
        op = askopenfilenames()
        Variables.Variable_op = op
        for i in Variables.Variable_op:
            zyx = Variables.Variable_op.index(i)
        label_image_added["text"] = "Будет добавлено " + str(zyx + 1) + " фото."

    frame1 = Frame(master=frame_three_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame1.pack(fill=BOTH)
    frame2 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame2.pack(fill=BOTH, expand=True)
    frame3 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame3.pack(fill=BOTH, expand=True)
    frame4 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame4.pack(fill=BOTH, expand=True)
    frame5 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame5.pack(fill=BOTH, expand=True)
    frame6 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame6.pack(fill=BOTH, expand=True)
    frame7 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame7.pack(fill=BOTH, expand=True)
    frame8 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame8.pack(fill=BOTH, expand=True)
    frame9 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame9.pack(fill=BOTH, expand=True)
    frame10 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame10.pack(fill=BOTH, expand=True)
    frame11 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame11.pack(fill=BOTH, expand=True)
    frame12 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame12.pack(fill=BOTH, expand=True)
    frame13 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame13.pack(fill=BOTH, expand=True)
    frame14 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame14.pack(fill=BOTH, expand=True)
    frame15 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame15.pack(fill=BOTH, expand=True)
    frame16 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame16.pack(fill=BOTH, expand=True)
    frame17 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame17.pack(fill=BOTH, expand=True)
    frame18 = Frame(master=frame1, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame18.pack(fill=BOTH, expand=True)

    font = "Tahoma 12"
    padx = 2
    pady = 2
    width = 15
    width1 = 3

    l2 = Label(frame2, text="1", font=font, padx=padx, pady=pady, width=width1)
    l2.pack(fill=BOTH, side=LEFT)
    label2 = Label(frame2, text="Пультовый номер", font=font, padx=padx, pady=pady, width=width)
    label2.pack(fill=BOTH, side=LEFT)
    entry2 = Entry(frame2, bd=3)
    entry2.pack(fill=BOTH, expand=True)
    # entry2.bind("<<Button-1>>", onWrite_to_base)
    l3 = Label(frame3, text="2", font=font, padx=padx, pady=pady, width=width1)
    l3.pack(fill=BOTH, side=LEFT)
    label3 = Label(frame3, text="Название", font=font, padx=padx, pady=pady, width=width)
    label3.pack(fill=BOTH, side=LEFT)
    entry3 = Entry(frame3, bd=3)
    entry3.pack(fill=BOTH, expand=True)
    l4 = Label(frame4, text="3", font=font, padx=padx, pady=pady, width=width1)
    l4.pack(fill=BOTH, side=LEFT)
    label4 = Label(frame4, text="Хозорган", font=font, padx=padx, pady=pady, width=width)
    label4.pack(fill=BOTH, side=LEFT)
    entry4 = Entry(frame4, bd=3)
    entry4.pack(fill=BOTH, expand=True)
    l5 = Label(frame5, text="4", font=font, padx=padx, pady=pady, width=width1)
    l5.pack(fill=BOTH, side=LEFT)
    label5 = Label(frame5, text="Адрес", font=font, padx=padx, pady=pady, width=width)
    label5.pack(fill=BOTH, side=LEFT)
    entry5 = Entry(frame5, bd=3)
    entry5.pack(fill=BOTH, expand=True)
    l6 = Label(frame6, text="5", font=font, padx=padx, pady=pady, width=width1)
    l6.pack(fill=BOTH, side=LEFT)
    label6 = Label(frame6, text="Зона1", font=font, padx=padx, pady=pady, width=width)
    label6.pack(fill=BOTH, side=LEFT)
    entry6 = Entry(frame6, bd=3)
    entry6.pack(fill=BOTH, expand=True)
    l7 = Label(frame7, text="6", font=font, padx=padx, pady=pady, width=width1)
    l7.pack(fill=BOTH, side=LEFT)
    label7 = Label(frame7, text="Зона2", font=font, padx=padx, pady=pady, width=width)
    label7.pack(fill=BOTH, side=LEFT)
    entry7 = Entry(frame7, bd=3)
    entry7.pack(fill=BOTH, expand=True)
    l8 = Label(frame8, text="7", font=font, padx=padx, pady=pady, width=width1)
    l8.pack(fill=BOTH, side=LEFT)
    label8 = Label(frame8, text="Зона3", font=font, padx=padx, pady=pady, width=width)
    label8.pack(fill=BOTH, side=LEFT)
    entry8 = Entry(frame8, bd=3)
    entry8.pack(fill=BOTH, expand=True)
    l9 = Label(frame9, text="8", font=font, padx=padx, pady=pady, width=width1)
    l9.pack(fill=BOTH, side=LEFT)
    label9 = Label(frame9, text="Зона4", font=font, padx=padx, pady=pady, width=width)
    label9.pack(fill=BOTH, side=LEFT)
    entry9 = Entry(frame9, bd=3)
    entry9.pack(fill=BOTH, expand=True)
    l10 = Label(frame10, text="9", font=font, padx=padx, pady=pady, width=width1)
    l10.pack(fill=BOTH, side=LEFT)
    label10 = Label(frame10, text="Зона5", font=font, padx=padx, pady=pady, width=width)
    label10.pack(fill=BOTH, side=LEFT)
    entry10 = Entry(frame10, bd=3)
    entry10.pack(fill=BOTH, expand=True)
    l11 = Label(frame11, text="10", font=font, padx=padx, pady=pady, width=width1)
    l11.pack(fill=BOTH, side=LEFT)
    label11 = Label(frame11, text="Зона6", font=font, padx=padx, pady=pady, width=width)
    label11.pack(fill=BOTH, side=LEFT)
    entry11 = Entry(frame11, bd=3)
    entry11.pack(fill=BOTH, expand=True)
    l12 = Label(frame12, text="11", font=font, padx=padx, pady=pady, width=width1)
    l12.pack(fill=BOTH, side=LEFT)
    label12 = Label(frame12, text="Зона7", font=font, padx=padx, pady=pady, width=width)
    label12.pack(fill=BOTH, side=LEFT)
    entry12 = Entry(frame12, bd=3)
    entry12.pack(fill=BOTH, expand=True)
    l13 = Label(frame13, text="12", font=font, padx=padx, pady=pady, width=width1)
    l13.pack(fill=BOTH, side=LEFT)
    label13 = Label(frame13, text="Зона8", font=font, padx=padx, pady=pady, width=width)
    label13.pack(fill=BOTH, side=LEFT)
    entry13 = Entry(frame13, bd=3)
    entry13.pack(fill=BOTH, expand=True)
    l14 = Label(frame14, text="13", font=font, padx=padx, pady=pady, width=width1)
    l14.pack(fill=BOTH, side=LEFT)
    label14 = Label(frame14, text="Основная ГБР", font=font, padx=padx, pady=pady, width=width)
    label14.pack(fill=BOTH, side=LEFT)
    entry14 = Entry(frame14, bd=3)
    entry14.pack(fill=BOTH, expand=True)
    l15 = Label(frame15, text="14", font=font, padx=padx, pady=pady, width=width1)
    l15.pack(fill=BOTH, side=LEFT)
    label15 = Label(frame15, text="Резервная ГБР", font=font, padx=padx, pady=pady, width=width)
    label15.pack(fill=BOTH, side=LEFT)
    entry15 = Entry(frame15, bd=3)
    entry15.pack(fill=BOTH, expand=True)
    l16 = Label(frame16, text="15", font=font, padx=padx, pady=pady, width=width1)
    l16.pack(fill=BOTH, side=LEFT)
    label16 = Label(frame16, text="Примечание", font=font, padx=padx, pady=pady, width=width)
    label16.pack(fill=BOTH, side=LEFT)
    entry16 = Entry(frame16, bd=3)
    entry16.pack(fill=BOTH, expand=True)

    button_image_add = Button(frame18, text="Добавить фото объекта", font=font, padx=padx, pady=pady, borderwidth=5,
                              command=add_images)
    label_image_added = Label(frame18, text="Фото еще не добавлены", font=font, padx=padx, pady=pady, borderwidth=5)
    button_apply18 = Button(frame18, text="Добавить в базу", font=font, padx=padx, pady=pady, borderwidth=5,
                            command=onWrite_to_base)
    button_apply18.pack(fill=BOTH, side=RIGHT)
    button_image_add.pack(fill=BOTH, side=LEFT)
    label_image_added.pack(fill=BOTH, expand=True)


def settings():

    Padx = 0
    Pady = 0
    Ipadx = 0
    Ipady = 0
    Bg = "#e8e6e7"
    Bg1 = "White"
    Font = "Tahoma 12"
    width = 35

    def load_lines_from_file():
        directory = "bin/"
        list_of_lines = []
        f = open(directory + "settings.ini", 'r')
        for line in f:
            list_of_lines.append(line)
        f.close()
        print(list_of_lines)
        ent1.insert(0, list_of_lines[0])
        ent2.insert(0, list_of_lines[1])
        ent3.insert(0, list_of_lines[2])
        ent4.insert(0, list_of_lines[3])
        ent5.insert(0, list_of_lines[4])
        ent6.insert(0, list_of_lines[5])
        ent7.insert(0, list_of_lines[6])
        ent8.insert(0, list_of_lines[7])
        ent9.insert(0, list_of_lines[8])
        ent10.insert(0, list_of_lines[9])
        ent11.insert(0, list_of_lines[10])
        ent12.insert(0, list_of_lines[11])
        ent13.insert(0, list_of_lines[12])
        ent14.insert(0, list_of_lines[13])
        ent15.insert(0, list_of_lines[14])
        ent16.insert(0, list_of_lines[15])
        ent17.insert(0, list_of_lines[16])

    def clear_fields():
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        ent4.delete(0, END)
        ent5.delete(0, END)
        ent6.delete(0, END)
        ent7.delete(0, END)
        ent8.delete(0, END)
        ent9.delete(0, END)
        ent10.delete(0, END)
        ent11.delete(0, END)
        ent12.delete(0, END)
        ent13.delete(0, END)
        ent14.delete(0, END)
        ent15.delete(0, END)
        ent16.delete(0, END)
        ent17.delete(0, END)

    def save_fields_to_file():
        list_add = [ent1.get(), ent2.get(), ent3.get(), ent4.get(), ent5.get(), ent6.get(), ent7.get(),
                    ent8.get(), ent9.get(), ent10.get(), ent11.get(), ent12.get(), ent13.get(), ent14.get(),
                    ent15.get(),
                    ent16.get(), ent17.get()]
        print(list_add)

        directory = "bin/"

        f = open(directory + "settings.ini", 'w')
        for e in list_add:
            f.write(e)
        f.close()

    frame_frame = Frame(master=frame_five_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame_frame.pack(fill=BOTH)
    frame1 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame1.pack(fill=BOTH, expand=True)
    frame2 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame2.pack(fill=BOTH, expand=True)
    frame3 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame3.pack(fill=BOTH, expand=True)
    frame4 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame4.pack(fill=BOTH, expand=True)
    frame5 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame5.pack(fill=BOTH, expand=True)
    frame6 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame6.pack(fill=BOTH, expand=True)
    frame7 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame7.pack(fill=BOTH, expand=True)
    frame8 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame8.pack(fill=BOTH, expand=True)
    frame9 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame9.pack(fill=BOTH, expand=True)
    frame10 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame10.pack(fill=BOTH, expand=True)
    frame11 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame11.pack(fill=BOTH, expand=True)
    frame12 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame12.pack(fill=BOTH, expand=True)
    frame13 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame13.pack(fill=BOTH, expand=True)
    frame14 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame14.pack(fill=BOTH, expand=True)
    frame15 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame15.pack(fill=BOTH, expand=True)
    frame16 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame16.pack(fill=BOTH, expand=True)
    frame17 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    frame17.pack(fill=BOTH, expand=True)

    lbl1 = Label(master=frame1, text="Адрес сервера сработок", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl1.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent1 = Entry(master=frame1, bg=Bg1)
    ent1.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl2 = Label(master=frame2, text="Адрес файла приема", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl2.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent2 = Entry(master=frame2, bg=Bg1)
    ent2.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl3 = Label(master=frame3, text="Адрес файла передачи", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl3.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent3 = Entry(master=frame3, bg=Bg1)
    ent3.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl4 = Label(master=frame4, text="Сервер контроля связи", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl4.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent4 = Entry(master=frame4, bg=Bg1)
    ent4.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl5 = Label(master=frame5, text="Рабочий сервер (адрес файла index.php)", padx=Padx, pady=Pady, bg=Bg, font=Font,
                 width=width)
    lbl5.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent5 = Entry(master=frame5, bg=Bg1)
    ent5.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl6 = Label(master=frame6, text="Резервный сервер", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl6.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent6 = Entry(master=frame6, bg=Bg1)
    ent6.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl7 = Label(master=frame7, text="Внешний IP и порт", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl7.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent7 = Entry(master=frame7, bg=Bg1)
    ent7.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl8 = Label(master=frame8, text="Name of value", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl8.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent8 = Entry(master=frame8, bg=Bg1)
    ent8.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl9 = Label(master=frame9, text="Name of value", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl9.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent9 = Entry(master=frame9, bg=Bg1)
    ent9.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl10 = Label(master=frame10, text="Name of value", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl10.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent10 = Entry(master=frame10, bg=Bg1)
    ent10.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl11 = Label(master=frame11, text="Name of value", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl11.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent11 = Entry(master=frame11, bg=Bg1)
    ent11.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl12 = Label(master=frame12, text="Name of value", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl12.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent12 = Entry(master=frame12, bg=Bg1)
    ent12.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl13 = Label(master=frame13, text="Name of value", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl13.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent13 = Entry(master=frame13, bg=Bg1)
    ent13.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl14 = Label(master=frame14, text="Name of value", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl14.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent14 = Entry(master=frame14, bg=Bg1)
    ent14.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl15 = Label(master=frame15, text="Папка логирования", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl15.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent15 = Entry(master=frame15, bg=Bg1)
    ent15.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl16 = Label(master=frame16, text="Папка логирования", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl16.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent16 = Entry(master=frame16, bg=Bg1)
    ent16.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
    lbl17 = Label(master=frame17, text="Папка логирования", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
    lbl17.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
    ent17 = Entry(master=frame17, bg=Bg1)
    ent17.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)

    frm_buttons = Frame(master=frame_frame)
    frm_buttons.pack(fill=X, ipadx=5, ipady=5)

    btn_submit = Button(master=frm_buttons, text="Сохранить", command=save_fields_to_file, font=Font)
    btn_submit.pack(side=RIGHT, padx=10, ipadx=10)

    btn_clear = Button(master=frm_buttons, text="Очистить", command=clear_fields, font=Font)
    btn_clear.pack(side=RIGHT, ipadx=10)

    ent1.focus()
    root.after(0, load_lines_from_file)

def delete_object():
    def deliting():
        if ent.get() == "":
            mbox.showerror("Ошибка", "Не введен пультовый номер!")
        else:

            mbox.showwarning("Удаление объекта из базы", "Вы точно хотите удалить объект из базы?\n Данную операцию "
                                                         "невозможно отменить!")
            mbox.showinfo("Удаление объекта из базы", "Удаление успешно завершено")

    gen = Frame(frame_four_frame)
    gen.pack(fill=BOTH, expand=True)

    frame_main_frame_alarm = Frame(master=gen, relief=GROOVE, width=400, height=60, borderwidth=5, bg='#0c47a6')
    frame_main_frame_alarm.pack()

    lab_name_of_alarm = Label(master=frame_main_frame_alarm, text="Пультовый номер объекта", width=22, font="Tahoma 12")

    ent = Entry(master=frame_main_frame_alarm, width=16, font="Tahoma 12")

    but = Button(frame_main_frame_alarm, text="Удалить", width=12, command=deliting)

    lab_name_of_alarm.pack(side=LEFT, padx=4, pady=4)
    but.pack(side=RIGHT, padx=4, pady=4)
    ent.pack(side=RIGHT, padx=4, pady=4)
    ent.focus()


def card_object_view(father, pult_number):
    win = Toplevel(father)
    win.title("Han Pult Карточка объекта " + str(pult_number))
    win.resizable(True, True)
    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)
    win.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))
    file = "Base/" + str(pult_number) + "/" + str(pult_number) + ".txt"
    print(file)

    cov_frame_main_frame = Frame(master=win, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    cov_frame_main_frame.pack(fill=BOTH, expand=True)

    cov_frame_center = Frame(master=cov_frame_main_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
    cov_frame_center.pack(fill=BOTH, expand=True)

    cov_frame_bottom = Frame(master=cov_frame_main_frame, relief=RAISED, borderwidth=2, bg='Gray')
    cov_frame_bottom.pack(fill=BOTH, padx=4, pady=4, side=BOTTOM)

    cov_frame_left = Frame(master=cov_frame_center, relief=RAISED, borderwidth=2, bg='Gray')
    cov_frame_left.pack(fill=BOTH, padx=4, pady=4, side=LEFT)

    cov_frame_right = Frame(cov_frame_center, relief=RAISED, borderwidth=2, bg='Gray')
    cov_frame_right.pack(fill=BOTH, padx=4, pady=4, side=RIGHT, expand=True)

    cov_lbl1 = Label(cov_frame_left, text="Пультовый номер\nНазвание\nХозорган\nАдрес\n\n\n\n\n\n\n\n\n\n", width=15,
                     font="Tahoma 12")
    cov_lbl1.grid(padx=4, pady=4, row=0)
    # txt1 = Text(cov_frame_right, font="Tahoma 12")
    # txt1.pack(fill=BOTH, padx=4, pady=4, expand=True)
    txl1 = Listbox(cov_frame_right,
                   font="Tahoma 12")  # Bad Listbox index!!! must be active, anchor. end. @x,y or a number???
    txl1.pack(fill=BOTH, padx=4, pady=4, expand=True)
    for i in fileinput.input(file):
        print(i)
        # txt1.insert(END, i)
        txl1.insert(END, i)

    cov_lbl1 = Label(cov_frame_bottom, text="Underground", width=16, height=5,
                     font="Tahoma 12")
    cov_lbl1.grid(padx=4, pady=4, row=0)
    # Доделать отображение фото при считывании из файла базы!


def about_developer():
    win = Toplevel(root)
    win.title("Han Pult О разработчике...")
    win.resizable(False, False)
    w = 300
    h = 200
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)
    win.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

    lab = Label(win, text=Variables.about_developer)
    lab.pack()


def license():
    win = Toplevel(root)
    win.title("Han Pult Лицензия")
    win.resizable(False, False)
    w = 400
    h = 200
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)
    win.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

    lab = Label(win, text=Variables.license_status)
    lab.pack()


def start_frame():  # Переключение фреймов на главном фрейме с выравниванием по всему фрейму и
    # привязкой к его размерам.
    frame_two_frame.place_forget()
    frame_three_frame.place_forget()
    frame_four_frame.place_forget()
    frame_five_frame.place_forget()
    frame_one_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
    print('def_start')


def frame_one(*event):
    frame_two_frame.place_forget()
    frame_three_frame.place_forget()
    frame_four_frame.place_forget()
    frame_five_frame.place_forget()
    frame_one_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
    print('def1')


def frame_two(*event):
    frame_one_frame.place_forget()
    frame_three_frame.place_forget()
    frame_four_frame.place_forget()
    frame_five_frame.place_forget()
    frame_two_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
    print('def2')


def frame_three(*event):
    frame_one_frame.place_forget()
    frame_two_frame.place_forget()
    frame_four_frame.place_forget()
    frame_five_frame.place_forget()
    frame_three_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
    print('def3')


def frame_four(*event):
    frame_one_frame.place_forget()
    frame_two_frame.place_forget()
    frame_three_frame.place_forget()
    frame_five_frame.place_forget()
    frame_four_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
    print('def4')


def frame_five(*event):
    frame_one_frame.place_forget()
    frame_two_frame.place_forget()
    frame_three_frame.place_forget()
    frame_four_frame.place_forget()
    frame_five_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
    print('def5')


def setwindow(root):
    root.title("HAN Pult")
    root.resizable(True, True)

    w = root.winfo_screenwidth() - 12
    h = root.winfo_screenheight() - 12

    x = 0
    y = 0
    # x = int(ws / 2 - w / 2)
    # y = int(wh / 2 - h / 2)
    # w = 1200
    # h = 700
    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))


root = Tk()

setwindow(root)
menubar = Menu(root)
root.config(menu=menubar)


fileMenu = Menu(menubar)
menubar.add_cascade(label="Система", menu=fileMenu)
fileMenu.add_command(label="Главное окно", command=run_active_alert)
fileMenu.add_command(label="Settings", command=run_settings)
fileMenu.add_command(label="Выход", command=exit)

baseMenu = Menu(menubar)
menubar.add_cascade(label="База", menu=baseMenu)
baseMenu.add_command(label="Каталог", command=run_catalog)

objectMenu = Menu(menubar)
menubar.add_cascade(label="Объект", menu=objectMenu)
objectMenu.add_command(label="Добавить", command=run_append)
objectMenu.add_command(label="Удалить", command=run_delete)

helpMenu = Menu(menubar)
menubar.add_cascade(label="Помощь", menu=helpMenu)
helpMenu.add_command(label="Краткая справка", command='')
helpMenu.add_command(label="Лицензия", command=license)
helpMenu.add_command(label="О разработчике", command=about_developer)

frame_main_frame = Frame(master=root, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame_main_frame.pack(fill=BOTH, expand=True)
frame_left = Frame(master=frame_main_frame, relief=RAISED, borderwidth=2, bg='Gray')
frame_left.pack(fill=BOTH, padx=4, pady=4, side=LEFT)

frame_right = Frame(master=frame_main_frame, relief=RAISED, borderwidth=2, bg='Gray')
frame_right.pack(fill=BOTH, padx=4, pady=4, side=RIGHT, expand=True)

lbl1 = Label(frame_left, text="Заголовок", width=10, font="Tahoma 14")
lbl1.grid(padx=5, pady=5, row=0)
btn1 = Button(frame_left, text="Button1", width=10, bg="Red", activebackground="Yellow", font="Tahoma 14",
              command="")
btn1.grid(padx=5, pady=5, row=1)
btn2 = Button(frame_left, text="Button1", width=10, bg="Green", activebackground="Yellow", font="Tahoma 14")
btn2.grid(padx=5, pady=5, row=2)
btn3 = Button(frame_left, text="Button1", width=10, bg="Red", activebackground="Yellow", font="Tahoma 14")
btn3.grid(padx=5, pady=5, row=3)
btn4 = Button(frame_left, text="Button1", width=10, bg="Green", activebackground="Yellow", font="Tahoma 14")
btn4.grid(padx=5, pady=5, row=4)
btn5 = Button(frame_left, text="Button1", width=10, bg="Green", activebackground="Yellow", font="Tahoma 14")
btn5.grid(padx=5, pady=5, row=5)
lbl1 = Label(frame_right, text="Активные сработки", height=1, font="Tahoma 14")
lbl1.pack(fill=BOTH, padx=4, pady=4)
window_frame = Frame(master=frame_right, relief=RAISED, borderwidth=2, bg='White')
window_frame.pack(fill=BOTH, padx=4, pady=4, expand=True)

frame_zero_frame = Frame(master=window_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame_zero_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
frame_one_frame = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_two_frame = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_three_frame = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_four_frame = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_five_frame = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')

# lbl_overview = Label(master=frame_two_frame, text='Frame 2', font="Tahoma 16", bg='#a4aaab')
# lbl_overview.pack()
# lbl_settings = Label(master=frame_three_frame, text='Frame 3', font="Tahoma 16", bg='#a4aaab')
# lbl_settings.pack()
# lbl_reserved = Label(master=frame_four_frame, text='Frame 4', font="Tahoma 16", bg='#a4aaab')
# lbl_reserved.pack()


l = ['94567, квартира. Харьков, Библика 19, 2 подъезд, 5 этаж, кв.47.; 28.03.2022, 14:57:06. Сработал объемник зала, '
     'ДРС окон зала.',
     '34895, Частный дом. Русские.Тишки, Центральная 53.; 28.03.2022, 15:29:49. СМК входной двери. объемник прихожей.']
lst = Listbox(master=frame_one_frame, selectmode=SINGLE, font="Tahoma 12")
scr = Scrollbar(master=frame_one_frame, command=lst.yview)
lst.configure(yscrollcommand=scr.set)
lst.bind("<<ListboxSelect>>", onSelect)
scr.pack(fill=BOTH, side=RIGHT)
lst.pack(fill=BOTH, padx=4, pady=4, expand=True)
for i in l:
    # z=(str(i[0]+i[1]))
    lst.insert(0, i)

th = Thread(target=Streams.start2, daemon=True)
th.start()

th1 = Thread(target=Streams.if_current_date_is_correct, daemon=True)
th1.start()

th2 = Thread(target=Streams.check_Server_sensor_connections, daemon=True)
th2.start()


root.after(0, start_frame)
root.mainloop()

# if __name__ == '__main__':
#     run_anyway()
