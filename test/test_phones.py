import re


# Сравнение номеров телефонов со страницы контактов и со страницы редактирования
def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_editpage = app.contact.get_contact_info_from_editpage(0)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_editpage)


# Сравнение номеров телефонов со страницы контактов и со страницы просмотра контакта
def test_phones_on_contact_viewpage(app):
    contact_from_viewpage = app.contact.get_contact_from_viewpage(0)
    contact_from_editpage = app.contact.get_contact_info_from_editpage(0)
    assert contact_from_viewpage.home == contact_from_editpage.home
    assert contact_from_viewpage.work == contact_from_editpage.work
    assert contact_from_viewpage.mobile == contact_from_editpage.mobile
    assert contact_from_viewpage.phone2 == contact_from_editpage.phone2


# Очищение строк от +, (, ), - (+7(923)111-22-33 = 79231112233)
def clear(s):
    return re.sub("[() -]", "", s)


# Склеивание строки телефонов
def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.home, contact.mobile, contact.work, contact.phone2]))))

