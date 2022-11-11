import time
from tkinter import messagebox as mbox
from tkinter import *
import os
import Variables


def update_time():
    Time = time.strftime('%Y-%m-%d %H:%M:%S')
    return str(Time)


def update_time_for_writing_files():
    Time = time.strftime('%Y-%m-%d_%H.%M.%S')
    return str(Time)


def date_for_session():
    Variables.date_current = str(time.strftime('%Y.%m.%d'))
    Variables.date_for_session = str(time.strftime('%Y.%m.%d'))
    print("date_for_session(): " + Variables.date_current)
    # date_plus_one = int(time.strftime('%d')) + 1
    # date_end_session = time.strftime('%Y.%m.') + str(date_plus_one)
    # print(date_start_session + "-" + date_end_session)


def create_directorys_and_files():
    logging_session("Start a new file.", 'bin/logging/' + str(Variables.date_current) + '_session.txt')
    time.sleep(0.5)
    logging_session("Start a new file.", 'bin/logging/' + str(Variables.date_current) + '_alerts.txt')
    time.sleep(0.5)
    logging_session("Start a new file.", 'bin/logging/' + str(Variables.date_current) + '_logs.txt')

    try:

        os.makedirs('bin/logging/alerts')


    except:
        pass


def loading_settings_from_file():
    list_of_settings = []
    with open("bin/settings.ini") as f:
        for line in f:
            list_of_settings.append(line.rstrip("\n"))
    print(list_of_settings)


def autorization_user(log, pas):  # log, pas
    login = False
    line1 = []
    lines_log = []
    lines_pas = []
    if os.path.exists('bin/passwords.txt'):
        print("Ok! File is here!")
        i = 0
        with open("bin/passwords.txt") as f:
            for line in f:
                line1.append(line.rstrip("\n"))  # Для удаления символа переноса строки нужно использовать rstrip(
                # "\n")!!!
                xxx = str(line1[i])
                zzz = xxx[: xxx.find(",")]  # Первое значение в ячейке списка до запятой!
                xzxz = xxx[xxx.find(",") + 2:]  # Второе значение в ячейке списка после запятой, плюс один пробел
                # после нее!
                # print(zzz)
                # print(xzxz)
                lines_log.append(str(zzz))
                lines_pas.append(str(xzxz))
                i += 1

        xxx = str(line1[0])
        zzz = xxx[: xxx.find(",")]  # Первое значение в ячейке списка до запятой!
        xzxz = xxx[
               xxx.find(",") + 2:]  # Второе значение в ячейке списка после запятой, плюс один пробел после нее!

        n = 0
        for i in range(len(lines_log)):
            print(i)
            print(lines_log[n])
            if log in lines_log[n]:
                print("login is good!")
                break
            else:
                print("FUCKING log!!!")
            n += 1
        try:
            if pas == lines_pas[n]:
                print("pass is good and compare with login!")
                login = True
            else:
                print("password is wrong!")
                login = False
        except IndexError:
            login = False

        f.close()
    else:
        os.mkdir("bin")
        f = open('bin/passwords.txt', 'w')
        f.write(str(Variables.autorization_first_time))
        f.close()
    line1.clear()
    lines_log.clear()
    lines_pas.clear()
    return login


def run_anyway():
    date_for_session()
    create_directorys_and_files()
    import main_New_GUI
    main_New_GUI.root.mainloop()


def logging_session(events, place):
    if os.path.exists(place):  # доделать создание файла (при открытии сессии) и закрытие его
        # при закрытии сессии. проверку на созданный файл с текущей датой (при перезапуске программы)!
        f = open(place, "a")
        f.write(update_time() + ". " + events + "\n")
        f.close()
        print("Ok! Logging is done!")
    else:
        try:
            os.mkdir("bin/logging")
        except:
            pass
        f = open(place, "w")
        f.write(update_time() + ". " + events + "\n")
        f.close()
        print("Ok! Directory created. Logging is done!")


def logging_alerts():
    if os.path.exists('bin/logging/alerts.txt'):
        print("Ok! File is here!")
    pass


def logging_logs():
    if os.path.exists('bin/logging/logs.txt'):
        print("Ok! File is here!")
    pass


def writing_alert(time_for_start_allert, listing, name_of_allert):
    # if os.path.exists("bin/logging/alerts/" + str(time_for_start_allert) + str(name_of_allert)):
    #     f = open("bin/logging/alerts/" + str(time_for_start_allert) + str(name_of_allert) + ".txt", "w")
    #     f.write(listing + "\n")
    #     f.close()
    #     print("Ok! File alerts" + str(name_of_allert) + "is created!")
    # else:
    try:
        os.mkdir("bin/logging/alerts/" + Variables.date_for_session)  # + str(time_for_start_allert) + "_" + str(
        # name_of_allert)
    except:
        pass  # Writing message about wrong writing to file!!!
    f = open("bin/logging/alerts/" + Variables.date_for_session + "/" +
             str(time_for_start_allert) + "_" + str(name_of_allert) + ".txt", "w", encoding="Utf-8")
    # f.decoding = "UTF-8"
    for e in listing:
        f.write(e + "\n")
    f.close()
    print("Ok! Allert " + str(name_of_allert) + " is writing!")
