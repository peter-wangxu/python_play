__author__ = 'wangp11'

import os

data_path = './'
d = open(data_path + 'data.txt')
lines = d.readlines()
num = 0.0
for n in lines:
    num += float(n)

print "total: %f" % num
print "avaerage: %f" % (num / len(lines))
