from random import randint
import random
import Variables


def start():
    value_a, value_b, value_c, ri1, ri2, ri3 = change_primer()
    Variables.value_a = value_a
    Variables.value_b = value_b
    Variables.value_c = value_c
    Variables.znak1 = ri2
    Variables.znak2 = ri3
    Variables.answer = ri1

def change_primer():
    while True:
        value_a = randint(1, 20)
        value_b = randint(1, 20)
        value_c = randint(1, 20)
        sign = [[value_a + value_b + value_c, '+', '+'], [value_a - value_b - value_c, '-', '-'], [value_a + value_b - value_c, '+', '-'], [value_a - value_b + value_c, '-', '+']]
        random_index = random.choice(sign)
        if int(random_index[0]) > 0:
            break

    return value_a, value_b, value_c, random_index[0], random_index[1], random_index[2]

