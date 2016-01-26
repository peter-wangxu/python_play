import six


def change_behave(func):
    # @six.wraps(func)
    def decorator(*args, **kwargs):
        # print "new message"
        cmd = func()
        # print "this is output for: {}".format(cmd)
        return False
    return decorator


@change_behave
def test_under():
    # print "This default message"
    return "command to execute"

@change_behave
def test_under1():
    return "dddd"


print test_under()
print test_under.__name__
print test_under1.__name__