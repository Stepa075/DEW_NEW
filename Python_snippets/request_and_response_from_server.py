# Отправка данных на сервер со скриптом приема и записи этих данных на страницу.
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
                Variables.counting_requaest +=1
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

#Запрос страницы на сервере, ее прием, распарсивание в лист и извлечение в переменные.
def start2():
    while True:
        try:
            if Variables.status_code_server_connections == 200:
                url = "http://f0555107.xsph.ru/hello.html"
                r = requests.get(url, timeout=3.00)
                Variables.counting_requaest += 1
                r.encoding = "UTF8"
                if r.status_code == 200:
                    print('start2 = Ok')
                    with open('response_server.html', 'w') as output_file:
                        output_file.write(r.text)
                    with open('response_server.txt', 'w') as output_file:
                        output_file.write(r.text)
                    text_file = open("response_server.html", "r")
                    lines = text_file.read().split(',')
                    print(lines)
                    # print(len(lines))
                    text_file.close()
                    Variables.receive_from_server = lines
                    Variables.receive_from_server1 = lines[0]
                    Variables.receive_from_server1 = lines[1]
                    Variables.receive_from_server1 = lines[2]
                    Variables.receive_from_server1 = lines[3]
                    Variables.receive_from_server1 = lines[4]
                    Variables.receive_from_server1 = lines[5]
                    Variables.receive_from_server1 = lines[6]
                    # with open('controlling.txt', 'a') as output_file:
                    #   output_file.write(Variables.time_now + str(lines) + '\n')
            else:
                with open('controlling.log.txt', 'a') as output_file:
                    output_file.write('start2 ' + Variables.time_now + ' Bad_status_code!' + '\n')
                print('start2 ' + str(Variables.time_now) + ' Bad response, status_code= ' + str(
                    Variables.status_code_server_connections))
            sleep(20.0)
        except:
            sleep(20.0)
            continue
            pass
    sleep(20.0)
