from time import sleep
import requests
import Variables


def get_data():
    while True:
        try:
            r = requests.get('http://' + str(Variables.ip) + '/data_get')
            Variables.list_of_get_data = r.text
            print( "get data   "+Variables.list_of_get_data)
            sleep(3.5)
        except:
            sleep(3.5)
            continue
            pass






