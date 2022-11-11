import ctypes
import time
from ctypes import wintypes
from threading import Thread
from tkinter import *
import requests

import Variables
import gc



def start_frame():
    frame_tumblers1_frame.place_forget()
    frame_tumblers2_frame.place_forget()
    frame_tumblers3_frame.place_forget()
    frame_tumblers_frame.place(x=18, y=225, width=765, height=355)
    print('def_start')


def general_menu(*event):
    frame_tumblers1_frame.place_forget()
    frame_tumblers2_frame.place_forget()
    frame_tumblers3_frame.place_forget()
    frame_tumblers_frame.place(x=18, y=225, width=765, height=355)
    print('def1')


def overview(*event):
    frame_tumblers_frame.place_forget()
    frame_tumblers2_frame.place_forget()
    frame_tumblers3_frame.place_forget()
    frame_tumblers1_frame.place(x=18, y=225, width=765, height=355)
    print('def2')


def settings(*event):
    frame_tumblers_frame.place_forget()
    frame_tumblers1_frame.place_forget()
    frame_tumblers3_frame.place_forget()
    frame_tumblers2_frame.place(x=18, y=225, width=765, height=355)
    print('def3')


def reserved(*event):
    frame_tumblers_frame.place_forget()
    frame_tumblers1_frame.place_forget()
    frame_tumblers2_frame.place_forget()
    frame_tumblers3_frame.place(x=18, y=225, width=765, height=355)
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


def check_Power():
    class SYSTEM_POWER_STATUS(ctypes.Structure):
        _fields_ = [
            ('ACLineStatus', wintypes.BYTE),
            ('BatteryFlag', wintypes.BYTE),
            ('BatteryLifePercent', wintypes.BYTE),
            ('Reserved1', wintypes.BYTE),
            ('BatteryLifeTime', wintypes.DWORD),
            ('BatteryFullLifeTime', wintypes.DWORD),
        ]

    SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)

    GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
    GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
    GetSystemPowerStatus.restype = wintypes.BOOL

    status = SYSTEM_POWER_STATUS()
    if not GetSystemPowerStatus(ctypes.pointer(status)):
        raise ctypes.WinError()
    if status.ACLineStatus != 0:
        # print('Power Ok!')
        lbl_Power_sensor['text'] = 'Power sensor status: AC power connected, Ok'
    else:
        # print('No Power')
        lbl_Power_sensor['text'] = 'Power sensor status: AC power lost, Battery mode!'
    # print('ACLineStatus', status.ACLineStatus)
    # print('BatteryFlag', status.BatteryFlag)
    # print('BatteryLifePercent', status.BatteryLifePercent)
    # print('BatteryLifeTime', status.BatteryLifeTime)
    # print('BatteryFullLifeTime', status.BatteryFullLifeTime)
    root.after(30000, check_Power)


# def xxx():
#     try:
#         xxx1 = Variables.parsing_ESP
#         lbl_gen_fr_1_value['text'] = xxx1
#         lbl_gen_fr_2_value['text'] = xxx1
#         del xxx1
#         print('xxx')
#         gc.collect()
#         # root.after(3000, xxx)
#     except:
#         lbl_gen_fr_1_value['text'] = 'Fucking ERROR!!!'
#         pass
#         gc.collect()
        # root.after(3000, xxx)


# def parser_GPIO_sadok():
#     try:
#
#             xxx1 = Variables.Sadok_Light
#
#             if int(xxx1) == 0:
#                 lbl_gen_fr3_1_value['text'] = 'ON'
#             else:
#                 lbl_gen_fr3_1_value['text'] = "OFF"
#             del xxx1
#             print('parser_GPIO_sadok')
#     except:
#         lbl_gen_fr3_1_value['text'] = 'No connect to ESP!'
#         pass
#     gc.collect()
    # root.after(3000, parser_GPIO_sadok)


# def parser_GPIO_4relay():
#     try:
#             if int(Variables.parsing_GPIO_4relay_0) != 0:
#                 lbl_gen_fr3_3_value['text'] = 'ON'
#             else:
#                 lbl_gen_fr3_3_value['text'] = "OFF"
#             if int(Variables.parsing_GPIO_4relay_1) != 0:
#                 lbl_gen_fr3_4_value['text'] = 'ON'
#             else:
#                 lbl_gen_fr3_4_value['text'] = "OFF"
#             if int(Variables.parsing_GPIO_4relay_2) != 0:
#                 lbl_gen_fr3_5_value['text'] = 'ON'
#             else:
#                 lbl_gen_fr3_5_value['text'] = "OFF"
#             if int(Variables.parsing_GPIO_4relay_3) != 0:
#                 lbl_gen_fr3_6_value['text'] = 'ON'
#             else:
#                 lbl_gen_fr3_6_value['text'] = "OFF"
#             print('parser_GPIO_4relay')
#             gc.collect()
#     except:
#         lbl_gen_fr3_3_value['text'] = 'Fucking ERROR!!!'
#         lbl_gen_fr3_4_value['text'] = 'Fucking ERROR!!!'
#         lbl_gen_fr3_5_value['text'] = 'Fucking ERROR!!!'
#         lbl_gen_fr3_6_value['text'] = 'Fucking ERROR!!!'
#         pass
#     finally:
#         gc.collect()
        # root.after(3000, parser_GPIO_4relay)


# def check_req():
#     try:
#         # r = requests.get('https://google.com/')  # резервный ('http://httpbin.org/get')
#         # print('check_reg ' + str(r.status_code))
#         xxx1=Variables.status_code_check_req
#         if Variables.status_code_check_req == 200:
#             lbl_Internet_sensor['text'] = 'Internet sensor status: Connected, Ok'
#             print('check_reg')
#         else:
#             lbl_Internet_sensor['text'] = 'Internet sensor status: Disconnected, Error!'
#             print('check_reg')
#         gc.collect()
#         # root.after(3000, check_req)
#     except:
#         print('except! Internet')
#         lbl_Internet_sensor['text'] = 'Internet sensor status: Error!'
#         pass
#     finally:
#         gc.collect()
#         # root.after(3000, check_req)


# def check_Light_sensor_conections():
#     try:
#         rl = requests.get('http://192.168.0.110/')
#         print('status_code Light_sensor_connection: ' + str(rl.status_code))
#         if int(rl.status_code) == 200:
#             # root.after(0, xxx)
#             lbl_Light_sensor['text'] = 'Light sensor status: Connected, Ok'
#         else:
#             lbl_Light_sensor['text'] = 'Light sensor status: Disconnected, Error!'
#         # root.after(1000, check_Light_sensor_conections)
#         rl.close()
#         del rl
#         gc.collect()
#     except:
#         print('except! Light sensor')
#         lbl_Light_sensor['text'] = 'Light sensor status: Error!'
#         pass
#         gc.collect()
#         # root.after(1000, check_Light_sensor_conections)


# def check_Server_sensor_conections():
#     try:
#         rg = requests.get("http://f0555107.xsph.ru/")  # резервный ('http://httpbin.org/get')
#         print('check server ' + str(rg.status_code))
#         if int(rg.status_code) == 200:
#             lbl_Server_sensor['text'] = 'Server sensor status: Connected, Ok'
#         else:
#             lbl_Server_sensor['text'] = 'Server sensor status: Disconnected, Error!'
#         Variables.status_code_server_connections = rg.status_code
#         rg.close()
#         del rg
#     except:
#         print('except! Server')
#         lbl_Server_sensor['text'] = 'Server sensor status: Error!'
#         pass
#     gc.collect()
#     # root.after(1000, check_Server_sensor_conections)


def update_time():
    # change text on Label
    lbl_time['text'] = time.strftime('Current date: %Y-%m-%d Current time: %H:%M:%S')

    # run `update_time` again after 1000ms (1s)
    root.after(1000, update_time)  # function name without ()
# def start_function():
    # check_Server_sensor_conections()
    # check_Light_sensor_conections()
    # check_req()
    # parser_GPIO_4relay()
    # parser_GPIO_sadok()
    # xxx()
    # gc.collect()
    # root.after(300000, start_function)


root = Tk()
setwindow(root)
frame_main_frame = Frame(master=root, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame_sensor_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5, bg='#0f80f2')

frame_tumblers_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_general1 = Frame(master=frame_tumblers_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_general2 = Frame(master=frame_tumblers_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_general3 = Frame(master=frame_tumblers_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')

frame_tumblers1_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_tumblers2_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_tumblers3_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')

lbl_time = Label(master=frame_sensor_frame, text='Current time: 00:00:00', font="Tahoma 12", bg='#0f80f2')
lbl_time.pack()

lbl_connections = Label(master=frame_sensor_frame, text='Connections state', font="Tahoma 14", bg='#0f80f2')
lbl_connections.pack()

lbl_Power_sensor = Label(master=frame_sensor_frame, text='Power sensor status: Connected, Power on', font='Tahoma 10',
                         bg='#0f80f2')
lbl_Light_sensor = Label(master=frame_sensor_frame, text='Light sensor status: ', font='Tahoma 10', bg='#0f80f2')
lbl_Water_sensor = Label(master=frame_sensor_frame, text='Water sensor status: Connected, Ok', font='Tahoma 10',
                         bg='#0f80f2')
lbl_Gas_sensor = Label(master=frame_sensor_frame, text='Gas sensor status: Connected, Ok', font='Tahoma 10',
                       bg='#0f80f2')
lbl_Server_sensor = Label(master=frame_sensor_frame, text='Server sensor status: Connected, Ok', font='Tahoma 10',
                          bg='#0f80f2')
lbl_Internet_sensor = Label(master=frame_sensor_frame, text='Internet sensor status: ', font='Tahoma 10', bg='#0f80f2')

lbl_Power_sensor.pack()
lbl_Light_sensor.pack()
lbl_Water_sensor.pack()
lbl_Gas_sensor.pack()
lbl_Server_sensor.pack()
lbl_Internet_sensor.pack()

lbl_general = Label(master=frame_tumblers_frame, text='General', font="Tahoma 16", bg='#a4aaab')
lbl_general.pack()
lbl_gen_fr_1 = Label(master=frame_general1, text='Light sensor value', font="Tahoma 14", bg='#a4aaab')
lbl_gen_fr_1_value = Label(master=frame_general1, text='Unknown value', font="Tahoma 14", bg='White')
lbl_gen_fr_2 = Label(master=frame_general1, text='Light sensor2 value', font="Tahoma 14", bg='#a4aaab')
lbl_gen_fr_2_value = Label(master=frame_general1, text='Unknown value', font="Tahoma 14", bg='White')
lbl_gen_fr_3 = Label(master=frame_general1, text='Light sensor value', font="Tahoma 14", bg='#a4aaab')
lbl_gen_fr_3_value = Label(master=frame_general1, text='Unknown value', font="Tahoma 14", bg='White')
lbl_gen_fr_4 = Label(master=frame_general1, text='Light sensor value', font="Tahoma 14", bg='#a4aaab')
lbl_gen_fr_4_value = Label(master=frame_general1, text='Unknown value', font="Tahoma 14", bg='White')
lbl_gen_fr_5 = Label(master=frame_general1, text='Light sensor value', font="Tahoma 14", bg='#a4aaab')
lbl_gen_fr_5_value = Label(master=frame_general1, text='Unknown value', font="Tahoma 14", bg='White')
lbl_gen_fr_1.pack(pady=1)
lbl_gen_fr_1_value.pack(pady=1)
lbl_gen_fr_2.pack(pady=1)
lbl_gen_fr_2_value.pack(pady=1)
lbl_gen_fr_3.pack(pady=1)
lbl_gen_fr_3_value.pack(pady=1)
lbl_gen_fr_4.pack(pady=1)
lbl_gen_fr_4_value.pack(pady=1)
lbl_gen_fr_5.pack(pady=1)
lbl_gen_fr_5_value.pack(pady=1)

lbl_gen_fr2_1 = Label(master=frame_general2, text='selective control', font="Tahoma 14", bg='#a4aaab')
lbl_gen_fr2_1.place(x=45, y=20, width=150, height=25)
lbl_gen_fr2_2 = Label(master=frame_general2, text='street light control', font="Tahoma 14", bg='#a4aaab')
lbl_gen_fr2_2.place(x=42, y=95, height=25)
lbl_gen_fr2_3 = Label(master=frame_general2, text='input power control', font="Tahoma 14", bg='#a4aaab')
lbl_gen_fr2_3.place(x=35, y=174, height=25)
lbl_gen_fr2_4 = Label(master=frame_general2, text='control system', font="Tahoma 14", bg='#a4aaab')
lbl_gen_fr2_4.place(x=57, y=252, height=25)

lbl_gen_fr3_1 = Label(master=frame_general3, text='Relay sadok', font="Tahoma 12", bg='#a4aaab')
lbl_gen_fr3_1_value = Label(master=frame_general3, text='Unknown position', font="Tahoma 12", bg='White')
lbl_gen_fr3_2 = Label(master=frame_general3, text='Reley2', font="Tahoma 12", bg='#a4aaab')
lbl_gen_fr3_2_value = Label(master=frame_general3, text='Unknown position', font="Tahoma 12", bg='White')
lbl_gen_fr3_3 = Label(master=frame_general3, text='4 Reley 1', font="Tahoma 12", bg='#a4aaab')
lbl_gen_fr3_3_value = Label(master=frame_general3, text='Unknown position', font="Tahoma 12", bg='White')
lbl_gen_fr3_4 = Label(master=frame_general3, text='4 Reley 2', font="Tahoma 12", bg='#a4aaab')
lbl_gen_fr3_4_value = Label(master=frame_general3, text='Unknown position', font="Tahoma 12", bg='White')
lbl_gen_fr3_5 = Label(master=frame_general3, text='4 Reley 3', font="Tahoma 12", bg='#a4aaab')
lbl_gen_fr3_5_value = Label(master=frame_general3, text='Unknown position', font="Tahoma 12", bg='White')
lbl_gen_fr3_6 = Label(master=frame_general3, text='4 Reley 4', font="Tahoma 12", bg='#a4aaab')
lbl_gen_fr3_6_value = Label(master=frame_general3, text='Unknown position', font="Tahoma 12", bg='White')
lbl_gen_fr3_1.pack(pady=1)
lbl_gen_fr3_1_value.pack(pady=1)
lbl_gen_fr3_2.pack(pady=1)
lbl_gen_fr3_2_value.pack(pady=1)
lbl_gen_fr3_3.pack(pady=1)
lbl_gen_fr3_3_value.pack(pady=1)
lbl_gen_fr3_4.pack(pady=1)
lbl_gen_fr3_4_value.pack(pady=1)
lbl_gen_fr3_5.pack(pady=1)
lbl_gen_fr3_5_value.pack(pady=1)
lbl_gen_fr3_6.pack(pady=1)
lbl_gen_fr3_6_value.pack(pady=1)

lbl_overview = Label(master=frame_tumblers1_frame, text='Overview', font="Tahoma 16", bg='#a4aaab')
lbl_overview.pack()

lbl_settings = Label(master=frame_tumblers2_frame, text='Settings', font="Tahoma 16", bg='#a4aaab')
lbl_settings.pack()

lbl_settings_server_IP = Label(master=frame_tumblers2_frame, text='Server IP', font="Tahoma 14", bg='#a4aaab')
lbl_settings_server_IP.place(x=0, y=50)
ent_settings_server_ip = Entry(master=frame_tumblers2_frame, text='', font="Tahoma 14", bg='White', fg='Black')
ent_settings_server_ip.place(x=150, y=50)

lbl_settings_Internet_IP = Label(master=frame_tumblers2_frame, text='Internet IP', font="Tahoma 14", bg='#a4aaab')
lbl_settings_Internet_IP.place(x=0, y=90)
ent_settings_Internet_IP1 = Entry(master=frame_tumblers2_frame, text='', font="Tahoma 14", bg='White', fg='Black')
ent_settings_Internet_IP1.place(x=150, y=90)

lbl_settings_sensor1 = Label(master=frame_tumblers2_frame, text='Sensor Light IP', font="Tahoma 14", bg='#a4aaab')
lbl_settings_sensor1.place(x=0, y=130)
ent_settings_sensor1 = Entry(master=frame_tumblers2_frame, text='', font="Tahoma 14", bg='White', fg='Black')
ent_settings_sensor1.place(x=150, y=130)

lbl_settings_ESP1 = Label(master=frame_tumblers2_frame, text='ESP1 IP', font="Tahoma 14", bg='#a4aaab')
lbl_settings_ESP1.place(x=420, y=50)
ent_settings_ESP1 = Entry(master=frame_tumblers2_frame, text='', font="Tahoma 14", bg='White', fg='Black')
ent_settings_ESP1.place(x=540, y=50)

lbl_settings_ESP2 = Label(master=frame_tumblers2_frame, text='ESP2 IP', font="Tahoma 14", bg='#a4aaab')
lbl_settings_ESP2.place(x=420, y=90)
ent_settings_ESP2 = Entry(master=frame_tumblers2_frame, text='', font="Tahoma 14", bg='White', fg='Black')
ent_settings_ESP2.place(x=540, y=90)

lbl_settings_ESP3 = Label(master=frame_tumblers2_frame, text='ESP3 IP', font="Tahoma 14", bg='#a4aaab')
lbl_settings_ESP3.place(x=420, y=130)
ent_settings_ESP3 = Entry(master=frame_tumblers2_frame, text='', font="Tahoma 14", bg='White', fg='Black')
ent_settings_ESP3.place(x=540, y=130)

lbl_reserved = Label(master=frame_tumblers3_frame, text='Reserved', font="Tahoma 16", bg='#a4aaab')
lbl_reserved.pack()

button1 = Button(master=frame_main_frame, text="General", command=general_menu, bg="#adb2b8", fg="Black",
                 font="Tahoma 14")
button2 = Button(master=frame_main_frame, text="Overview", command=overview, bg="#adb2b8", fg="Black", font="Tahoma 14")
button3 = Button(master=frame_main_frame, text="Settings", command=settings, bg="#adb2b8", fg="Black", font="Tahoma 14")
button4 = Button(master=frame_main_frame, text="Reserved", command=reserved, bg="#adb2b8", fg="Black", font="Tahoma 14")

button311 = Button(master=frame_general2, text="General1", command=general_menu, bg="#adb2b8", fg="Black",
                   font="Tahoma 14")
button312 = Button(master=frame_general2, text="General1", command=general_menu, bg="#adb2b8", fg="Black",
                   font="Tahoma 14")
button313 = Button(master=frame_general2, text="General1", command=general_menu, bg="#adb2b8", fg="Black",
                   font="Tahoma 14")
button314 = Button(master=frame_general2, text="General1", command=general_menu, bg="#adb2b8", fg="Black",
                   font="Tahoma 14")
button315 = Button(master=frame_general2, text="General1", command=general_menu, bg="#adb2b8", fg="Black",
                   font="Tahoma 14")

var = BooleanVar()
var.set(0)
R1 = Radiobutton(master=frame_general2, text="Local remote   ", width=29, height=1, variable=var, value=True)
R1.place(x=5, y=45)
R2 = Radiobutton(master=frame_general2, text="Online remote", width=29, height=1, variable=var, value=False)
R2.place(x=5, y=65)

var2 = BooleanVar()
var2.set(0)
R3 = Radiobutton(master=frame_general2, text="Manual Off       ", width=29, height=1, variable=var2, value=True)
R3.place(x=5, y=125)
R4 = Radiobutton(master=frame_general2, text="Manual On       ", width=29, height=1, variable=var2, value=False)
R4.place(x=5, y=145)

var3 = BooleanVar()
var3.set(0)
R5 = Radiobutton(master=frame_general2, text="Manual Off       ", width=29, height=1, variable=var3, value=True)
R5.place(x=5, y=205)
R6 = Radiobutton(master=frame_general2, text="Manual On       ", width=29, height=1, variable=var3, value=False)
R6.place(x=5, y=225)
var4 = BooleanVar()
var4.set(0)
R7 = Radiobutton(master=frame_general2, text="Manual Off       ", width=29, height=1, variable=var4, value=True)
R7.place(x=5, y=280)
R8 = Radiobutton(master=frame_general2, text="Manual On       ", width=29, height=1, variable=var4, value=False)
R8.place(x=5, y=300)

frame_main_frame.place(x=5, y=5, width=790, height=590)
frame_sensor_frame.place(x=150, y=10, width=622, height=195)
frame_tumblers_frame.place(x=18, y=225, width=765, height=355)
frame_tumblers1_frame.place(x=18, y=225, width=765, height=355)
frame_tumblers2_frame.place(x=18, y=225, width=765, height=355)
frame_tumblers3_frame.place(x=18, y=225, width=765, height=355)
frame_general1.place(x=3, y=5, width=250, height=340)
frame_general2.place(x=256, y=5, width=250, height=340)
frame_general3.place(x=508, y=5, width=250, height=340)

button1.place(x=10, y=13, width=130, height=40)
button2.place(x=10, y=63, width=130, height=40)
button3.place(x=10, y=113, width=130, height=40)
button4.place(x=10, y=163, width=130, height=40)

button311.place()
button312.place()
button313.place()



# root.after(0, start_function)
root.after(0, start_frame)
root.after(0, check_Power)
# root.after(0, check_req)
# root.after(2000, check_Light_sensor_conections)
# root.after(1000, check_Server_sensor_conections)
root.after(1000, update_time)
root.title('Control panel')
# root.after(500, parser_GPIO_sadok)
# root.after(500, parser_GPIO_4relay)
# root.after(0, xxx)
root.mainloop()