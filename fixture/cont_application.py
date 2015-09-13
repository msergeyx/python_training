__author__ = 'msergeyx'

from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper


class ContApplication():
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_homepage(self):
        wd = self.wd
        # Open homepage
        wd.get("http://localhost/addressbook/")

    def destroying(self):
        self.wd.quit()