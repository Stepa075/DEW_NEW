from time import sleep
import requests
import Variables


def get_data():
    while True:
        try:
            r = requests.get('http://' + str(Variables.ip) + '/data_get')
            Variables.list_of_get_data = list(r.text.split(','))
            Variables.code_of_response_server = r.status_code
            print( "get data   "+str(Variables.list_of_get_data))
            sleep(2)
        except:
            Variables.code_of_response_server = 404
            print(Variables.code_of_response_server)
            sleep(2)
            continue
            pass






