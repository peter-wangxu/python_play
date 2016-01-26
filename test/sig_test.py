__author__ = 'wangp11'



import signal
import os
import time

def receive_signal_1(signum, stack):
    print "111"
    print 'Received:', signum

def receive_signal_2(signum, stack):
    print "222"
    print 'Received:', signum

def receive_signal_3(signum, stack):
    print "333"
    print 'Received:', signum

def receive_signal_4(signum, stack):
    print "444"
    print 'Received:', signum

signal.signal(signal.SIGTERM, receive_signal_1)
signal.signal(signal.SIGILL, receive_signal_2)
signal.signal(signal.SIGINT, receive_signal_3)
signal.signal(signal.SIGABRT, receive_signal_4)

print 'My PID is:', os.getpid()

while True:
    print 'Waiting...'
    time.sleep(3)