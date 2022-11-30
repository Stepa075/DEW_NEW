import os
import pickle

from flask import Flask, jsonify
from flask import request
import json

import Variables


def after_start():
    if os.path.exists('data/data.pickle'):
        with open('data/data.pickle', 'rb') as f:  # Выгружаем данные из файла пикли
            try:
                data_new = pickle.load(f)
            except:
                data_new = []
                pass
        Variables.list_of_content_data = data_new
    else:
        with open('data/data.pickle', "wb"):
            pass

    if os.path.exists('data/data_json.pickle'):
        with open('data/data_json.pickle', 'rb') as f:  # Выгружаем данные из файла пикли
            try:
                data_new = pickle.load(f)
            except:
                data_new = {}
                pass
        Variables.dict_json = data_new
    else:
        with open('data/data_json.pickle', "wb"):
            pass

    print("Variables.dictionary_of_content = " + str(Variables.dictionary_of_content))
    print("Variables.list_of_content_data = " + str(Variables.list_of_content_data))
    # Выгрузили содержимое контент.тхт в список и словарь...
    # Выгрузили содержимое data.pickle в список и словарь...


def load_settings():
    with open("settings.txt", "r", encoding="UTF8") as setings:
        f = setings.read()
        lines = f.split(';')
        Variables.host = lines[0]
        Variables.port = int(lines[1])


app = Flask(__name__)


@app.route("/data_set", methods=['GET', ])
def set_info():
    data = request.args.get('data')  # Получаем значение ID из запроса
    Variables.list_of_content_data = list(data.split(','))
    with open('data/data.pickle', 'wb') as f:
        pickle.dump(Variables.list_of_content_data, f)
    print(str(Variables.list_of_content_data))
    return "Ok!"


@app.route("/data_get", methods=['GET', ])
def getinfo_from_file():
    return ",".join(Variables.list_of_content_data)


@app.route("/data_json_set", methods=['GET', 'POST'])
def set_json_info():
    data = request.get_json()  # Получаем значение  из запроса
    Variables.dict_json = data
    with open('data/data_json.pickle', 'wb') as f:
        pickle.dump(data, f)
    print(data)
    return "Ok!"


@app.route("/data_json_get", methods=['GET', ])
def getinfo_from_file_json():
    return jsonify(Variables.dict_json)


if __name__ == "__main__":
    load_settings()
    after_start()
    app.run(host=Variables.host, port=Variables.port, debug=True)
