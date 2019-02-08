from fixture.application import Application
from fixture.db import DBfixture
import json
import os.path
from model.group import Group
from model.contact import Contact


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config='target.json', browser='chrome'):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target['web']
        self.fixture = Application(browser=self.browser, base_url=web_config['baseUrl'])
        self.fixture.session.ensure_Login(user_name=web_config['user_name'], password=web_config['password'])
        db_config = self.target['db']
        self.dbfixture = DBfixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])

    def destroy_fixtures(self):
        self.fixture.Destroy()
        self.dbfixture.Destroy()

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def get_contact_list(self):
        return self.dbfixture.get_contact_list()

    def new_group(self, group_name, header, footer):
        return Group(group_name=group_name, header=header, footer=footer)

    def new_contact(self, firstname, lastname, address):
        return Contact(firstname=firstname, lastname=lastname, address=address)

    def create_group(self, group):
        self.fixture.group.Create(group)

    def create_contact(self, contact):
        self.fixture.contact.Create(contact)

    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    def contact_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Contact.id_or_max) == sorted(list2, key=Contact.id_or_max)

    def delete_group(self, group):
        self.fixture.group.Delete_group_by_id(group.id)

    def delete_contact(self, contact):
        self.fixture.contact.delete_contact_by_id(contact.id)

    def update_group(self, group, new_group):
        new_group.id = group.id
        self.fixture.group.Update_group_by_id(new_group, group.id)

    def update_contact(self, contact, new_contact):
        new_contact.id = contact.id
        self.fixture.contact.Update_contact_by_id(new_contact, contact.id)
