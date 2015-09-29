__author__ = 'msergeyx'
from model.contact import Contact
from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def go_home(self):
        wd = self.app.wd
        if wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0:
            return
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
        self.cont_cache = None

    def delete_first_cont(self):
        self.delete_cont_by_index(0)

    def select_cont_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_cont_by_index(self, index):
        wd = self.app.wd
        self.go_home()
        self.select_cont_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.cont_cache = None

    def select_first_cont(self):
        self.select_cont_by_index(0)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.go_home()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
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
        self.cont_cache = None

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

    cont_cache = None

    def get_cont_list(self):
        if self.cont_cache is None:
            wd = self.app.wd
            self.go_home()
            self.cont_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                elem_info = element.find_elements_by_tag_name('td')
                fname = elem_info[2].text
                lname = elem_info[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = elem_info[5].text.splitlines()
                self.cont_cache.append(Contact(firstname=fname, lastname=lname, id=id, home_tel=all_phones[0],
                                               mobile_tel=all_phones[1], work_tel=all_phones[2], second_phone=all_phones[3]))
        return list(self.cont_cache)

    def open_cont_to_edit_by_index(self, index):
        wd = self.app.wd
        self.go_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_cont_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_cont_to_edit_by_index(index)
        fname = wd.find_element_by_name("firstname").get_attribute("value")
        lname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_tel = wd.find_element_by_name("home").get_attribute("value")
        mobile_tel = wd.find_element_by_name("mobile").get_attribute("value")
        work_tel = wd.find_element_by_name("work").get_attribute("value")
        sec_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=fname, lastname=lname, id=id, home_tel=home_tel, mobile_tel=mobile_tel, work_tel=work_tel, second_phone=sec_phone)