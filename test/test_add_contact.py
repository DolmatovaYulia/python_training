# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    # old_contacts = app.contact.get_contact_list()
    app.contact.Create(Contact(firstname="q", middlename="w", lastname="e", nickname="qwerty", photo="", title="qwerty",
                               company="qwerty", address="qwe", home="123456", mobile="1234567890", work="654321", fax="",
                               email="qwerty@qwe.rty", email2="qwerty", email3="qwerty1@qwe.rty", homepage="none", bday="1",
                               bmonth="January", byear="1999", aday="4", amonth="March", ayear="2000", address2="qwerty", phone2="qwewqe", notes="zxc"))
    # new_contacts = app.contact.get_contact_list()
    # assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    # old_contacts = app.contact.get_contact_list()
    app.contact.Create(Contact(firstname="", middlename="", lastname="", nickname="", photo="", title="", company="", address="",
                               home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="",
                               bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="", phone2="", notes=""))
    # new_contacts = app.group.get_group_list()
    # assert len(old_contacts) + 1 == len(new_contacts)


