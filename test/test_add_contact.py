# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


# Генератор случайных строк
def random_strint(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# Генератор числовых строк
def random_digits(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])


# Тестовые данные
testdata = [Contact(firstname="", middlename="", lastname="", nickname="", photo="", title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="", phone2="", notes="")] \
           + [Contact(firstname=random_strint("name", 20), middlename=random_strint("middlename", 20), lastname=random_strint("lastname", 20), nickname=random_strint("nickname", 20), title=random_strint("title", 20), company=random_strint("company", 30), address=random_strint("address", 30), home=random_digits("", 6), mobile=random_digits("", 11), work=random_digits("", 6), fax=random_digits("fax", 20), email=random_strint("email", 20), email2=random_strint("email2", 20), email3=random_strint("email3", 20), homepage=random_strint("homepage", 20), address2=random_strint("address2", 20), phone2=random_digits("", 10), notes=random_strint("notes", 30))
              for i in range(5)
]


# Передаются название параметра, куда должны передаваться тестовые данные, источник данных
# и список с текстовым представлением данных
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.Create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


