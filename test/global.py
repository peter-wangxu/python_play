__author__ = 'wangp11'

from A import *

def func():

    global l1
    print id(l1)
    print l1
    #l1 = [3, 2]
    print l1
    print id(l1)

def func2():
    global n
    print id(n)
    n = 23
    print id(n)

func()

l1.extend([66, 77, 88])
print l1
print "id global.py : %d" % id(l1)
print_l1()
extend_l1()
print_l1()


def x_x():
    not_set = 1
    print not_set
print "==============="
func2()
print n
print_n()