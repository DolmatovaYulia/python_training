# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_update_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.Create(Contact(firstname="new firstname"))
    old_contacts = db.get_contact_list()
    contact_id = random.choice(old_contacts)
    contact = Contact(firstname="q1", middlename="w1", lastname="e1", nickname="qwerty1", photo="", title="qwerty1", company="qwerty1", address="qwe1", home="1234561", mobile="12345678901", work="6543211", fax="456789", email="qwerty1@qwe.rty", email2="qwerty1", email3="qwerty1@qwe1.rty", homepage="123", bday="11", bmonth="January", byear="1990", aday="14", amonth="March", ayear="2004", address2="qwerty1", phone2="qwewqe1", notes="zxc123")
    contact.id = contact_id.id
    app.contact.Update_contact_by_id(contact, contact_id.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(contact_id)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_update_contact_from_details(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.Create(Contact(lastname="new lastname"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="q2", middlename="w2", lastname="e2", nickname="qwerty2", photo="", title="qwerty2", company="qwerty2", address="qwe2", home="123456122", mobile="1234567890221", work="65432112", fax="4567892", email="qwerty12@qwe.rty", email2="qwerty12", email3="qwerty12@qwe1.rty", homepage="1232", bday="22", bmonth="May", byear="1992", aday="22", amonth="October", ayear="2008", address2="qwerty12", phone2="qwewqe12", notes="zxc123123")
    contact_id = random.choice(old_contacts)
    contact.id = contact_id.id
    app.contact.Update_contact_from_details_by_id(contact, contact_id.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(contact_id)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)



