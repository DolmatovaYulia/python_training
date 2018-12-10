# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def Open_homepage(self, wd):
        wd.get("http://addressbook/")

    def Login(self, wd, user_name, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def Open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def Create_group(self, wd, group):
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        wd.find_element_by_name("submit").click()

    def Return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def Logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        wd = self.wd
        self.Open_homepage(wd)
        self.Login(wd, user_name="admin", password="secret")
        self.Open_groups_page(wd)
        self.Create_group(wd, Group(group_name="group", header="gr", footer="gr"))
        self.Return_to_groups_page(wd)
        self.Logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.Open_homepage(wd)
        self.Login(wd, user_name="admin", password="secret")
        self.Open_groups_page(wd)
        self.Create_group(wd, Group(group_name="", header="", footer=""))
        self.Return_to_groups_page(wd)
        self.Logout(wd)

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
