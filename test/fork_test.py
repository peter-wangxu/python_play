__author__ = 'wangp11'
import os
import time

print "my pid1: " + str(os.getpid())
child_id = os.fork()
if child_id == 0:
    print "Fork succeeded"
    time.sleep(10)

#print "child_id %d " % child_id
print "my pid2: " + str(os.getpid())
if child_id != 0:
    print "I am parent, ended at " + str(time.time())
else:
    print "I am child, ended at " + str(time.time())