from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db, ormdb):
    if len(db.get_contact_list()) == 0:
        app.contact.Create(Contact(firstname="FIRSTNAME WITH GROUP"))
    if len(db.get_group_list()) == 0:
        app.group.Create(Group(group_name="GROUP"))
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    app.contact.add_contact_to_group_by_id(contact.id, group.id)
    assert contact == list(filter(lambda x: x.id == contact.id, ormdb.get_contacts_in_group(group)))[0]


def test_del_contact_from_group(app, db, ormdb):
    if len(db.get_contact_list()) == 0:
        app.contact.Create(Contact(firstname="FIRSTNAME WITH GROUP"))
    if len(db.get_group_list()) == 0:
        app.group.Create(Group(group_name="GROUP"))
    if len(ormdb.get_groups_with_contacts()) == 0:
        contact = random.choice(db.get_contact_list())
        group = random.choice(db.get_group_list())
        app.contact.add_contact_to_group_by_id(contact.id, group.id)
    group_to_del = random.choice(ormdb.get_groups_with_contacts())
    old_contacts_from_group = ormdb.get_contacts_in_group(group_to_del)
    contact_to_del = random.choice(old_contacts_from_group)
    app.contact.del_contact_from_group(contact_to_del.id, group_to_del.id)
    new_contacts_from_group = ormdb.get_contacts_in_group(group_to_del)
    old_contacts_from_group.remove(contact_to_del)
    assert sorted(old_contacts_from_group, key=Contact.id_or_max) == sorted(new_contacts_from_group, key=Contact.id_or_max)


