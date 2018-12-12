from selenium import webdriver


# The class that contains all the helper methods.
class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def Open_homepage(self):
        wd = self.wd
        wd.get("http://addressbook/")

    def Login(self, user_name, password):
        wd = self.wd
        self.Open_homepage()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def Open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def Create_group(self, group):
        wd = self.wd
        self.Open_groups_page()
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
        self.Return_to_groups_page()

    def Return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def Logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def Destroy(self):
        self.wd.quit()
