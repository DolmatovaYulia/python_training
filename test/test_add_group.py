# -*- coding: utf-8 -*-
from model.group import Group


# Test method that takes a fixture as a parameter
def test_add_group(app):
    app.session.Login(user_name="admin", password="secret")
    app.group.Create(Group(group_name="group", header="gr", footer="gr"))
    app.session.Logout()


def test_add_empty_group(app):
    app.session.Login(user_name="admin", password="secret")
    app.group.Create(Group(group_name="", header="", footer=""))
    app.session.Logout()






