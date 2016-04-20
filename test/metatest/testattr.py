class Test(object):
    def __init__(self):
        self._properties = {}

    def __getattr__(self, item):
        try:
            return super(Test, self).__getattr__(item)
        except AttributeError:
            return self._properties[item]

    def __setattr__(self, key, value):
        # try:
        #     super(Test, self).__setattr__(key, value)
        # except AttributeError:
        self._properties[key] = value


t = Test()
t.pro = '111'

print t.pro
