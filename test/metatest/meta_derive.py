import abc
import six


@six.add_metaclass(abc.ABCMeta)
class ClassBase(object):
    @abc.abstractmethod
    def fun_a(self):
        """This function must be implemented by subclass"""
        pass

    def fun_b(self):
        pass

    def fun_d(self):
        pass


class ClassDerive(ClassBase):

    def fun_c(self):
        print "Fun c"


@six.add_metaclass(abc.ABCMeta)
class ClassBase2(object):
    def fun_e(self):
        print "fun_e"


print issubclass(ClassBase2, ClassBase)
d = ClassDerive()


d.fun_c()