__author__ = 'msergeyx'
from model.contact import Contact


def test_full_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="ertyuiklkmnbvc",
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
                                          notes="erctvybuniercvybyygvbhjhdtrch"))
    app.session.logout()


def test_modify_first_contact_base_info(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="rtyjnbvyujk", lastname="57hgffdfg", mobile_tel="67843234", birth_year="1386"))
    app.session.logout()
