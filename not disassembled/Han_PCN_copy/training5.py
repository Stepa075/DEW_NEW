import datetime
from tkinter import *
# Значение: datetime.datetime(2017, 4, 5, 0, 18, 51, 980187)
from time import sleep

from timer_from_specoper import variables

year = 2022
month = 2
day = 24
ostatok_hour = 23 - 4
ostatok_minutes = 59 - 0
ostatok_seconds = 59 - 0

def podschet():
    year = 2022
    month = 2
    day = 24
    ostatok_hour = 23 - 4
    ostatok_minutes = 59 - 0
    ostatok_seconds = 59 - 0

    then = datetime.datetime(year, month, day, ostatok_hour, ostatok_minutes, ostatok_seconds)

    while True:
        now = datetime.datetime.now()
        delta = now - then
        print("days: " + str(delta.days))
        hours = delta.seconds // 3600

        print("hours:" + str(hours))  # 186.0
        minutes = (delta.seconds % 3600) // 60
        print("minutes: " + str(minutes))  # 13.0
        seconds = (delta.seconds - ((hours * 3600) + (minutes * 60)))
        print("seconds: " + str(seconds))
        itog = "days: " + str(delta.days) + "\n" + "hours:" + str(hours) + "\n" + "minutes: " + str(minutes) + "\n" + "seconds: " + str(seconds)
        variables.value = itog
        print(itog)
        sleep(1.0)


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

root_main.bind("<Return>", podschet)
root_main.bind("<Up>", "")
root_main.bind("<Down>", "")

root_main.mainloop()
