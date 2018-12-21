from model.group import Group
from random import randrange

"""
def test_update_group(app):
    if app.group.count() == 0:
        app.group.Create(Group(group_name="test"))
    old_groups = app.group.get_group_list()
    app.group.Update_first_group(Group(group_name="group123", header="gr1", footer="gr2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_update_empty_group(app):
    if app.group.count() == 0:
        app.group.Create(Group(group_name="test"))
    old_groups = app.group.get_group_list()
    app.group.Update_first_group(Group(group_name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
"""


def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.Create(Group(group_name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(group_name="new group")
    group.id = old_groups[index].id
    app.group.Update_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

"""
def test_update_group_header(app):
    if app.group.count() == 0:
        app.group.Create(Group(group_name="test"))
    old_groups = app.group.get_group_list()
    app.group.Update_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
"""

