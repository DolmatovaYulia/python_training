from pytest_bdd import given, when, then
from model.group import Group
import random


@given('a group list')
def group_list(db):
    return db.get_group_list()


@given('a new group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(group_name=name, header=header, footer=footer)


@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.Create(new_group)


@then('the new group list is equal to the old group list with the added group')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@given('a non-empty group list')
def non_empty_group_list(app, db):
    if len(db.get_group_list()) == 0:
        app.group.Create(Group(group_name='name'))
    return db.get_group_list()


@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.Delete_group_by_id(random_group.id)


@then('the new group list is equal to the old group list without the deleted group')
def verify_group_deleted(app, db, check_ui, non_empty_group_list, random_group):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


@given('a new group with parameters')
def new_data():
    group = Group(group_name="test")
    return group


@when('I update the group from the list')
def update_group(app, new_data, random_group):
    new_data.id = random_group.id
    app.group.Update_group_by_id(new_data, random_group.id)


@then('the new group list is equal to the old group list with the modify group')
def verify_group_modify(app, db, check_ui, non_empty_group_list, random_group, new_data):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(random_group)
    old_groups.append(new_data)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

