__author__ = 'msergeyx'
from model.contact import Contact
import random


def test_del_some_contact(app, db, check_ui):
    if len(db.get_cont_list()) == 0:
        app.contact.create(Contact(firstname="4567ghvhjk"))
    old_contacts = db.get_cont_list()
    contact = random.choice(old_contacts)
    app.contact.delete_cont_by_id(int(contact.id))
    assert len(old_contacts) - 1 == app.contact.contactcount()
    new_contacts = db.get_cont_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max()) == sorted(app.group.get_group_list(), key=Contact.id_or_max())
