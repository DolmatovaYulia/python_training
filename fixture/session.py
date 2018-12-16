class SessionHelper:
    def __init__(self, app):
        self.app = app

    def Login(self, user_name, password):
        wd = self.app.wd
        self.app.Open_homepage()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def Logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, user_name):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "(" + user_name + ")"

    def ensure_Logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.Logout()

    def ensure_Login(self, user_name, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(user_name):
                return
            else:
                self.Logout()
        self.Login(user_name, password)


