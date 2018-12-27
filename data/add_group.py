from model.group import Group
import random
import string


constant = [
    Group(group_name="name1", header="header1", footer="footer1"),
    Group(group_name="name2", header="header2", footer="footer2")
]


# Генератор случайных строк
def random_strint(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# Тестовые данные
testdata = [Group(group_name="", header="", footer="")] + [
    Group(group_name=random_strint("name", 10), header=random_strint("header", 20), footer=random_strint("footer", 20))
    for i in range(5)
]

