__author__ = 'msergeyx'
import re
from random import randrange


def test_compare_contact_on_home_page(app):
    all_contacts = app.contact.get_cont_list()
    index = randrange(len(all_contacts))
    cont_from_home_page = app.contact.get_contact_info_from_home_page(index)
    cont_from_edit_page = app.contact.get_cont_info_from_edit_page(index)
    assert cont_from_home_page.firstname == cont_from_edit_page.firstname
    assert cont_from_home_page.lastname == cont_from_edit_page.lastname
    assert cont_from_home_page.address == cont_from_edit_page.address
    assert clear_mail(cont_from_home_page.email) == clear_mail(cont_from_edit_page.email)
    assert cont_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(cont_from_edit_page)


def clear_mail(s):
    return re.sub("[. -+]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_mail(x),
                                filter(lambda x: x is not None,
                                       [contact.home_tel, contact.mobile_tel, contact.work_tel, contact.second_phone]))))