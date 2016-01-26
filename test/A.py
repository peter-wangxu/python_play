__author__ = 'wangp11'
AA=1

l1 = [13, 13]

n = 1
def print_l1():
    print "id A.py: %d" % id(l1)
    print l1

def extend_l1():
    l1.extend([1,31,31])
    print l1

def print_n():
    print n