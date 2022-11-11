from tkinter import *


def start_frame():  # Переключение фреймов на главном фрейме с выравниванием по всему фрейму и
    # привязкой к его размерам.
    frame_two_frame.place_forget()
    frame_three_frame.place_forget()
    frame_four_frame.place_forget()
    frame_one_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
    print('def_start')


def general_menu(*event):
    frame_two_frame.place_forget()
    frame_three_frame.place_forget()
    frame_four_frame.place_forget()
    frame_one_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
    print('def1')


def overview(*event):
    frame_one_frame.place_forget()
    frame_three_frame.place_forget()
    frame_four_frame.place_forget()
    frame_two_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
    print('def2')


def settings(*event):
    frame_one_frame.place_forget()
    frame_two_frame.place_forget()
    frame_four_frame.place_forget()
    frame_three_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
    print('def3')


def reserved(*event):
    frame_one_frame.place_forget()
    frame_two_frame.place_forget()
    frame_three_frame.place_forget()
    frame_four_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
    print('def4')


def setwindow(root):
    root.title("Окно программы")
    root.resizable(False, False)

    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))


root = Tk()
setwindow(root)

root.resizable(True, True)

frame_main_frame = Frame(master=root, relief=GROOVE, borderwidth=5, bg='#0c47a6')

frame_one_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_two_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_three_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_four_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')

lbl_general = Label(master=frame_one_frame, text='General', font="Tahoma 16", bg='#a4aaab')
lbl_general.pack()
lbl_overview = Label(master=frame_two_frame, text='Overview', font="Tahoma 16", bg='#a4aaab')
lbl_overview.pack()
lbl_settings = Label(master=frame_three_frame, text='Settings', font="Tahoma 16", bg='#a4aaab')
lbl_settings.pack()
lbl_reserved = Label(master=frame_four_frame, text='Reserved', font="Tahoma 16", bg='#a4aaab')
lbl_reserved.pack()

button1 = Button(master=frame_main_frame, text="General", command=general_menu, bg="#adb2b8", fg="Black", font="Tahoma 14")
button2 = Button(master=frame_main_frame, text="Overview", command=overview, bg="#adb2b8", fg="Black", font="Tahoma 14")
button3 = Button(master=frame_main_frame, text="Settings", command=settings, bg="#adb2b8", fg="Black", font="Tahoma 14")
button4 = Button(master=frame_main_frame, text="Reserved", command=reserved, bg="#adb2b8", fg="Black", font="Tahoma 14")

frame_main_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")

button1.place(x=10, y=13, width=130, height=40)
button2.place(x=10, y=63, width=130, height=40)
button3.place(x=10, y=113, width=130, height=40)
button4.place(x=10, y=163, width=130, height=40)

root.after(0, start_frame)

root.title('Control panel')

root.mainloop()
