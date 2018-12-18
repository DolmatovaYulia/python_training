from model.group import Group


def test_del_group(app):
    if app.group.count() == 0:
        app.group.Create(Group(group_name="test"))
    app.group.Delete_first_group()

