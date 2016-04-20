class VNXObject(object):
    def __init__(self):
        self._props = {}

    def __setattr__(self, key, value):
        try:
            super(VNXObject, self).__setattr__(key, value)
        except AttributeError:
            self._props[key] = value

    # def __getattr__(self, item):
    #     try:
    #         super(VNXObject, self).__getattribute__(item)
    #     except AttributeError:
    #         # v = self.__props[item]
    #         # print "__get__: ", v
    #         # if callable(v):
    #         #     return v()
    #         # return v
    #         raise


class VNXObject1(object):
    props = {}

    def __setattr__(self, key, value):
        self.props[key] = value

    def __getattr__(self, item):
        try:
            super(VNXObject1, self).__getattr__(item)
        except AttributeError:
            v = self.props[item]
            print "__get__: ", v
            if callable(v):
                return v()
            return v
import mock
#
# obj =VNXObject()
#
# obj.test= '111'
# print obj.test
#
# setattr(obj, 'hello', "hello, peter")
# print obj.hello
#
# setattr(obj, 'mock', mock.PropertyMock(return_value='hello,mock'))
# print obj.mock

vnx1 = VNXObject1()
vnx1.test= 'hello'
print vnx1.test