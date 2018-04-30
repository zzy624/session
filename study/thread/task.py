# -*-coding:utf-8-*-
import threading
from time import sleep,ctime

class MyThread(threading.Thread):

    def __init__(self,time):
        threading.Thread.__init__(self)
        self.time = time

    def run(self):
        print 'start MyThread ~ at: {0}'.format(ctime())
        print 'start time is {0} s'.format(self.time)
        sleep(self.time)
        print 'over MyThread ~ at: {0}'.format(ctime())

def main(time):
    print 'start main() at: {0}'.format(ctime())
    t = MyThread(time)
    t.start()
    # t.join()
    print 'go on main() at :{0}\n'.format(ctime())
    sleep(10)
    print 'main() is over at :{0}'.format(ctime())

if __name__ == '__main__':
    main(20)