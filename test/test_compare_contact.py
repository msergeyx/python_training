__author__ = 'msergeyx'
import re
from random import randrange
from model.contact import Contact


def test_compare_contact_on_home_page(app):
    all_contacts = app.contact.get_cont_list()
    index = randrange(len(all_contacts))
    cont_from_home_page = app.contact.get_contact_info_from_home_page(index)
    cont_from_edit_page = app.contact.get_cont_info_from_edit_page(index)
    assert cont_from_home_page.firstname == cont_from_edit_page.firstname
    assert cont_from_home_page.lastname == cont_from_edit_page.lastname
    assert clear(cont_from_home_page.address) == clear(cont_from_edit_page.address)
    assert clear(cont_from_home_page.email) == clear(cont_from_edit_page.email)
    assert cont_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(cont_from_edit_page)


def test_compare_contact_on_home_page_with_db(app, db):
    contact_from_ui = sorted(app.contact.get_cont_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_cont_list(), key=Contact.id_or_max)
    for db_contact in range(len(contact_from_db)):
        for ui_contact in range(len(contact_from_ui)):
            assert contact_from_ui[ui_contact].id == contact_from_db[db_contact].id
            assert contact_from_ui[ui_contact].firstname == contact_from_db[db_contact].firstname
            assert contact_from_ui[ui_contact].lastname == contact_from_db[db_contact].lastname
            assert contact_from_ui[ui_contact].address == contact_from_db[db_contact].address
            assert contact_from_ui[db_contact].all_phones_from_home_page == "\n".join(filter(lambda x: x is not None,
                                                                                    [contact_from_db[db_contact].home_tel,
                                                                                     contact_from_db[db_contact].mobile_tel,
                                                                                     contact_from_db[db_contact].work_tel,
                                                                                     contact_from_db[db_contact].second_phone]))
        ui_contact += 1
    db_contact += 1



def clear(s):
    return re.sub("[. -+]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_tel, contact.mobile_tel, contact.work_tel, contact.second_phone]))))