from selenium.webdriver.support.select import Select


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
        wd = self.app.wd
        # Add first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # Add middle name
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # Add last name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # Add nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # Add photo
        wd.find_element_by_name("photo").clear()
        # Add title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        # Add company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        # Add address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # Add home telephone
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        # Add mobile telephone
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        # Add work telephone
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        # Add fax
        wd.find_element_by_name("fax").click()
        # Add email 1
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # Add email 2
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        # Add email 3
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        # Add homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # Add bday
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bday").click()
        # Add bmonth
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("bmonth").click()
        # Add byear
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        # Add aday
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_name("aday").click()
        # Add amonth
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("amonth").click()
        # Add ayear
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        # Add secondary address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        # Add secondary telephone
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        # Add notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    # Create new contact
    def Create(self, contact):
        wd = self.app.wd
        self.AddNew_page()
        self.Contact_details(contact)
        # Submit new contact
        wd.find_element_by_xpath("(//input[@name='submit'])").click()
        self.Return_to_homepage()

    # Update first contact from homepage
    def Update_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
        self.Contact_details(contact)
        # Submit new contact
        wd.find_element_by_name("update").click()
        wd.find_element_by_xpath("//div[@id='content']/div").click()
        self.Return_to_homepage()

    # Update first contact from open details page
    def Update_first_contact_from_open_details(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("(//img[@alt='Details'])").click()
        wd.find_element_by_name("modifiy").click()
        self.Contact_details(contact)
        # Submit new contact
        wd.find_element_by_name("update").click()
        self.Return_to_homepage()

    # Delete first contact from homepage
    def Delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.Return_to_homepage()

    # Delete all contacts from homepage
    def Delete_all_contacts(self):
        wd = self.app.wd
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.Return_to_homepage()

    # Delete first contact from edit page
    def Delete_contact_from_edit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        self.Return_to_homepage()




