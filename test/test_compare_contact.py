__author__ = 'msergeyx'
import re
from random import randrange


def test_compare_contact_on_home_page(app):
    all_contacts = app.contact.get_cont_list()
    index = randrange(len(all_contacts))
    get_contact_info_from_home_page(index)
    full_info_about_contact_from_edit_page(index)


def clear(s):
    return re.sub("[() -]", "", s)

