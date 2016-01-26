# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_cont_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.contactcount()
    new_contacts = app.contact.get_cont_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
