import subprocess
import threading
from threading import Thread
import time
import gevent
from gevent import subprocess as g_subprocess
from eventlet.green import subprocess as e_subprocess
import eventlet
def process():
    t = time.time()
    p = subprocess.Popen('sudo iscsiadm -m node -T '
                         'iqn.1992-04.com.emc:cx.apm00150602415.b0 '
                         '-p 192.168.1.60:3260 --login',
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         shell=True)
    out, err = p.communicate()
    end = time.time()
    thread_name = threading.currentThread().getName()
    print ('[%s]: %s seconds.' % (thread_name, str(end - t)))
    print ('[%s]: return code - %s' % (thread_name, p.returncode))
    print ('[%s]:  - %s' % (thread_name, ''.join([out, err])))


def gevent_process():
    t = time.time()
    p = g_subprocess.Popen(
        'sudo iscsiadm -m node -T '
        'iqn.1992-04.com.emc:cx.apm00150602415.b0 '
        '-p 192.168.1.60:3260 --login',
        stdin=g_subprocess.PIPE,
        stderr=g_subprocess.PIPE,
        stdout=g_subprocess.PIPE,
        shell=True)
    out, err = p.communicate()
    end = time.time()
    thread_name = threading.currentThread().getName()
    print ('[%s]: %s seconds.' % (thread_name, str(end - t)))
    print ('[%s]: return code - %s' % (thread_name, p.returncode))
    print ('[%s]:  - %s' % (thread_name, ''.join([out, err])))

def gevent_process_raw():
    t = time.time()
    p = gevent.subprocess.Popen(
        'sudo iscsiadm -m node -T '
        'iqn.1992-04.com.emc:cx.apm00150602415.b0 '
        '-p 192.168.1.60:3260 --login',
        stdin=gevent.subprocess.PIPE,
        stderr=gevent.subprocess.PIPE,
        stdout=gevent.subprocess.PIPE,
        shell=True)
    out, err = p.communicate()
    end = time.time()
    thread_name = threading.currentThread().getName()
    print ('[%s]: %s seconds.' % (thread_name, str(end - t)))
    print ('[%s]: return code - %s' % (thread_name, p.returncode))
    print ('[%s]:  - %s' % (thread_name, ''.join([out, err])))

def eventlet_process():
    t = time.time()
    p = e_subprocess.Popen(
        'sudo iscsiadm -m node -T '
        'iqn.1992-04.com.emc:cx.apm00150602415.b0 '
        '-p 192.168.1.60:3260 --login',
        stdin=e_subprocess.PIPE,
        stderr=e_subprocess.PIPE,
        stdout=e_subprocess.PIPE,
        shell=True)
    out, err = p.communicate()
    end = time.time()
    thread_name = threading.currentThread().getName()
    print ('[%s]: %s seconds.' % (thread_name, str(end - t)))
    print ('[%s]: return code - %s' % (thread_name, p.returncode))
    print ('[%s]:  - %s' % (thread_name, ''.join([out, err])))

def multi_thread():
    begin = time.time()
    threads = []
    for i in xrange(2):
        t = Thread(target=process, name='Thread-%s' % i)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end = time.time()

    print ("[Total]: %s seconds" % str(end - begin))


def multi_gevent():
    begin = time.time()
    events = []
    for i in xrange(2):
        t = gevent.spawn(gevent_process)
        events.append(t)

    gevent.joinall(events)
    end = time.time()
    print ("[Total]: %s seconds" % str(end - begin))

def multi_gevent_raw():
    begin = time.time()
    events = []
    for i in xrange(2):
        t = gevent.spawn(gevent_process_raw)
        events.append(t)

    gevent.joinall(events)
    end = time.time()
    print ("[Total]: %s seconds" % str(end - begin))

def multi_eventlet():
    begin = time.time()
    events = []
    for i in xrange(2):
        t = eventlet.greenthread.spawn(eventlet_process)
        events.append(t)

    for x in events:
        x.wait()
    end = time.time()
    print ("[Total]: %s seconds" % str(end - begin))

def multi_eventlet_pool():
    begin = time.time()
    pool = eventlet.GreenPool()
    for x in xrange(2):
        pool.imap(eventlet_process)
    pool.waitall()

    end = time.time()
    print ("[Total]: %s seconds" % str(end - begin))
#print "multi thread mode ==================="
#multi_thread()
#print "multi gevent mode ==================="
#multi_gevent()
#print "multi gevent mode(raw) ==================="
#multi_gevent_raw()

#print "multi eventlet mode ==================="
#multi_eventlet()
print "multi eventlet poolmode ==================="
multi_eventlet_pool()
