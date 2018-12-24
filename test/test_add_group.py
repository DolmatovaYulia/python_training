# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


# Генератор случайных строк
def random_strint(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# Тестовые данные
testdata = [Group(group_name="", header="", footer="")] + [
    Group(group_name=random_strint("name", 10), header=random_strint("header", 20), footer=random_strint("footer", 20))
    for i in range(5)
]


# Передаются название параметра, куда должны передаваться тестовые данные, источник данных
# и список с текстовым представлением данных
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.Create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
