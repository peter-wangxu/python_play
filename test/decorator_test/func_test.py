__author__ = 'wangp11'


def decorator_fun(my_func):
    def decorator(*args, **kwargs):
        print 'before ' + my_func.__name__
        print '1'
        print args
        print '2'
        print kwargs
        setattr(my_func, "New", "Test")
        r = my_func(*args, **kwargs)
        print 'after ' + my_func.__name__
        return r
    return decorator


@decorator_fun
def fun_under_test(hello):
    print "in fun_under_test"
    print hello


fun_under_test(hello='asdf')


def outer(y):
    def inner():
        x = y
        print x # 1
    return inner
foo1 = outer(1)
foo2 = outer(2)
foo2()
foo1()