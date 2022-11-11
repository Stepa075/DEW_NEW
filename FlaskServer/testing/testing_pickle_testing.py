import pickle


def run():  # For experiments...
    load_from_file('data.pickle', "items_iter", "a")


def write_to_file():
    pass


def load_from_file(file, method, key):
    try:
        with open(file, "rb") as f:
            data_load = pickle.load(f)
            if method == "key":
                try:
                    print(data_load[f'{key}'])
                except:
                    print("Bad key value!")

            elif method == "keys" or method == "values" or method == "items":
                print(eval(f"data_load.{method}()"))
            elif method == "keys_iter":
                keys = []
                for key in data_load:  # итерация словаря по ключу, можно использовать data_load.keys()
                    keys.append(key)
                print(keys)
            elif method == "values_iter":
                values = []
                for value in data_load.values():  # итерация словаря по значению
                    values.append(value)
                print(values)
            elif method == "items_iter":
                dict = {}
                for key, value in data_load.items():  # итерация словаря по значению и ключу
                    dict[key] = value
                print(dict)
            else:
                print("load_from_file: No match methods!")
                return None
    except:
        print("Wrong file name or directory!")


if __name__ == "__main__":
    run()
