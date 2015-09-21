__author__ = 'msergeyx'
from fixture.application import Application
import pytest


fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    elif not fixture.is_valid():
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def final():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(final)
    return fixture