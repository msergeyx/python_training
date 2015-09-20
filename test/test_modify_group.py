__author__ = 'msergeyx'
from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(gr_name="123", gr_header="345", gr_footer="456"))
    app.session.logout()
