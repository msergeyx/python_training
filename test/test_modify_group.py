__author__ = 'msergeyx'
from model.group import Group
from random import randrange


def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(gr_name="ghj", gr_header="gnkl", gr_footer="jhb"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(gr_name="123", gr_header="345", gr_footer="456")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


"""def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(gr_name="ghj", gr_header="gnkl", gr_footer="jhb"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(gr_name="dfjknk"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
"""