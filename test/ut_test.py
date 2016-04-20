import unittest
import mock

class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "SetupClass"

    def tearDown(self):
        print "tearDown." + self._testMethodName

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO1')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_cli(self):
        from vnxCliApi.vnx.resource.system import VNXSystem
        VNXSystem.__init__ = mock.Mock(return_value=None)
        # vnx = VNXSystem('192.168')
        VNXSystem.__init__.assert_has_calls([mock.call('192.168')])
        # self.assertEqual(None, vnx)

