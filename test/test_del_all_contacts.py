from model.contact import Contact


def test_del_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.Create(Contact(firstname="test", middlename="test", lastname="test"))
    app.contact.Delete_all_contacts()

