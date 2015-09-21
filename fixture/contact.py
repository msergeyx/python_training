__author__ = 'msergeyx'
from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def go_home(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title='Addressbook']").click()

    def create(self, contact):
        wd = self.app.wd
        # Init contact creation
        wd.find_element_by_link_text("add new").click()
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nick)
        self.change_field_value("title", contact.tytle)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_tel)
        self.change_field_value("mobile", contact.mobile_tel)
        self.change_field_value("work", contact.work_tel)
        self.change_field_value("fax", contact.fax)
        self.fill_bday_date(contact.birth_day)
        self.fill_bday_month(contact.birth_month)
        self.change_field_value("byear", contact.birth_year)
        self.change_field_value("address2", contact.second_addr)
        self.change_field_value("phone2", contact.second_phone)
        self.change_field_value("notes", contact.notes)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_homepage()

    def delete_first_cont(self):
        wd = self.app.wd
        self.go_home()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.go_home()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nick)
        self.change_field_value("title", contact.tytle)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_tel)
        self.change_field_value("mobile", contact.mobile_tel)
        self.change_field_value("work", contact.work_tel)
        self.change_field_value("fax", contact.fax)
        self.fill_bday_date(contact.birth_day)
        self.fill_bday_month(contact.birth_month)
        self.change_field_value("byear", contact.birth_year)
        self.change_field_value("address2", contact.second_addr)
        self.change_field_value("phone2", contact.second_phone)
        self.change_field_value("notes", contact.notes)
        wd.find_element_by_name("update").click()
        self.return_to_homepage()

    def fill_bday_month(self, text):
        wd = self.app.wd
        if text is not None:
            select = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[2]"))
            select.select_by_visible_text(text)

    def fill_bday_date(self, text):
        wd = self.app.wd
        if text is not None:
            select = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[1]"))
            select.select_by_visible_text(text)

    def contactcount(self):
        wd = self.app.wd
        self.go_home()
        return len(wd.find_elements_by_name("selected[]"))
