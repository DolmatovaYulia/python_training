from model.group import Group


def test_update_group(app):
    app.group.Update_first_group(Group(group_name="group123", header="gr1", footer="gr2"))


def test_update_empty_group(app):
    app.group.Update_first_group(Group(group_name="", header="", footer=""))


def test_update_group_name(app):
    app.group.Update_first_group(Group(group_name="new group"))


def test_update_group_header(app):
    app.group.Update_first_group(Group(header="New header"))


