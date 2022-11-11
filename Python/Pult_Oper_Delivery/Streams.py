import gc
import time
from time import sleep

import requests

import Functions
import Variables


def check_new_events_from_server():
    while True:
        try:
            res = requests.get('http://localhost:5000/data_get_file?id=all_data')
            list1 = res.text
            a = list1
            list2 = list1.split('\n')
            del list2[-1]
            print(list2)
            # listishe = listishe + list2
            # print(listishe)
            number_of_elements = len(list2)
            print(len(list2))
            if number_of_elements >= 50:
                print(" Owerflow list!!!!")
                break
            else:
                pass
        except:
            print("Fuck!")
            pass

        time.sleep(2)


def check_Server_sensor_connections():
    while True:
        try:
            rg = requests.get("http://127.0.0.1/hello.html")  # резервный ('http://httpbin.org/get')
            # Variables.counting_requaest += 1
            print('check server ' + str(rg.status_code))
            if int(rg.status_code) == 200:
                # lbl_Server_sensor['text'] = 'Server sensor status: Connected, Ok'
                print('connected ok')
            else:
                print('connected false')
                # lbl_Server_sensor['text'] = 'Server sensor status: Disconnected, Error!'
            # Variables.status_code_server_connections = rg.status_code
            rg.close()
            del rg
        except:
            print('except! Server')
            # lbl_Server_sensor['text'] = 'Server sensor status: Error!'
            pass

        gc.collect()
        sleep(5)


def start1():
    while True:
        try:
            if Variables.status_code_server_connections == 200:
                r4_0 = Variables.parsing_GPIO_4relay1
                r4_1 = str(Variables.r1)
                r4_2 = str(Variables.r2)
                r4_3 = str(Variables.r3)
                r4_4 = str(Variables.r4)
                params = {'params': str(Variables.parsing_ESP1),
                          'params1': str(Variables.Sadok_Light1),
                          'params2_1': r4_1,
                          'params2_2': r4_2,
                          'params2_3': r4_3,
                          'params2_4': r4_4, 'control': 'home'}
                print(params)
                r = requests.get('http://f0555107.xsph.ru/index.php', params=params, timeout=3.0)
                Variables.counting_requaest += 1
                r.encoding = "UTF8"
                print('start1 = Ok')
                print(r.text)
            else:
                print('start1 ' + Variables.time_now + ' Bad response, status_code= ' + str(
                    Variables.status_code_server_connections))
            sleep(20.0)
        except:
            sleep(20.0)
            continue
            pass
    sleep(20.0)


def start2():
    a = 1
    while a == 1:
        # global lines

        try:
            url = "http://127.0.0.1/hello.html"
            r = requests.get(url)
            print(r.text)
            r.encoding = "UTF8"
            print('start2 = Ok')
            lines = r.text.split(',')
            # print(lines)

            Variables.receive_from_server = lines
            Variables.receive_from_server1 = lines[0]
            Variables.receive_from_server1 = lines[1]
            Variables.receive_from_server1 = lines[2]
            Variables.receive_from_server1 = lines[3]
            Variables.receive_from_server1 = lines[4]
            Variables.receive_from_server1 = lines[5]
            # Variables.receive_from_server1 = lines[6]

            sleep(5.0)

        except:
            # lines.append('0')
            print('Except! No connect to work server!')

            pass
            sleep(5.0)

    sleep(5.0)


def if_current_date_is_correct():
    while True:
        if Variables.date_current == str(time.strftime('%Y.%m.%d')):
            print(" if_current_date_is_correct(): current date is correct!")
        else:
            Variables.date_current = time.strftime('%Y.%m.%d')
            Functions.logging_session("Start a new file.",
                                      'bin/logging/' + str(Variables.date_current) + '_session.txt')
            sleep(0.5)
            Functions.logging_session("Start a new file.", 'bin/logging/' + str(Variables.date_current) + '_alerts.txt')
            sleep(0.5)
            Functions.logging_session("Start a new file.", 'bin/logging/' + str(Variables.date_current) + '_logs.txt')
            print("Variables.date_current = " + str(time.strftime('%Y.%m.%d')))
        sleep(1.0)

# if __name__ == '__main__':
#     start2()
