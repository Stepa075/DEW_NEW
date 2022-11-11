import pickle

data = {
    'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'c': {None, True, False}
}
value = {
    'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'c': {None, True, False}
}
method = "wb"
file = "data.pickle"
def save_to_file(file, value, method):
    with open(file, 'wb') as f:
        pickle.dump(value, f)




# def load_from_file(file, method, key):
#     with open(file, 'rb') as f:
#         data_load = pickle.load(f)
#
#     print(data_load['a'])  # Вывод значения словаря по ключу
#     print(data_load.keys())  # Вывод всех ключей словаря
#     print(data_load.values())  # Вывод всех значнеий словаря
#     print(data_load.items())  # Вывод всех пар ключ-значение словаря
#     for key in data_load:  # итерация словаря по ключу, можно использовать data_load.keys()
#         print(key)

    # for values in data_load.values():  # итерация словаря по значению
    #     print(values)
    #
    # for key, value in data_load.items():  # итерация словаря по значению и ключу
    #     print(key, value)


if __name__ == "__main__":
    save_to_file(file, data, method)
