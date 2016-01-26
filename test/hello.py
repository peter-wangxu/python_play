__author__ = 'wangp11'

'''
Created on Aug 15, 2014

@author: wangp11
'''
A='B'

class FakeTest(dict):

    CONST = 'TEST'
    def __init__(self, values):
        self.values = values

    def __getattr__(self, name):
        print("Calling __getarrt__")
        print self.CONST
        return self.values[name]


    def __getitem__(self, key):
        print("Calling __getitem__")
        if key in self.values:
            return self.values[key]
        raise NotImplementedError()


t = {'k1': 'v1'}
f1 = FakeTest(t)

print f1.k1
print f1['k1']
print f1.get('k1')


try:
    x = 1/0
except Exception as ex:
    print('not excuse: %s' + ex.message)