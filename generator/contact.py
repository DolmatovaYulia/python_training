from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


# Читаем опции из командной строки
try:
    # n - опция, которая задает количество генерируемых данных
    # f - опция, которая задет файл, в который это должно помещаться
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"


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


# Генератор числовых строк
def random_digits(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])


# Тестовые данные
testdata = [Contact(firstname="", middlename="", lastname="", nickname="", photo="", title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="", phone2="", notes="")] \
           + [Contact(firstname=random_strint("name", 20), middlename=random_strint("middlename", 20), lastname=random_strint("lastname", 20), nickname=random_strint("nickname", 20), title=random_strint("title", 20), company=random_strint("company", 30), address=random_strint("address", 30), home=random_digits("", 6), mobile=random_digits("", 11), work=random_digits("", 6), fax=random_digits("fax", 20), email=random_strint("email", 20), email2=random_strint("email2", 20), email3=random_strint("email3", 20), homepage=random_strint("homepage", 20), address2=random_strint("address2", 20), phone2=random_digits("", 10), notes=random_strint("notes", 30))
              for i in range(5)
]


# Сохранение сгенерированных данных в файл
# Определяем путь к файлу
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# Открываем файл на запись
with open(file, "w") as out:
    # Параметры форматирования. Библиотека работает с разными кодировщиками ("json")
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
