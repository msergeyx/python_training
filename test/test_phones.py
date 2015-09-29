import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_cont_list()[0]
    contact_from_edit_page = app.contact.get_cont_info_from_edit_page(0)
    assert contact_from_home_page.home_tel == clear(contact_from_edit_page.home_tel)
    assert contact_from_home_page.mobile_tel == clear(contact_from_edit_page.mobile_tel)
    assert contact_from_home_page.work_tel == clear(contact_from_edit_page.work_tel)
    assert contact_from_home_page.second_phone == clear(contact_from_edit_page.second_phone)

def clear(s):
    return re.sub("[() -]", "", s)