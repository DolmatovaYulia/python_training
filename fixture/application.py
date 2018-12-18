from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


# The class that contains all the helper methods.
class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def Open_homepage(self):
        wd = self.wd
        if not (wd.current_url.endswith("http://addressbook/") and len(wd.find_elements_by_name("MassCB")) > 0):
            wd.get("http://addressbook/")

    def Destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except ():
            return False


