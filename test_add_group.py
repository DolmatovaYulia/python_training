# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    # Initialization. Making fixtures
    fixture = Application()
    # How the fixture should be destroyed
    request.addfinalizer(fixture.Destroy)
    return fixture


# Test method that takes a fixture as a parameter
def test_add_group(app):
    app.Login(user_name="admin", password="secret")
    app.Create_group(Group(group_name="group", header="gr", footer="gr"))
    app.Logout()


def test_add_empty_group(app):
    app.Login(user_name="admin", password="secret")
    app.Create_group(Group(group_name="", header="", footer=""))
    app.Logout()

