# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="ertyuiklkmnbvc",
                                          middlename="dfg",
                                          lastname="sdfghjk",
                                          nick="rtlkjhkl",
                                          tytle="rtyuik,mnb",
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
