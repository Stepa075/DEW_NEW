from time import sleep
import requests
import Variables


def get_data():
    while True:
        try:
            r = requests.get('http://' + str(Variables.ip) + '/data_json_get')
            dict = r.json()
            list_list = []
            for val in dict.values():
                list_list.append(val)
            print(list_list)
            if list_list[-1] == '\n' or list_list[-1] == '':
                del list_list[-1]
            Variables.list_of_get_data = list_list
            Variables.code_of_response_server = r.status_code
            print("get data   "+str(Variables.list_of_get_data))
            sleep(2)
        except:
            Variables.code_of_response_server = 404
            print(Variables.code_of_response_server)
            sleep(2)
            continue
            pass






