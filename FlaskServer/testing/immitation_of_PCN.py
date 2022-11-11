import requests
import time
listishe = []
while True:
    try:
        res = requests.get('http://localhost:5000/data_get_file?id=all_data')
        list1 = res.text
        a = list1
        list2 = list1.split('\n')
        del list2[-1]
        print(list2)
        # listishe = listishe + list2
        # print(listishe)
        number_of_elements = len(list2)
        print(len(list2))
        if number_of_elements >= 50:
            print(" Owerflow list!!!!")
            break
        else:
            pass
    except:
        print("Fuck!")
        pass

    time.sleep(2)