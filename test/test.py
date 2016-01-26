#!/usr/bin/env python

def outer():
    x = 100
    def inner():
        y = 1000
        print "1: id(y) = {}".format(id(y))
        print "In inner, x = {}".format(x)
        # x = 200
    inner()

outer()
#print "2:id(y) = {}".format(id(y))
y =200
print "3:id(y) = {}".format(id(y))