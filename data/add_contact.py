from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1", nickname="nickname1", address="address1", home="home1", mobile="mobile1", work="work1", email="email1", bday="1", bmonth="-", byear="1", aday="1", amonth="-", ayear="1"),
    Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2", nickname="nickname2", address="address2", home="home2", mobile="mobile2", work="work2", email="email2", bday="2", bmonth="-", byear="2", aday="2", amonth="-", ayear="2")
]


# Генератор случайных строк
def random_strint(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# Генератор числовых строк
def random_digits(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])


# Тестовые данные
testdata = [Contact(firstname="", middlename="", lastname="", nickname="", photo="", title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="", phone2="", notes="")] \
           + [Contact(firstname=random_strint("name", 20), middlename=random_strint("middlename", 20), lastname=random_strint("lastname", 20), nickname=random_strint("nickname", 20), title=random_strint("title", 20), company=random_strint("company", 30), address=random_strint("address", 30), home=random_digits("", 6), mobile=random_digits("", 11), work=random_digits("", 6), fax=random_digits("fax", 20), email=random_strint("email", 20), email2=random_strint("email2", 20), email3=random_strint("email3", 20), homepage=random_strint("homepage", 20), address2=random_strint("address2", 20), phone2=random_digits("", 10), notes=random_strint("notes", 30))
              for i in range(5)
]

