__author__ = 'msergeyx'
from model.contact import Contact
from random import randrange


def test_del_first_contact(app):
    if app.contact.contactcount() == 0:
        app.contact.create(Contact(firstname="4567ghvhjk"))
    old_contacts = app.contact.get_cont_list()
    index = randrange(len(old_contacts))
    app.contact.delete_cont_by_index(index)
    assert len(old_contacts) - 1 == app.contact.contactcount()
    new_contacts = app.contact.get_cont_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
