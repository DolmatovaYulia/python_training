# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.Login(user_name="admin", password="secret")
    app.contact.Update_first_contact(Contact(firstname="q1", middlename="w1", lastname="e1", nickname="qwerty1", photo="", title="qwerty1",
                               company="qwerty1", address="qwe1", home="1234561", mobile="12345678901", work="6543211", fax="456789",
                               email="qwerty1@qwe.rty", email2="qwerty1", email3="qwerty1@qwe1.rty", homepage="123", bday="11",
                               bmonth="January", byear="1990", aday="14", amonth="March", ayear="2004", address2="qwerty1", phone2="qwewqe1", notes="zxc123"))
    app.session.Logout()
