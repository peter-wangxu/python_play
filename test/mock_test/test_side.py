__author__ = 'wangp11'
import mock

from mock import Mock


def side_1(*args, **kwargs):
    print args
    print kwargs
    return 1

test1 = Mock(side_effect=side_1)

test1(1,35,test='11')

test1.assert_has_calls(mock.call(1, 35, test='11'))


class TestCaseBase(object):
    KEYS = [1, 3]
    def __init__(self):
        pass

    def test(self):
        for k in self.KEYS:
            print k
        print ''

    @staticmethod
    def static_test(p1):
        print p1

    def call_static(self):
        self.__class__.static_test(1)


t = TestCaseBase()
t.test()
print id(t)
t.call_static()