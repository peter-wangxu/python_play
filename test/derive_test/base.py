__author__ = 'wangp11'


class Base(object):
    g_test = 'aa'
    print 'id:',id(g_test)
    def __init__(self, test):
        print self.g_test
        print 'id-in:', id(self.g_test)
        self.g_test  = 'fffff'
        print 'id-in:', id(self.g_test)
        print test


class Derived1(Base):
    def __init__(self, qq):
        # super(Derived1, self).__init__(qq)
        print qq


print id(Derived1.g_test) == id(Base.g_test)
b = Base('bbb')
d = Derived1('ddd')

print "========="

print b.g_test
print d.g_test
print "========="

# b.g_test = 'changed'
Derived1.g_test  = 'd_changed'
print id(Derived1.g_test) == id(Base.g_test)
# d.g_test = 'd_origin'
# Derived1.g_test = 'd_changed'
print "========="
print d.g_test
print b.g_test
print "-========"
print Base.g_test

