# -*- coding: utf-8 -*-
from model.group import Group


# Test method that takes a fixture as a parameter
def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="group", header="gr", footer="gr")
    app.group.Create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="", header="", footer="")
    app.group.Create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




