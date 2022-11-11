def parsing_ESP_nasos():
    while True:

        try:
            url = "http://192.168.0.140/uartbrprint"
            r = requests.get(url)
            Variables.status_code_4relay = r.status_code
            r.encoding = "UTF8"
            with open('nasos_ESP.txt', 'w') as output_file:
                output_file.write(r.text)
            f = open('nasos_ESP.txt')
            str_nasos = f.read()
            f.close()
            print('parsing_ESP_nasos = Ok')
            str_1 = str_nasos
            Variables.gerkon_down = str_1[12:13]
            Variables.gerkon_up = str_1[24:25]
            Variables.gerkon_alarm = str_1[39:40]
            Variables.status = str_1[41:47]
            Variables.Position_relay1_on_off = str_1[51:52]
            Variables.Position_relay2 = str_1[56:57]
            Variables.Position_relay3_alarm = str_1[61:62]
            sleep(10.0)
        except:
            sleep(10.0)
            continue
            pass
    sleep(10.0)
