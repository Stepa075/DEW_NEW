from time import sleep

import requests

from client import Variables


def send_data():
    while True:
        try:
            r = requests.get('http://f0555107.xsph.ru/index.php', timeout=3.0)
            response = r.status_code = "UTF8"
            print(str(response))
            print(r.text)
            sleep(3.0)
        except:
            sleep(3.0)
            continue
            pass



def get_data():
    while True:
        try:
            url = "127.0.0.1:5000/data_get"
            r = requests.get(url, timeout=3.00)
            r.encoding = "UTF8"
            if r.status_code == 200:
                print('get_data = Ok')
                data = r.text.split(',')
                Variables.list_of_get_data = data
                sleep(3.0)
        except:
            sleep(3.0)
            continue
            pass
