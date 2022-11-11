from time import sleep

import requests
import datetime
from random import randint

while True:
    now = datetime.datetime.now()
    id = randint(0, 10)
    data = randint(20, 95)
    res = requests.get(
        'http://localhost:5000/data_receive?datetime=' + str(now) + '&id=' + str(id) + '&data=' + str(data))
    print(res)
    sleep(2)