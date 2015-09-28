__author__ = 'msergeyx'
from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_group_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # Init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # click edit
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_data)
        # click update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.gr_name)
        self.change_field_value("group_header", group.gr_header)
        self.change_field_value("group_footer", group.gr_footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(gr_name=text, id=id))
        return list(self.group_cache)
