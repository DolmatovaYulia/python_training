class GroupHelper:
    def __init__(self, app):
        self.app = app

    def Open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def Return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def Fill_group_form(self, group):
        wd = self.app.wd
        self.Change_field_value("group_name", group.group_name)
        self.Change_field_value("group_header", group.header)
        self.Change_field_value("group_footer", group.footer)

    def Change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def Create(self, group):
        wd = self.app.wd
        self.Open_groups_page()
        # Init group creation
        wd.find_element_by_name("new").click()
        self.Fill_group_form(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.Return_to_groups_page()

    def Select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def Delete_first_group(self):
        wd = self.app.wd
        self.Open_groups_page()
        self.Select_first_group()
        # Submit deletion
        wd.find_element_by_name("delete").click()
        self.Return_to_groups_page()

    def Update_first_group(self, group):
        wd = self.app.wd
        self.Open_groups_page()
        self.Select_first_group()
        # Submit deletion
        wd.find_element_by_name("edit").click()
        self.Fill_group_form(group)
        # Submit group creation
        wd.find_element_by_name("update").click()
        self.Return_to_groups_page()

    def count(self):
        wd = self.app.wd
        self.Open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

