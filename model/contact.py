__author__ = 'msergeyx'
from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nick=None, tytle=None, company=None, address=None, home_tel=None, mobile_tel=None, work_tel=None,
                 fax=None, birth_day=None, birth_month=None, birth_year=None, second_addr=None, second_phone=None, notes=None, id=None, all_phones_from_home_page=None, email=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nick = nick
        self.tytle = tytle
        self.company = company
        self.address = address
        self.home_tel = home_tel
        self.mobile_tel = mobile_tel
        self.work_tel = work_tel
        self.fax = fax
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.second_addr = second_addr
        self.second_phone = second_phone
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.address, self.email, self.all_phones_from_home_page)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
