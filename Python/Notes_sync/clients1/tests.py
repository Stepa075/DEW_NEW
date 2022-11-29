dict = {}
list = ["123", "456", '335', '222']
for index, val in enumerate(list):
    # dictionary = dict.fromkeys(str(index), val)
    dict[index] = val
    print(index)
    print(val)
print(dict)

list_list = []
for val in dict.values():
    list_list.append(val)
print(list_list)