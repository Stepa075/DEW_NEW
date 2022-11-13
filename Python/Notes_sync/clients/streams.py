from time import sleep
import requests
import Variables


def get_data():
    while True:
        try:
            r = requests.get('http://' + str(Variables.ip) + '/data_get')
            Variables.list_of_get_data = r.text
            Variables.code_of_response_server = r.status_code
            print( "get data   "+Variables.list_of_get_data)
            sleep(2)
        except:
            sleep(2)
            continue
            pass






