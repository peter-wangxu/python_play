__author__ = 'wangp11'


class PeterWang(object):
    def test1(self,args):
        print "test1--" + args

    def test2(self):
        print "<-----Test 2 start------>"
        print "test2--" + self.outter
        print "<-----Test 2 end------>"

    def test3(self):
        print "<-----Test 3 start------>"
        print self.outter
        self.outter = "test3"
        print self.outter
        print "<-----Test 3 end------>"

    func_ref = test1
    @classmethod
    def class_method(cls):
        cls.outter = "class value"
        print cls.outter

    @staticmethod
    def static_method(args="static"):
        print args
c = PeterWang()
c.test1('ddddd')
PeterWang.class_method()
#PeterWang.static_method('hello')
#c.class_method()
PeterWang.test1(c,'dadfa') #instance method could not be invoked by Class
PeterWang.func_ref(c,'fucn_ref')
print "direct:" + c.outter


c.test3()
c.test2()