from model.group import Group


def test_edit_group(app):
    app.session.Login(user_name="admin", password="secret")
    app.group.Update_first_group(Group(group_name="group123", header="gr1", footer="gr2"))
    app.session.Logout()


def test_update_empty_group(app):
    app.session.Login(user_name="admin", password="secret")
    app.group.Update_first_group(Group(group_name="", header="", footer=""))
    app.session.Logout()
