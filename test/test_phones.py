import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_cont_list()[0]
    contact_from_edit_page = app.contact.get_cont_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_cont_view_page(app):
    contact_from_view_page = app.contact.get_cont_from_view_page(0)
    contact_from_edit_page = app.contact.get_cont_info_from_edit_page(0)
    assert contact_from_view_page.home_tel == contact_from_edit_page.home_tel
    assert contact_from_view_page.mobile_tel == contact_from_edit_page.mobile_tel
    assert contact_from_view_page.work_tel == contact_from_edit_page.work_tel
    assert contact_from_view_page.second_phone == contact_from_edit_page.second_phone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_tel, contact.work_tel, contact.mobile_tel, contact.second_phone]))))
