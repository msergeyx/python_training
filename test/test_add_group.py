# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(gr_name="uyrms", gr_header="sfjns", gr_footer="kdjfshn"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(gr_name="", gr_header="", gr_footer=""))
    app.session.logout()
