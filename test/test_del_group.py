def test_del_group(app):
    app.session.Login(user_name="admin", password="secret")
    app.group.Delete_first_group()
    app.session.Logout()

