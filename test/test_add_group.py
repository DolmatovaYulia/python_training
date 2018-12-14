# -*- coding: utf-8 -*-
from model.group import Group


# Test method that takes a fixture as a parameter
def test_add_group(app):
    app.group.Create(Group(group_name="group", header="gr", footer="gr"))


def test_add_empty_group(app):
    app.group.Create(Group(group_name="", header="", footer=""))







