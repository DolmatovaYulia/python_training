def test_del_contact(app):
    app.session.Login(user_name="admin", password="secret")
    app.contact.Delete_first_contact()
    app.session.Logout()

