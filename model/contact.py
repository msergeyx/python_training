__author__ = 'msergeyx'


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nick=None, tytle=None, company=None, address=None, home_tel=None, mobile_tel=None, work_tel=None,
                 fax=None, birth_day=None, birth_month=None, birth_year=None, second_addr=None, second_phone=None, notes=None):
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