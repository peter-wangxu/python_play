

TestClass = type('TestClass', (), dict(i=4))

instance = TestClass()
print instance.i
print type(TestClass)
print type(instance)


Foo = type('Foo', (TestClass,), {'get_i': lambda self: self.i})


foo = Foo()
print "direct: ", Foo.i
print foo.get_i()


class InterfaceMeta(type):
    def __new__(cls, name, parents, dct):
        if 'class_id' not in dct:
            dct['class_id'] = name.lower()
        if 'file' in dct:
            filename = dct['file']
            dct['file'] = open(filename, 'w')
        return super(InterfaceMeta, cls).__new__(cls, name, parents, dct)


Interface = InterfaceMeta('Interface', (), dict(file='tmp.txt'))

#
# class Interface():
#     __metaclass__ = InterfaceMeta
#     file = 'foo.txt'

print Interface.class_id
print Interface.file


print type(Interface)