import os
import pickle

from flask import Flask
from flask import request

import Variables


def after_start():
    lines1 = []

    if os.path.exists('data/content.txt'):
        with open('data/content.txt', 'r', encoding="UTF-8") as fp:  # Считываем объекты из файла в лист
            for n, line in enumerate(fp, 1):
                line = line.rstrip('\n')
                lines1.append(line)
        Variables.list_of_content_txt = lines1
    else:
        with open('data/content.txt', "w"):
            pass
    if os.path.exists('data/data.pickle'):
        with open('data/data.pickle', 'rb') as f:  # Выгружаем данные из файла пикли
            try:
                data_new = pickle.load(f)
            except:
                data_new = []
                pass
        Variables.list_of_content_data = data_new
    else:
        with open('data/data.pickle', "w"):
            pass

    print("Variables.dictionary_of_content = " + str(Variables.dictionary_of_content))
    print("Variables.list_of_content_data = " + str(Variables.list_of_content_data))
    # Выгрузили содержимое контент.тхт в список и словарь...


app = Flask(__name__)


@app.route("/data_set", methods=['GET', ])
def set_info():

    data = request.args.get('data')  # Получаем значение ID из запроса
    if data != '':
        incoming_list = list(data.split(','))
        for lis in incoming_list:
            if lis not in Variables.list_of_content_data: Variables.list_of_content_data.append(lis)
        for lis in incoming_list:
            if lis not in Variables.list_of_content_txt: Variables.list_of_content_txt.append(lis)
        print(Variables.list_of_content_data)

        with open('data/data.pickle', 'wb') as f:
            pickle.dump(Variables.list_of_content_data, f)
    else:
        Variables.list_of_content_data = []
        with open('data/data.pickle', 'wb') as f:
            pickle.dump(Variables.list_of_content_data, f)
    return "Ok!"


@app.route("/data_get", methods=['GET', ])
def getinfo_from_file():
    return "".join(Variables.list_of_content_data)


if __name__ == "__main__":
    after_start()
    app.run(host='0.0.0.0', port=5000, debug=True)
