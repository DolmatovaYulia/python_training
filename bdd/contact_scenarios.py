from pytest_bdd import scenario
from .contact_steps import *


@scenario('contact.features', 'Add new contact')
def test_add_new_contact():
    pass


@scenario('contact.features', 'Delete a contact')
def test_delete_contact():
    pass


@scenario('contact.features', 'Update a contact')
def test_update_contact():
    pass

