from New_HAN_PCN import Variables

list_of_lines = []
f = open("bin/settings.ini", 'r')
for line in f:
    list_of_lines.append(line.rstrip('\n'))
f.close()
# print(list_of_lines)
Variables.addres_of_getting_events = str(list_of_lines[0])
print(Variables.addres_of_getting_events)