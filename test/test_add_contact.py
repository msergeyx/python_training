# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=random_string("fname", 15), middlename=random_string("mname", 15),
            lastname=random_string("lname", 15), nick=random_string("nick", 20), tytle=random_string("tytle", 15),
            company=random_string("company", 18), address=random_string("addr", 40), home_tel=random_string("htel", 15),
            mobile_tel=random_string("mtel", 15), work_tel=random_string("wtel", 15), fax=random_string("fax", 15),
            birth_day="2", birth_month="October", birth_year="1985", second_addr=random_string("saddr2", 40), second_phone=random_string("stel", 18),
            notes=random_string("note", 80))
    for i in range(20)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_cont_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.contactcount()
    new_contacts = app.contact.get_cont_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
