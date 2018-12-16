from model.contact import Contact


def test_del_contact_from_edit(app):
    if app.contact.count() == 0:
        app.contact.Create(Contact(firstname="test", middlename="test", lastname="test"))
    app.contact.Delete_contact_from_edit()
