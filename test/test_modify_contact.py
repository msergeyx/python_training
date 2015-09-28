__author__ = 'msergeyx'
from model.contact import Contact
from random import randrange


def test_full_modify_some_contact(app):
    if app.contact.contactcount() == 0:
        app.contact.create(Contact(firstname="hghjdsfni4389"))
    old_contacts = app.contact.get_cont_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="ertyuiklkmnbvc",
                                          middlename="dfg",
                                          lastname="sdfghjk",
                                          nick="rtlkjhkl",
                                          tytle="rty567,mnb",
                                          company="wertyuiop",
                                          address="xcvbntrewertyujnbvccfghj",
                                          home_tel="123456789",
                                          mobile_tel="987654321",
                                          work_tel="345643",
                                          fax="098789",
                                          birth_day="2",
                                          birth_month="October",
                                          birth_year="1985",
                                          second_addr="ertyukjbvcjkmnbbjkl,mnhghjkl",
                                          second_phone="45676789890",
                                          notes="erctvybuniercvybyygvbhjhdtrch")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.contactcount()
    new_contacts = app.contact.get_cont_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


"""def test_modify_first_contact_base_info(app):
    if app.contact.contactcount() == 0:
        app.contact.create(Contact(firstname="hghjdsfni4389"))
    old_contacts = app.contact.get_cont_list()
    app.contact.modify_first_contact(Contact(firstname="rtyjnbvyujk", lastname="hgffdfg", mobile_tel="67843234", birth_year="1386"))
    new_contacts = app.contact.get_cont_list()
    assert len(old_contacts) == len(new_contacts)"""
