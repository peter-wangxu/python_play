from unittest import TestCase
from mock import patch


class Product(object):
    pass


@patch('__main__.Product')
class MyTest(TestCase):

    def test_one(self, MockSomeClass):
        self.assertTrue(Product is MockSomeClass)
        print "Success in mock class"

    def test_two(self, MockSomeClass):
        self.assertTrue(Product is MockSomeClass)
        print "Success in mock class"

    def not_a_test(self):
        return 'something'

MyTest('test_one').test_one()
MyTest('test_two').test_two()
print MyTest('test_two').not_a_test()