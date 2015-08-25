# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.group_creation(Group(gr_name="uyrms", gr_header="sfjns", gr_footer="kdjfshn"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.group_creation(Group(gr_name="", gr_header="", gr_footer=""))
    app.logout()
