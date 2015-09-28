__author__ = 'msergeyx'
from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.contactcount() == 0:
        app.contact.create(Contact(firstname="4567ghvhjk"))
    old_contacts = app.contact.get_cont_list()
    app.contact.delete_first_cont()
    new_contacts = app.contact.get_cont_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
