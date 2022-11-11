import random
from random import randint

import Variables


def start():
    value_a, value_b, value_c, ri1, ri2, ri3 = change_primer()
    chislo1 = value_a
    chislo2 = value_b
    chislo3 = value_c
    znak1 = ri2
    znak2 = ri3
    primer = str(chislo1) + str(znak1) + str(chislo2) + str(znak2) + str(chislo3)
    otvet = ri1
    Variables.answer = ri1
    return primer, otvet


def change_primer():
    while True:
        value_a = randint(1, 20)
        value_b = randint(1, 20)
        value_c = randint(1, 20)
        sign = [[value_a + value_b + value_c, '+', '+'], [value_a - value_b - value_c, '-', '-'],
                [value_a + value_b - value_c, '+', '-'], [value_a - value_b + value_c, '-', '+']]
        random_index = random.choice(sign)
        if int(random_index[0]) > 0:
            break
    return value_a, value_b, value_c, random_index[0], random_index[1], random_index[2]


def control_int(value):
    global a, isdigit
    try:
        a = int(value)
        isdigit = True
    except:
        isdigit = False


    return isdigit
