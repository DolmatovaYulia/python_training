from model.group import Group
import random
import string
import os.path
import json
import getopt
import sys


# Читаем опции из командной строки
try:
    # n - опция, которая задает количество генерируемых данных
    # f - опция, которая задет файл, в который это должно помещаться
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/groups.json"

# Читаем опции
for o, a in opts:
    # Если название опции == -n, значит в ней задается количество групп
    if o == "-n":
        # Преобразуем значение опции в число
        n = int(a)
    # Если название опции == -f, значит в ней задается файл
    elif o == "-f":
        f = a

# Генератор случайных строк
def random_strint(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# Тестовые данные
testdata = [Group(group_name="", header="", footer="")] + [
    Group(group_name=random_strint("name", 10), header=random_strint("header", 20), footer=random_strint("footer", 20))
    for i in range(n)
]


# Сохранение сгенерированных данных в файл
# Определяем путь к файлу
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# Открываем файл на запись
with open(file, "w") as out:
    # Функция dumps превращает структуру данных в строку в формате json
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
