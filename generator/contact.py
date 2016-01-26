from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("fname", 15), middlename=random_string("mname", 15),
            lastname=random_string("lname", 15), nick=random_string("nick", 20), tytle=random_string("tytle", 15),
            company=random_string("company", 18), address=random_string("addr", 40), home_tel=random_string("htel", 15),
            mobile_tel=random_string("mtel", 15), work_tel=random_string("wtel", 15), fax=random_string("fax", 15),
            birth_day="2", birth_month="October", birth_year="1985", second_addr=random_string("saddr2", 40),
            second_phone=random_string("stel", 18), notes=random_string("note", 80))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
