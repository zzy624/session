#!/usr/bin/env python
# -*-coding:utf-8-*-

import threading
from time import sleep,ctime

loops = [4,2]

class MyThread(threading.Thread):

    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        print 'start {0} {1}'.format(self.name,self.args[0])
        self.func(*self.args)


def loop(nloop,nsec):
    print 'start loop {0} at: {1}'.format(nloop,ctime())
    sleep(nsec)
    print 'loop {0} done at: {1}'.format(nloop,ctime())

def main():
    print 'starting at:',ctime()
    therads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        therads.append(t)

    for i in nloops:
        therads[i].start()

    for i in nloops:
        therads[i].join()

    print 'all DONE at:',ctime()

if __name__ == '__main__':
    main()