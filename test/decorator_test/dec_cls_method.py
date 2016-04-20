def decorator_method(f):
    def inner(c):
        print "inner: ", c
        return f(c)

    return inner


class ClassUnderTest:
    C_New = "CCCCC"

    def __init__(self, a , b):
        self.a = a
        self.b = b

    @decorator_method
    def test_func(self):
        print 'in test_func'
        print self.a
        print self.b
        if hasattr(self, 'New'):
            print self.New


c = ClassUnderTest(1, 2)
c.test_func()