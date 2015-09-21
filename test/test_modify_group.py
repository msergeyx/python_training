__author__ = 'msergeyx'
from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(gr_name="ghj", gr_header="gnkl", gr_footer="jhb"))
    app.group.modify_first_group(Group(gr_name="123", gr_header="345", gr_footer="456"))


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(gr_name="ghj", gr_header="gnkl", gr_footer="jhb"))
    app.group.modify_first_group(Group(gr_name="dfjknk"))
