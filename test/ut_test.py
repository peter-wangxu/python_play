import unittest


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


