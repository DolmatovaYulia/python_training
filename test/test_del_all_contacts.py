from model.contact import Contact


def test_del_all_contacts(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.Create(Contact(firstname="test", middlename="test", lastname="test"))
    old_contacts = db.get_contact_list()
    app.contact.Delete_all_contacts()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - len(old_contacts) == len(db.get_contact_list()) - len(db.get_contact_list())
    old_contacts.clear()
    new_contacts.clear()
    assert old_contacts == new_contacts
    if check_ui:
        assert new_contacts == app.contact.get_contact_list()

