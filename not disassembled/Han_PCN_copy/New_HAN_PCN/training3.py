list_of_settings = []
with open("bin/settings.ini") as f:
    for line in f:
        list_of_settings.append(line.rstrip("\n"))

print(list_of_settings)