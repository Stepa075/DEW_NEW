from tkinter import *

Padx = 0
Pady = 0
Ipadx = 0
Ipady = 0
Bg = "Grey"
Bg1 = "White"


def setwindow(root):
    root.title("Окно программы")
    root.resizable(False, False)

    # w = 800
    # h = 500
    # ws = root.winfo_screenwidth()
    # wh = root.winfo_screenheight()
    #
    # x = int(ws / 2 - w / 2)
    # y = int(wh / 2 - h / 2)

    # root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))


root = Tk()
setwindow(root)

root.resizable(True, True)
root.title('Testing')


frame_zero_frame = Frame(master=root, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame_zero_frame.pack(fill=BOTH, expand=True)
frame1 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame1.pack(fill=BOTH)
frame2 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame2.pack(fill=BOTH)
frame3 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame3.pack(fill=BOTH)
frame4 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame4.pack(fill=BOTH)
frame5 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame5.pack(fill=BOTH)
frame6 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame6.pack(fill=BOTH)
frame7 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame7.pack(fill=BOTH)
frame8 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame8.pack(fill=BOTH)
frame9 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame9.pack(fill=BOTH)
frame10 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame10.pack(fill=BOTH)
frame11 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame11.pack(fill=BOTH)
frame12 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame12.pack(fill=BOTH)
frame13 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame13.pack(fill=BOTH)
frame14 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame14.pack(fill=BOTH)
frame15 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame15.pack(fill=BOTH)
frame16 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame16.pack(fill=BOTH)
frame17 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame17.pack(fill=BOTH)
frame18 = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame18.pack(fill=BOTH)
lbl1 = Label(master=frame1, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl1.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent1 = Entry(master=frame1, bg=Bg1)
ent1.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl2 = Label(master=frame2, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl2.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent2 = Entry(master=frame2, bg=Bg1)
ent2.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl3 = Label(master=frame3, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl3.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent3 = Entry(master=frame3, bg=Bg1)
ent3.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl4 = Label(master=frame4, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl4.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent4 = Entry(master=frame4, bg=Bg1)
ent4.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl5 = Label(master=frame5, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl5.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent5 = Entry(master=frame5, bg=Bg1)
ent5.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl6 = Label(master=frame6, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl6.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent6 = Entry(master=frame6, bg=Bg1)
ent6.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl7 = Label(master=frame7, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl7.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent7 = Entry(master=frame7, bg=Bg1)
ent7.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl8 = Label(master=frame8, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl8.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent8 = Entry(master=frame8, bg=Bg1)
ent8.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl9 = Label(master=frame9, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl9.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent9 = Entry(master=frame9, bg=Bg1)
ent9.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl10 = Label(master=frame10, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl10.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent10 = Entry(master=frame10, bg=Bg1)
ent10.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl11 = Label(master=frame11, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl11.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent11 = Entry(master=frame11, bg=Bg1)
ent11.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl12 = Label(master=frame12, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl12.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent12 = Entry(master=frame12, bg=Bg1)
ent12.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl7 = Label(master=frame13, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl7.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent7 = Entry(master=frame13, bg=Bg1)
ent7.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl8 = Label(master=frame14, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl8.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent8 = Entry(master=frame14, bg=Bg1)
ent8.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl9 = Label(master=frame15, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl9.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent9 = Entry(master=frame15, bg=Bg1)
ent9.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl10 = Label(master=frame16, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl10.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent10 = Entry(master=frame16, bg=Bg1)
ent10.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl11 = Label(master=frame17, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl11.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent11 = Entry(master=frame17, bg=Bg1)
ent11.pack(fill=BOTH, padx=Padx, pady=Pady)
lbl12 = Label(master=frame18, text="Name of value", padx=Padx, pady=Pady, bg=Bg)
lbl12.pack(side=LEFT, ipadx=Ipadx, ipady=Ipady)
ent12 = Entry(master=frame18, bg=Bg1)
ent12.pack(fill=BOTH, padx=Padx, pady=Pady)


frm_buttons = Frame(master=frame_zero_frame)
frm_buttons.pack(fill=X, ipadx=5, ipady=5)

# Создает кнопку "Отправить" и размещает ее
# справа от рамки `frm_buttons`.
btn_submit = Button(master=frm_buttons, text="Отправить")
btn_submit.pack(side=RIGHT, padx=10, ipadx=10)

# Создает кнопку "Очистить" и размещает ее
# справа от рамки `frm_buttons`.
btn_clear = Button(master=frm_buttons, text="Очистить")
btn_clear.pack(side=RIGHT, ipadx=10)

# Запуск приложения.


root.mainloop()
