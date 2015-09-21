__author__ = 'msergeyx'
from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.contactcount() == 0:
        app.contact.create(Contact(firstname="4567ghvhjk"))
    app.contact.delete_first_cont()
