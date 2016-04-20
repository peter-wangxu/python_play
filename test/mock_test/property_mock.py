import mock
__author__ = 'wangp11'


class Test(object):
    test = ""
    def __init__(self):
        test = "OK"

    def print_test(self):
        print self.test


t = Test()
print t.test
with mock.patch('__main__.Test.test', mock.PropertyMock(return_value="TestOK")):
    t = Test()
    print t.test


