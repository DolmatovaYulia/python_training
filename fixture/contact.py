from selenium.webdriver.support.select import Select
from model.contact import Contact
import re


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

    # Поля для создания/редактирования контакта
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

    # Создание контакта
    def Create(self, contact):
        wd = self.app.wd
        self.AddNew_page()
        self.Contact_details(contact)
        # Submit new contact
        wd.find_element_by_xpath("(//input[@name='submit'])").click()
        self.Return_to_homepage()
        self.contact_cache = None

    # Открыть контакт для просмотра
    def Open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.Open_homepage()
        # wd.find_element_by_xpath("//tr[" + str(index + 2) + "]/td[7]/a/img").click()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    # Выбор контакта для редактирования по индексу
    def select_contact_by_index_to_update(self, index):
        wd = self.app.wd
        self.app.Open_homepage()
        # wd.find_element_by_xpath("//tr[" + str(index + 2) + "]/td[8]/a/img").click()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def Update_first_contact(self):
        self.Update_contact_by_index(0)

    # Редактирование контакта по индексу
    def Update_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.select_contact_by_index_to_update(index)
        self.Contact_details(contact)
        # Submit new contact
        wd.find_element_by_name("update").click()
        self.Return_to_homepage()
        self.contact_cache = None

    def Update_first_contact_from_open_details(self):
        self.Update_contact_from_details_by_index(0)

    # Открытие редактирования контакта через страницу просмотра
    def Update_contact_from_details_by_index(self, contact, index):
        wd = self.app.wd
        self.Open_contact_view_by_index(index)
        wd.find_element_by_name("modifiy").click()
        self.Contact_details(contact)
        # Submit new contact
        wd.find_element_by_name("update").click()
        self.Return_to_homepage()
        self.contact_cache = None

    # Выбор контакта для удаления по индексу
    def select_contact_by_index_to_delete(self, index):
        wd = self.app.wd
        self.app.Open_homepage()
        wd.find_elements_by_name("selected[]")[index].click()

    def Delete_first_contact(self):
        self.Delete_contact_by_index(0)

    # Удаление контакта по индексу
    def Delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index_to_delete(index)
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    # Удаление всех контактов на странице
    def Delete_all_contacts(self):
        wd = self.app.wd
        self.app.Open_homepage()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    # Удаление первого контакта через страницу редактирования
    def Delete_contact_from_edit(self):
        self.Delete_contact_from_edit_by_index(0)

    # Удаление контакта через страницу редактирования по индексу
    def Delete_contact_from_edit_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index_to_update(index)
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        self.Return_to_homepage()
        self.contact_cache = None

    # Счетчик контактов
    def count(self):
        wd = self.app.wd
        self.app.Open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    # Глобальная переменная для получения списка контактов
    contact_cache = None

    # Получение списка контактов
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.Open_homepage()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_xpath("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                                                  all_phones_from_homepage=all_phones, all_emails_from_homepage=all_emails))
        return list(self.contact_cache)

    # Получение информации о контакте через страницу редактирования по индексу
    def get_contact_info_from_editpage(self, index):
        wd = self.app.wd
        self.select_contact_by_index_to_update(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        # Получение номеров телефонов
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        # Получение email-адресов
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                       home=home, work=work, mobile=mobile, phone2=phone2,
                       email=email, email2=email2, email3=email3)

    # Получение информации о контакте через страницу просмотра по индексу
    def get_contact_from_viewpage(self, index):
        wd = self.app.wd
        self.Open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2)

