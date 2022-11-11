# Фильтр пустых строк в списке строк.
list = [x for x in list if x.strip()!='']

# Чтение файла по строкам.
with open("/path/to/file") as f:
    for line in f:
        print(line)
# Запись в файл строка за строкой.
f = open("/path/tofile", 'w')

for e in aList:
    f.write(e + "\n")

f.close()
# Позиционирование строки в тексте.
sentence = "this is a test, not testing."
it = re.finditer('\\btest\\b', sentence)
for match in it:
    print("match position: " + str(match.start()) +"-"+ str(match.end()))
# Запрос в базе данных.
db = MySQLdb.connect("localhost", "username", "password", "dbname")
cursor = db.cursor()

sql = "SELECT `name`, `age` FROM `ursers` ORDER BY `age` DESC"
cursor.execute(sql)
results = cursor.fetchall()

for row in results:
    print(row[0] + row[1])

db.close()
# Создание списка с указанным символом.
theList = ["a","b","c"]
joinedString = ",".join(theList)
# Фильтр дублируемых элементов.
targetList = list(set(targetList))
# Удаляем пустые значения из списка.
targetList = [v for v in targetList if not v.strip()=='']
# или
targetList = filter(lambda x: len(x)>0, targetList)
# Добавление списка к другому списку.
anotherList.extend(aList)
# Итерация словаря.
for k,v in aDict.iteritems():
    print(k + v)
# Есть ли строка в списке.
myList = ['one', 'two', 'ten']

if 'one' in myList:
    print('Да')
# Соединяем два словаря.
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

print(z)  # {'c': 4, 'a': 1, 'b': 3}
# Поиск используя регулярные выражения.
m = re.search('\d+-\d+', line) # search 123-123 like strings
if m:
    current = m.group(0)