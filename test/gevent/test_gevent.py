# encoding=utf-8
import gevent
from gevent.queue import Queue  #类似于内置的Queue
import time

tasks = Queue() #队列实例


def foo():
    print('Running in foo')
    gevent.sleep(0)
    time.sleep(10)
    print('Explicit context switch to foo again')
    tasks.put_nowait(True)

def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    time.sleep(10)
    print('Implicit context switch back to bar')
    tasks.put_nowait(False)

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])
r = []
while not tasks.empty():
    r.append(tasks.get_nowait())
all(r)