# import copy
#
#
# class TestCopy(object):
#     p1 = 'test'
#     p2 = 'test2'
#
#     def __init__(self):
#         self.qq = 'qq'
#         self.pp = 'pp'
#
#
# original = TestCopy()
# print original
# original.qq = 'mm'
#
# copy1 = copy.deepcopy(original)
# TestCopy.p1 = 'p1'
# original.qq = 'zz'
#
# print copy1


class Test1:
    def __init__(self):
        pass

    def fun1(self, func):
        func()


class Test2:
    def __init__(self, data):
        self.data = data

    def inner(self):
        print "inner", self.data


t2 = Test2('hello')

t1 = Test1()
t1.fun1(t2.inner)