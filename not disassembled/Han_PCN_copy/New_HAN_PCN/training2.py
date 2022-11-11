from tkinter import *


def start_frame():  # Переключение фреймов на главном фрейме с выравниванием по всему фрейму и
    # привязкой к его размерам.
    frame_two_frame.place_forget()
    frame_three_frame.place_forget()
    frame_four_frame.place_forget()
    frame_one_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
    print('def_start')


def frame_one(*event):
    frame_two_frame.place_forget()
    frame_three_frame.place_forget()
    frame_four_frame.place_forget()
    frame_one_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
    print('def1')


def frame_two(*event):
    frame_one_frame.place_forget()
    frame_three_frame.place_forget()
    frame_four_frame.place_forget()
    frame_two_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
    print('def2')


def frame_three(*event):
    frame_one_frame.place_forget()
    frame_two_frame.place_forget()
    frame_four_frame.place_forget()
    frame_three_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
    print('def3')


def frame_four(*event):
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

frame_zero_frame = Frame(master=root, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame_zero_frame.place(relx=0, rely=0, relwidth=1.0, relheight=1.0, anchor="nw")
frame_one_frame = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_two_frame = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_three_frame = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_four_frame = Frame(master=frame_zero_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')

lbl_general = Label(master=frame_one_frame, text='Frame 1', font="Tahoma 16", bg='#a4aaab')
lbl_general.pack()
lbl_overview = Label(master=frame_two_frame, text='Frame 2', font="Tahoma 16", bg='#a4aaab')
lbl_overview.pack()
lbl_settings = Label(master=frame_three_frame, text='Frame 3', font="Tahoma 16", bg='#a4aaab')
lbl_settings.pack()
lbl_reserved = Label(master=frame_four_frame, text='Frame 4', font="Tahoma 16", bg='#a4aaab')
lbl_reserved.pack()

button1 = Button(master=frame_zero_frame, text="General", command=frame_one, bg="#adb2b8", fg="Black", font="Tahoma 14")
button2 = Button(master=frame_zero_frame, text="Overview", command=frame_two, bg="#adb2b8", fg="Black", font="Tahoma 14")
button3 = Button(master=frame_zero_frame, text="Settings", command=frame_three, bg="#adb2b8", fg="Black", font="Tahoma 14")
button4 = Button(master=frame_zero_frame, text="Reserved", command=frame_four, bg="#adb2b8", fg="Black", font="Tahoma 14")



button1.place(x=10, y=13, width=130, height=40)
button2.place(x=10, y=63, width=130, height=40)
button3.place(x=10, y=113, width=130, height=40)
button4.place(x=10, y=163, width=130, height=40)

root.after(0, start_frame)

root.title('Control panel')

root.mainloop()
