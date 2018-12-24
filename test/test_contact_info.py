import re
from random import randrange


# Сравнение номеров телефонов со страницы контактов и со страницы редактирования
def test_contact_on_homepage(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_editpage = app.contact.get_contact_info_from_editpage(index)
    assert contact_from_homepage.lastname == contact_from_editpage.lastname
    assert contact_from_homepage.firstname == contact_from_editpage.firstname
    assert contact_from_homepage.address == contact_from_editpage.address
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_editpage)
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_editpage)


# Очищение строк от +, (, ), - (+7(923)111-22-33 = 79231112233)
def clear(s):
    return re.sub("[() -]", "", s)


# Склеивание строки телефонов
def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.home, contact.mobile, contact.work, contact.phone2]))))


# Склеивание строки с email-адресами
def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.email, contact.email2, contact.email3]))))

