from model.group import Group
import random


def test_update_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.Create(Group(group_name="test"))
    old_groups = db.get_group_list()
    group = Group(group_name="test")
    group_id = random.choice(old_groups)
    group.id = group_id.id
    app.group.Update_group_by_id(group, group_id.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(group_id)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
