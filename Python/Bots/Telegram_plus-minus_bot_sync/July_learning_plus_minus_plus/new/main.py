import random
from random import randint
from tkinter import *
from tkinter.messagebox import showerror

import Variables

root = Tk()


root.title("Python plus-minus-2 by Stepa075")
root.geometry('487x117')
root.resizable(False, False)
f1 = LabelFrame(root, text='Число 1')
f2 = LabelFrame(root, text='Знак')
f4 = LabelFrame(root, text='Число 2')
f7 = LabelFrame(root, text='Знак')
f8 = LabelFrame(root, text='Число 3')
f3 = LabelFrame(root, text='Ответ')
f5 = LabelFrame(root, text='Ответов правильно')
f6 = LabelFrame(root, text='Ответов неправильно')


def start():
    value_a, value_b, value_c, ri1, ri2, ri3 = change_primer()
    number1['text'] = value_a
    number2['text'] = value_b
    number3['text'] = value_c
    hours2['text'] = ri3
    hours1['text'] = ri2
    Variables.answer = ri1

def control_int(event):

        getNumber = entry.get()
        if getNumber.isdigit():
            getNumber02(getNumber)


        else:
            entry.delete(0, END)
            showerror(
                "Ошибка",
                "Должно быть введено число!")


def getNumber02(value):
    # while True:
    getNumber = value #int(entry.get())
    print(entry.get())
    if str(Variables.answer) == getNumber:
        Variables.true = Variables.true+1
        hours3['text'] = Variables.true
        start()
    else:
        Variables.false = Variables.false + 1
        hours4['text'] = Variables.false
        print("Fuck!!!")
        start()
    entry.delete(0, END)



def change_primer():
    while True:
        value_a = randint(1, 20)
        value_b = randint(1, 20)
        value_c = randint(1, 20)

        sign = [[value_a + value_b + value_c, '+', '+'], [value_a - value_b - value_c, '-', '-'], [value_a + value_b - value_c, '+', '-'], [value_a - value_b + value_c, '-', '+']]
        random_index = random.choice(sign)
        if int(random_index[0]) > 0:
            if random_index[1] == '-':
                if (value_a-value_b)>value_c:
                    break
                else:
                   continue
            else:
                break
    return value_a, value_b, value_c, random_index[0], random_index[1], random_index[2]


# def podschet():
#     answer = getNumber02()
#     value_c = random_index[0]
#
#     if str(value_c) == answer:
#         print("Правильно, молодец!")
#         true = true + 1
#     else:
#         print("Неправильно, будь внимательнее!")
#         false = false + 1
#     print('Правильно: ' + str(true) + ' Неправильно: ' + str(false))
#     print('Всего вопросов: ' + str(true + false))


# def circle_request():
#     # Variables.h = spin_hour.get()
#     # Variables.m = spin_min.get()
#     # Variables.s = spin_sec.get()
#     # print('Time variables= ' + str(Variables.h) + ' ' +  str(Variables.m) + ' ' +  str(Variables.s))
#     # Variables.sound = check_cb.get()
#     # print('cb_sound ' + str(check_cb.get()))
#     # Variables.input_combo_box = combo_box.current()
#     # print('combo_box ' + str(combo_box.get()))
#     root.after(1000, circle_request)
#

number1 = Label(f1, text='  1', font=("Arial Bold", 12), width=4)
hours1 = Label(f2, text=' +- ', font=("Arial Bold", 12), width=4)
number2 = Label(f4, text='  2', font=("Arial Bold", 12), width=4)
hours2 = Label(f7, text=' +- ', font=("Arial Bold", 12), width=4)
number3 = Label(f8, text='  1', font=("Arial Bold", 12), width=4)
entry = Entry(f3, font=("Arial Bold", 12), width=7)
hours3 = Label(f5, text=' 0', font=("Arial Bold", 12), bg='#228B22')
hours4 = Label(f6, text=' 0', font=("Arial Bold", 12), bg='#FF0000')
button1 = Button(f3, text='Ответить', width=10, font=("Arial Bold", 11))  # command=Variables.about
button1.bind('<Button-1>', control_int)
entry.bind('<Return>', control_int)

f1.grid(column=0, row=0, sticky=N + S + E + W, padx=2, pady=2)
f2.grid(column=1, row=0, sticky=N + S + E + W, padx=2, pady=2)
f4.grid(column=2, row=0, sticky=N + S + E + W, padx=2, pady=2)
f3.grid(column=5, row=0, sticky=N + S + E + W, padx=2, pady=2)
f5.grid(column=0, columnspan=2, row=2, sticky=N + S + E + W, padx=2, pady=2)
f6.grid(column=2, columnspan=3, row=2, sticky=N + S + E + W, padx=2, pady=2)
f7.grid(column=3, row=0, sticky=N + S + E + W, padx=2, pady=2)
f8.grid(column=4, row=0, sticky=N + S + E + W, padx=2, pady=2)
number1.grid(column=1, row=0)
hours1.grid(column=1, row=0)
number2.grid(column=1, row=0)
hours2.grid(column=1, row=0)
number3.grid(column=1, row=0)
hours3.grid(column=1, row=0)
hours4.grid(column=1, row=0)
entry.grid(column=1, row=0, sticky=N + S + W + E, padx=3, pady=6)
entry.focus()

button1.grid(column=2, row=0, sticky=N + S + W + E, padx=3, pady=6)

root.after(0, start)
# root.after(0, set_timer)
root.mainloop()
