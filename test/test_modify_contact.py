__author__ = 'msergeyx'


def test_full_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact()
    app.session.logout()
