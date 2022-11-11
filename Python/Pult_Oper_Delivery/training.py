# import os
# from tkinter import *
# from tkinter import messagebox as mbox
#
# from Pult_Oper_Delivery import Variables
#
#
# def setwindow(root):
#     root.title("HAN Pult")
#     root.resizable(True, True)
#
#     w = root.winfo_screenwidth() - 12
#     h = root.winfo_screenheight() - 12
#
#     x = 0
#     y = 0
#     # x = int(ws / 2 - w / 2)
#     # y = int(wh / 2 - h / 2)
#     # w = 1200
#     # h = 700
#     root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))
#
#
# root = Tk()
#
# setwindow(root)
#
# Padx = 0
# Pady = 0
# Ipadx = 0
# Ipady = 0
# Bg = "#e8e6e7"
# Bg1 = "White"
# Font = "Tahoma 12"
# width = 35
#
#
# def clear_fields():
#     ent1.delete(0, END)
#     ent2.delete(0, END)
#     ent3.delete(0, END)
#     ent4.delete(0, END)
#     ent5.delete(0, END)
#     ent6.delete(0, END)
#     ent7.delete(0, END)
#     ent8.delete(0, END)
#     ent9.delete(0, END)
#     ent10.delete(0, END)
#     ent11.delete(0, END)
#     ent12.delete(0, END)
#     ent13.delete(0, END)
#     ent14.delete(0, END)
#     ent15.delete(0, END)
#     ent16.delete(0, END)
#     ent17.delete(0, END)
#
# def load_lines_from_file():
#     directory = "bin/"
#     list_of_lines = []
#     f = open(directory + "settings.ini", 'r')
#     for line in f:
#         list_of_lines.append(line)
#     f.close()
#     print(list_of_lines)
#     ent1.insert(0, list_of_lines[0])
#     ent2.insert(0, list_of_lines[1])
#     ent3.insert(0, list_of_lines[2])
#     ent4.insert(0, list_of_lines[3])
#     ent5.insert(0, list_of_lines[4])
#     ent6.insert(0, list_of_lines[5])
#     ent7.insert(0, list_of_lines[6])
#     ent8.insert(0, list_of_lines[7])
#     ent9.insert(0, list_of_lines[8])
#     ent10.insert(0, list_of_lines[9])
#     ent11.insert(0, list_of_lines[10])
#     ent12.insert(0, list_of_lines[11])
#     ent13.insert(0, list_of_lines[12])
#     ent14.insert(0, list_of_lines[13])
#     ent15.insert(0, list_of_lines[14])
#     ent16.insert(0, list_of_lines[15])
#     ent17.insert(0, list_of_lines[16])
# def save_fields_to_file():
#     list_add = [ent1.get(), ent2.get(), ent3.get(), ent4.get(), ent5.get(), ent6.get(), ent7.get(),
#                 ent8.get(), ent9.get(), ent10.get(), ent11.get(), ent12.get(), ent13.get(), ent14.get(), ent15.get(),
#                 ent16.get(), ent17.get()]
#     print(list_add)
#
#     directory = "bin/"
#
#     f = open(directory + "settings.ini", 'w')
#     for e in list_add:
#         f.write(e)
#     f.close()
#
#
# frame_frame = Frame(master=root, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame_frame.pack(fill=BOTH)
# frame1 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame1.pack(fill=BOTH, expand=True)
# frame2 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame2.pack(fill=BOTH, expand=True)
# frame3 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame3.pack(fill=BOTH, expand=True)
# frame4 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame4.pack(fill=BOTH, expand=True)
# frame5 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame5.pack(fill=BOTH, expand=True)
# frame6 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame6.pack(fill=BOTH, expand=True)
# frame7 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame7.pack(fill=BOTH, expand=True)
# frame8 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame8.pack(fill=BOTH, expand=True)
# frame9 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame9.pack(fill=BOTH, expand=True)
# frame10 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame10.pack(fill=BOTH, expand=True)
# frame11 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame11.pack(fill=BOTH, expand=True)
# frame12 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame12.pack(fill=BOTH, expand=True)
# frame13 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame13.pack(fill=BOTH, expand=True)
# frame14 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame14.pack(fill=BOTH, expand=True)
# frame15 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame15.pack(fill=BOTH, expand=True)
# frame16 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame16.pack(fill=BOTH, expand=True)
# frame17 = Frame(master=frame_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
# frame17.pack(fill=BOTH, expand=True)
#
# lbl1 = Label(master=frame1, text="Адрес сервера сработок", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl1.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent1 = Entry(master=frame1, bg=Bg1)
# ent1.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl2 = Label(master=frame2, text="Адрес файла приема", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl2.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent2 = Entry(master=frame2, bg=Bg1)
# ent2.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl3 = Label(master=frame3, text="Адрес файла передачи", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl3.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent3 = Entry(master=frame3, bg=Bg1)
# ent3.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl4 = Label(master=frame4, text="Сервер контроля связи", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl4.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent4 = Entry(master=frame4, bg=Bg1)
# ent4.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl5 = Label(master=frame5, text="Рабочий сервер (адрес файла index.php)", padx=Padx, pady=Pady, bg=Bg, font=Font,
#              width=width)
# lbl5.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent5 = Entry(master=frame5, bg=Bg1)
# ent5.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl6 = Label(master=frame6, text="Резервный сервер", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl6.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent6 = Entry(master=frame6, bg=Bg1)
# ent6.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl7 = Label(master=frame7, text="Внешний IP и порт", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl7.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent7 = Entry(master=frame7, bg=Bg1)
# ent7.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl8 = Label(master=frame8, text="Name of value", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl8.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent8 = Entry(master=frame8, bg=Bg1)
# ent8.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl9 = Label(master=frame9, text="Name of value", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl9.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent9 = Entry(master=frame9, bg=Bg1)
# ent9.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl10 = Label(master=frame10, text="Name of value", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl10.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent10 = Entry(master=frame10, bg=Bg1)
# ent10.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl11 = Label(master=frame11, text="Name of value", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl11.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent11 = Entry(master=frame11, bg=Bg1)
# ent11.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl12 = Label(master=frame12, text="Name of value", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl12.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent12 = Entry(master=frame12, bg=Bg1)
# ent12.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl13 = Label(master=frame13, text="Name of value", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl13.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent13 = Entry(master=frame13, bg=Bg1)
# ent13.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl14 = Label(master=frame14, text="Name of value", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl14.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent14 = Entry(master=frame14, bg=Bg1)
# ent14.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl15 = Label(master=frame15, text="Папка логирования", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl15.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent15 = Entry(master=frame15, bg=Bg1)
# ent15.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl16 = Label(master=frame16, text="Папка логирования", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl16.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent16 = Entry(master=frame16, bg=Bg1)
# ent16.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
# lbl17 = Label(master=frame17, text="Папка логирования", padx=Padx, pady=Pady, bg=Bg, font=Font, width=width)
# lbl17.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
# ent17 = Entry(master=frame17, bg=Bg1)
# ent17.pack(fill=BOTH, padx=Padx, pady=Pady, expand=True)
#
# frm_buttons = Frame(master=frame_frame)
# frm_buttons.pack(fill=X, ipadx=5, ipady=5)
#
# btn_submit = Button(master=frm_buttons, text="Сохранить", command=save_fields_to_file, font=Font)
# btn_submit.pack(side=RIGHT, padx=10, ipadx=10)
#
# btn_clear = Button(master=frm_buttons, text="Очистить", command=clear_fields, font=Font)
# btn_clear.pack(side=RIGHT, ipadx=10)
#
# ent1.focus()
# root.after(0, load_lines_from_file)
# root.mainloop()
