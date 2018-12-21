from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def Return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def AddNew_page(self):
        wd = self.app.wd
        # Create contact
        wd.find_element_by_link_text("add new").click()

    def Contact_details(self, contact):
        # Add first name
        self.Change_field_value("firstname", contact.firstname)
        # Add middle name
        self.Change_field_value("middlename", contact.middlename)
        # Add last name
        self.Change_field_value("lastname", contact.lastname)
        # Add nickname
        self.Change_field_value("nickname", contact.nickname)
        # Add photo
        # self.Change_field_value("photo", contact.photo)
        # Add title
        self.Change_field_value("title", contact.title)
        # Add company
        self.Change_field_value("company", contact.company)
        # Add address
        self.Change_field_value("address", contact.address)
        # Add home telephone
        self.Change_field_value("home", contact.home)
        # Add mobile telephone
        self.Change_field_value("mobile", contact.mobile)
        # Add work telephone
        self.Change_field_value("work", contact.work)
        # Add fax
        self.Change_field_value("fax", contact.fax)
        # Add email 1
        self.Change_field_value("email", contact.email)
        # Add email 2
        self.Change_field_value("email2", contact.email2)
        # Add email 3
        self.Change_field_value("email3", contact.email3)
        # Add homepage
        self.Change_field_value("homepage", contact.homepage)
        # Add bday
        self.Change_field_value_select("bday", contact.bday)
        # Add bmonth
        self.Change_field_value_select("bmonth", contact.bmonth)
        # Add byear
        self.Change_field_value("byear", contact.byear)
        # Add aday
        self.Change_field_value_select("aday", contact.aday)
        # Add amonth
        self.Change_field_value_select("amonth", contact.amonth)
        # Add ayear
        self.Change_field_value("ayear", contact.ayear)
        # Add secondary address
        self.Change_field_value("address2", contact.address2)
        # Add secondary telephone
        self.Change_field_value("phone2", contact.phone2)
        # Add notes
        self.Change_field_value("notes", contact.notes)

    def Change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def Change_field_value_select(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).click()

    # Create new contact
    def Create(self, contact):
        wd = self.app.wd
        self.AddNew_page()
        self.Contact_details(contact)
        # Submit new contact
        wd.find_element_by_xpath("(//input[@name='submit'])").click()
        self.Return_to_homepage()
        self.contact_cache = None

    # Update first contact from homepage
    def Update_first_contact(self, contact):
        wd = self.app.wd
        self.app.Open_homepage()
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
        self.Contact_details(contact)
        # Submit new contact
        wd.find_element_by_name("update").click()
        wd.find_element_by_xpath("//div[@id='content']/div").click()
        self.Return_to_homepage()
        self.contact_cache = None

    # Update first contact from open details page
    def Update_first_contact_from_open_details(self, contact):
        wd = self.app.wd
        self.app.Open_homepage()
        wd.find_element_by_xpath("(//img[@alt='Details'])").click()
        wd.find_element_by_name("modifiy").click()
        self.Contact_details(contact)
        # Submit new contact
        wd.find_element_by_name("update").click()
        self.Return_to_homepage()
        self.contact_cache = None

    # Delete first contact from homepage
    def Delete_first_contact(self):
        wd = self.app.wd
        self.app.Open_homepage()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    # Delete all contacts from homepage
    def Delete_all_contacts(self):
        wd = self.app.wd
        self.app.Open_homepage()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    # Delete first contact from edit page
    def Delete_contact_from_edit(self):
        wd = self.app.wd
        self.app.Open_homepage()
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        self.Return_to_homepage()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.Open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.Open_homepage()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr")[1:]:
                cells = element.find_elements_by_xpath("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)


