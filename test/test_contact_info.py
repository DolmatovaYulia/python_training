import re
from random import randrange
from model.contact import Contact


# Сравнение информации о контактах с главной страницы сайта и БД
def test_assert_contact_from_homepage_and_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="firstname1", lastname="larstname1", address="address1", home="home 123 45 67",
                                   mobile="mob +123-45-67", work="work 3(050)-444-22-11", email="email1@email.com",
                                   email2="email2@email.com", email3="email3@email.com", phone2="second 098-765 33 11"))
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contact_from_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    print(contact_from_db)
    print(contact_from_homepage)
    for i in range(len(contact_from_db)):
        assert clear(contact_from_homepage[i].lastname) == clear(contact_from_db[i].lastname)
        assert clear(contact_from_homepage[i].firstname) == clear(contact_from_db[i].firstname)
        assert clear(contact_from_homepage[i].address) == clear(contact_from_db[i].address)
        assert contact_from_homepage[i].all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_db[i])
        assert clear(contact_from_homepage[i].all_emails_from_homepage) == clear(merge_emails_like_on_homepage(contact_from_db[i]))


# Сравнение номеров телефонов со страницы контактов и со страницы редактирования
def test_contact_on_homepage(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_editpage = app.contact.get_contact_info_from_editpage(index)
    assert clear(contact_from_homepage.lastname) == clear(contact_from_editpage.lastname)
    assert clear(contact_from_homepage.firstname) == clear(contact_from_editpage.firstname)
    assert clear(contact_from_homepage.address) == clear(contact_from_editpage.address)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_editpage)
    assert clear(contact_from_homepage.all_emails_from_homepage) == merge_emails_like_on_homepage(contact_from_editpage)


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

