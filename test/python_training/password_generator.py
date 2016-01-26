import random


def create_password_generator(keys):
    inner_keys = ""
    def inner(length):
        inner_keys
        password = ''
        for x in xrange(length):
            password += random.choice(keys)
        return password
    return inner



alpha_password = create_password_generator('abcde')
print alpha_password(5)
print alpha_password(3)
numeric_password = create_password_generator('12345')
print numeric_password(5)
print numeric_password(3)