from model.contact import Contact


def test_del_contact_from_edit(app):
    if app.contact.count() == 0:
        app.contact.Create(Contact(firstname="test", middlename="test", lastname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.Delete_contact_from_edit()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

