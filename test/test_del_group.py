from model.group import Group


def test_del_group(app):
    if app.group.count() == 0:
        app.group.Create(Group(group_name="test"))
    old_groups = app.group.get_group_list()
    app.group.Delete_first_group()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups

