# -*- coding: utf-8 -*-
import unittest
from contact import Contact
from application_for_contact import Application


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.Login(user_name="admin", password="secret")
        self.app.Create_new_contact(Contact(firstname="q", middlename="w", lastname="e", nickname="qwerty", photo="", title="qwerty",
                                        company="qwerty", address="qwe", home="123456", mobile="1234567890", work="654321", fax="",
                                        email="qwerty@qwe.rty", email2="qwerty", email3="qwerty1@qwe.rty", homepage="none", bday="1",
                                        bmonth="January", byear="1999", aday="4", amonth="March", ayear="2000", address2="qwerty", phone2="qwewqe", notes="zxc"))
        self.app.Logout()

    def test_add_empty_contact(self):
        self.app.Login(user_name="admin", password="secret")
        self.app.Create_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", photo="",title="", company="",address="",
                                        home="", mobile="", work="", fax="",email="", email2="", email3="", homepage="",
                                        bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="", phone2="", notes=""))
        self.app.Logout()

    def tearDown(self):
        self.app.Destroy()


if __name__ == "__main__":
    unittest.main()
