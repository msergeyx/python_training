# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(gr_name="uyrms", gr_header="sfjns", gr_footer="kdjfshn"))


def test_add_empty_group(app):
    app.group.create(Group(gr_name="", gr_header="", gr_footer=""))
