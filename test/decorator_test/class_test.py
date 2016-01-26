__author__ = 'wangp11'


def decorator_class(cls_under_test):
    def decorator(*args, **kwargs):
        print args
        print kwargs
        for attr_name, attr_val in cls_under_test.__dict__.items():
            print attr_name, attr_val
        setattr(cls_under_test, 'New', 'Test')
        return cls_under_test
    return decorator

@decorator_class
class ClassUnderTest:
    C_New = "CCCCC"

    def __init__(self, a , b):
        self.a = a
        self.b = b
        print "in __init__"

    def test_func(self):
        print 'in test_func'
        print self.a
        print self.b
        if hasattr(self, 'New'):
            print self.New


c = ClassUnderTest(1, 2)

c.test_func()

# print "is instance level: {}".format(c.New)
print "is Class level: {}".format(ClassUnderTest.C_New)