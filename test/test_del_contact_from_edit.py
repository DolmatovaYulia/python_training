def test_del_contact_from_edit(app):
    app.session.Login(user_name="admin", password="secret")
    app.contact.Delete_contact_from_edit()
    app.session.Logout()

