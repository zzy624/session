#!/usr/bin/env python
# -*-coding:utf-8-*-

import threading
from Queue import Queue
from time import sleep,ctime

loops = [9,9]

class MyThread(threading.Thread):

    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        print 'start {0} {1}'.format(self.name,self.args[0])
        self.func(*self.args)


def loop(nloop,nsec,q):
    print 'start loop {0} at: {1}'.format(nloop,ctime())
    sleep(nsec)
    print 'queue {0} put {1}'.format(nloop,nloop)
    q.put(nloop)
    print 'loop {0} done at: {1}'.format(nloop,ctime())
    q.task_done()

def main():
    print 'starting at:',ctime()
    therads = []
    q = Queue(32)
    nloops = range(len(loops))


    for i in nloops:
        t = MyThread(loop,(i,loops[i],q),loop.__name__)
        therads.append(t)

    for i in nloops:
        therads[i].start()

    for i in nloops:
        therads[i].join()

    # q.join()
    while 1:
        print 'get Queue {0}'.format(q.get(1))
        if q.empty():
            break

    print 'all DONE at:',ctime()

if __name__ == '__main__':
    main()