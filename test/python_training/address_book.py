import json

address = {
    'given_name': '',
    'family_name': '',
    'phone_number': '',
    'email': ''
}

help_str = """
q -- quit
a -- add a new person
l -- list all of the people
f -- find all matches
r -- read from disk
w -- write the current contents to disk
"""


def add():
    given_name = raw_input("Given Name:")
    family_name = raw_input("Family Name:")
    phone_number = raw_input("Phone Number:")
    email = raw_input("Email:")
    tmp = address.copy()
    tmp['given_name'] = given_name
    tmp['family_name'] = family_name
    tmp['phone_number'] = phone_number
    tmp['email'] = email
    return tmp


def write(data):
    f = open("data.txt", 'a+')
    for d in data:
        f.write(json.dumps(d) + "\n")
    f.close()


def read():
    nn = []
    for d in open("data.txt", 'r'):
        nn.append(json.loads(d))
    return nn


def find_addr(find_str, data_list):
    for data in data_list:
        pass


cache = []
while True:
    command = raw_input("")
    if command in 'qalfrw':
        if command == 'q':
            break
        elif command == 'a':
            cache.append(add())
        elif command == 'l':
            print "Current Addresses:\n"
            print cache
        elif command == 'f':
            find_addr(raw_input("Input what you want:"))
        elif command == 'r':
            cache = read()
            print "Loading from disk, DONE!"
        elif command == 'w':
            write(cache)
            cache = []
        else:
            print "Should never goes here!"
    else:
        print "Invalid command!"
        print help_str

