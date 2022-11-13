from tkinter import *

root = Tk()

root.title("My notes")
root.geometry('300x155-0-40')
root.resizable(True, True)
root.minsize(300, 100)
f_top = Frame(root)
f_bot = Frame(root)
f_top.pack()
f_bot.pack()
entry = Text(f_top, font=("Arial Bold", 12), height=4, ).pack(expand=True)
entry1 = Text(f_bot,font=("Arial Bold", 12), height=4).pack(expand=True)



root.mainloop()