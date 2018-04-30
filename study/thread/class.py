# -*-coding:utf-8-*-

class MyClass(object):

    def __init__(self,name,func):
        self.name = name
        self.func = func
        print 'This is MyClass __init__'

    def __call__(self, *args, **kwargs):
        print self.func(*self.name)

    @staticmethod
    def Hello():
        print "This is MyClass Hello staticmethod"

    @classmethod
    def Hi(cls):
        print 'This is MyClass Hi classmethod'

    def Ha(self):
        print 'This is MyClass Ha of {0}'.format(self.name)

    def run(self):
        print 'This is MyClass run'

    def start(self):
        self.run()

class Myclass(MyClass):

    def __init__(self,name = None,func = None):
        MyClass.__init__(self,name,func)

    def run(self):
        print 'This is Myclass run'

def Call(a):
    return 'This is Call {0}'.format(a)

if __name__ == '__main__':
    # t = MyClass('t',Call)
    # MyClass.Hello()
    # MyClass.Hi()
    # t.Ha()
    # t()
    s = Myclass()
    s.start()