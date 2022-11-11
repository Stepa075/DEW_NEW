from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/<username>')
# def show_user_profile(username):
#     return 'Hello my good friend %s' % username
def show_user_name(username):
    return f'Hello my good friend {username} I love you!'


# @app.route("/data", methods=['GET', ])
# def setinfo():
#     # Получить значение параметра id во входящем URL http://localhost:5000/data?id=666&data=123456
#     sendid = request.args.get('id')
#     getdata = request.args.get('data')
#     with open("data.txt", "w") as f:
#         f.write(getdata)
#     return "Get info id is " + str(sendid)

@app.route("/data_receive", methods=['GET', ])
def setinfo():
    # Получить значение параметра id во входящем URL http://localhost:5000/data?id=0001&data_time=05.09.2022,
    # 06:23&event=1-1,2-1,3-1,4-0.5-1,6-1,7-0
    sendid = request.args.get('id')
    getdata = request.args.get('data')
    with open(str(sendid) + ".txt", "w") as f:
        f.write(getdata)
    return "Ok"


@app.route("/data_get", methods=['GET', ])
def getinfo():
    getid = request.args.get('id')
    with open(str(getid) + ".txt", 'r') as f:
        a = f.read()  # .split('\n')
    return str(a)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
