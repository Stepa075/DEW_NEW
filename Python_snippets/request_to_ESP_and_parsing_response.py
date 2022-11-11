# Опрос ЕСП с датчиком освещенности.
def parsing_ESP():
    global str3

    while True:
        try:
            if Variables.status_code_light_sensor == 200:
                url = "http://192.168.0.110/sensors/adci1/"
                r = requests.get(url, timeout=3.0)
                r.encoding = "UTF8"
                with open('test.html', 'w') as output_file:
                    output_file.write(r.text)
                with open('test1.txt', 'w') as output_file:
                    output_file.write(r.text)

                f = open('test1.txt')
                str1 = f.read()
                f.close()

                str2 = str1[str1.find(";") + 1:]
                str3 = str2[str2.find(":") + 1: str2.find(";")]
                Variables.parsing_ESP = int(str3)
                Variables.parsing_ESP1 = int(str3)
                print('parsing_ESP = Ok, Variables.parsing_ESP = ' + str(Variables.parsing_ESP))
            else:
                Variables.parsing_ESP = 'No connect ESP!'
            sleep(10.0)
        except:
            sleep(10.0)
            continue
            pass
    sleep(10.0)

# Опрос ЕСП с подключенным одним реле.
def parsing_GPIO_Sadok():
    global str_sad3
    while True:
        try:

            url = "http://192.168.0.100/gpioprint"
            r = requests.get(url, timeout=3.0)
            Variables.status_code_sadok = r.status_code
            r.encoding = "UTF8"
            if r.status_code == 200:
                with open('sadok.html', 'w') as output_file:
                    output_file.write(r.text)
                with open('sadok1.txt', 'w') as output_file:
                    output_file.write(r.text)

                f = open('sadok1.txt')
                str_sad = f.read()
                f.close()
                str_sad2 = str_sad[:str_sad.find(";") + 1]
                str_sad3 = str_sad2[str_sad2.find(":") + 1: str_sad2.find(";")]
                Variables.Sadok_Light = int(str_sad3)
                Variables.Sadok_Light1 = int(str_sad3)
                print('parsing_GPIO_Sadok = Ok ')
            else:
                Variables.status_code_sadok = 0
                Variables.Sadok_Light = 2
                str_sad3 = 2
                print('parsing_GPIO_Sadok = else(error, can not read)!')
            sleep(10.0)
        except NewConnectionError:
            Variables.Sadok_Light = 'Except, NewConnection error!!'
            str_sad3 = 2
            continue
        except:
            sleep(10.0)
            continue
            pass
    sleep(10.0)

# Опрос ЕСП с подключенными четырьмя реле.

def parsing_GPIO_4relay11():
    while True:

        try:
            url = "http://192.168.0.120/gpioprint"
            r = requests.get(url)
            Variables.status_code_4relay = r.status_code
            r.encoding = "UTF8"
            with open('4relay.txt', 'w') as output_file:
                output_file.write(r.text)
            f = open('4relay.txt')
            str_4relay = f.read()
            f.close()
            print('parsing_GPIO_4relay = Ok')
            str_4relay2 = str_4relay[str_4relay.find(":") + 1:]

            Variables.r1 = str_4relay2[: str_4relay2.find(";")]
            Variables.r2 = str_4relay[10:11]
            Variables.r3 = str_4relay[18:19]
            Variables.r4 = str_4relay[23:24]
            # relay_list = [r1, r2, r3, r4]
            # Variables.parsing_GPIO_4relay = relay_list
            # Variables.parsing_GPIO_4relay1 = relay_list
            # print('Variables.parsing_GPIO_4relay =' + str(Variables.parsing_GPIO_4relay))
            sleep(10.0)
        except:
            sleep(10.0)
            continue
            pass
        # break
    sleep(10.0)
