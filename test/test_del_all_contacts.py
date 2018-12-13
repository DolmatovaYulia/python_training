def test_del_all_contacts(app):
    app.session.Login(user_name="admin", password="secret")
    app.contact.Delete_all_contacts()
    app.session.Logout()

