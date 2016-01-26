__author__ = 'wangp11'


class LUN(object):
    def __init__(self, name, size):
        self._name = name
        self._size = size

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value + '_new'


lun1 = LUN('test', 2)

print "get property"
# print lun1._name
print lun1.name


print "set property"
lun1.name = 'sate'


print lun1.name
print "_name"
print lun1._name



class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x


    @x.deleter
    def x(self):
        del self._x

print 'before'
c = C()
c.x
print 'after'
c.x = 'nbew'
print c.x