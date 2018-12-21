from model.contact import Contact


def test_del_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.Create(Contact(firstname="test", middlename="test", lastname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.Delete_all_contacts()
    assert len(old_contacts) - len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:] = []
    assert old_contacts == new_contacts
