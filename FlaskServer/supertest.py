with open('data/list_of_objects/list_of_objects.txt', 'r', encoding='utf-8') as f:
    arr = f.read().splitlines()
d = {}
for line in arr:
    key1, key2, value = line.split()
    d[key1] = {key2: value}
print(d)