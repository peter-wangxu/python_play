import mymod


mymod.x = 1000

print mymod.x


reload(mymod)
print mymod.x


class T1est(object):
    x = 9
    def __init__(self):
        pass


t1 = T1est()

print t1.x

T1est.x = 10000
t2 = T1est()
print "=" * 10
print t2.x
print t1.x

print "=" * 10
t1.x = 999

T1est.x=222222

print t2.x
print t1.x