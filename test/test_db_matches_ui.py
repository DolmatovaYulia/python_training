# Тест для проверки работоспособности фикстур (соответствие БД и пользовательского интерфейса)
from model.group import Group
from timeit import timeit


def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))

    def clean(group):
        return Group(id=group.id, group_name=group.group_name.strip())

    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert False
    # sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
