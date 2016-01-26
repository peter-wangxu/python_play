import time

import gevent
import urllib2
import simplejson as json
import threading
import gevent.monkey
gevent.monkey.patch_socket()

THREAD_NUM = 150
COUNT = 100000

def fetch(pid):
    start = time.time()
    response = urllib2.urlopen('http://sdiehl.github.io/gevent-tutorial/')
    result = response.read()
    #json_result = json.loads(result)
    #datetime = json_result['datetime']

    print('Process %s: %s\n' % (pid, time.time()-start))
    #return json_result['datetime']


def compute(count):
    tmp = count
    # start = time.time()
    while count > 0:
        count -= 1
    # print('Process %s: %s\n' % (tmp, time.time()-start))


def synchronous():
    for i in range(1, THREAD_NUM):
        fetch(i)


def asynchronous():
    threads = []
    for i in range(1,THREAD_NUM):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)


def async_cpu():
    threads = []
    for i in range(1,THREAD_NUM):
        threads.append(gevent.spawn(compute, COUNT))
    gevent.joinall(threads)


class UrlThread(threading.Thread):
    # IO threads
    def __init__(self, index):
        super(UrlThread, self).__init__()
        self.index = index

    def run(self):
        fetch(self.index)


class CPUThread(threading.Thread):
    # Cpu-bound threads
    def __init__(self, count):
        super(CPUThread, self).__init__()
        self.count = count

    def run(self):
        while self.count > 0:
            self.count -= 1


def async_thread(thread_class):
    threads = []
    for i in range(1, THREAD_NUM):
        # t = threading.Thread(target=fetch, args=[i])
        t = thread_class(COUNT)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


# print('Synchronous:')
# t0 = time.time()
# synchronous()
# print ('cost:%s' % (time.time() - t0))
# print('Asynchronous:')
# t1 = time.time()
# asynchronous()
# print ('cost:%s' % (time.time() - t1))
print('Asynchronous(Thread):')
t2 = time.time()
async_thread(CPUThread)
print ('cost:%s' % (time.time() - t2))

print('Asynchronous(cpu-bound, gevent):')
t3 = time.time()
async_cpu()
print ('cost:%s' % (time.time() - t3))