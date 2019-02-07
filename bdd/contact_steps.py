from pytest_bdd import given, when, then
from model.contact import Contact
import random
import re


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a new contact with <firstname>, <lastname>, <address>, <home>, <mobile>, <work> and <email>')
def new_contact(firstname, lastname, address, home, mobile, work, email):
    return Contact(firstname=firstname, lastname=lastname, address=address, home=home, mobile=mobile, work=work, email=email)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.Create(new_contact)


@then('the new contact list is equal to the old contact list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.Create(Contact(firstname='firstname'))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old contact list without the deleted contact')
def verify_ccontact_deleted(app, db, check_ui, non_empty_contact_list, random_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


@given('a new contact with parameters')
def new_data():
    contact = Contact(firstname='test_firstname', lastname='test_lastname', address='test_address')
    return contact


@when('I update the contact from the list')
def update_contact(app, new_data, random_contact):
    new_data.id = random_contact.id
    print('gfd')
    return app.contact.Update_contact_by_id(new_data, random_contact.id)


@then('the new contact list is equal to the old contact list with the modify contact')
def verify_contact_modify(app, db, check_ui, non_empty_contact_list, random_contact, new_data):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(random_contact)
    old_contacts.append(new_data)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

