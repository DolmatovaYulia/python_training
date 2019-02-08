from model.group import Group
import random
import pytest


def test_update_group_name(app, db, check_ui):
    with pytest.allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.Create(Group(group_name="test"))
    with pytest.allure.step('Given a new group with parameters'):
        old_groups = db.get_group_list()
        group = Group(group_name="test")
    with pytest.allure.step('Given a random group from the list'):
        group_id = random.choice(old_groups)
    with pytest.allure.step('When I update the group %s from the list' % group):
        group.id = group_id.id
        app.group.Update_group_by_id(group, group_id.id)
    with pytest.allure.step('Then the new group list is equal to the old group list with the modify group'):
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups.remove(group_id)
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
