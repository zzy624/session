#!/usr/bin/env python
# -*-coding:utf-8-*-

import threading
from time import sleep,ctime

loops = [4,2]

class ThreadFunc(object):

    def __init__(self,func,args,name=''):
        self.func = func
        self.args = args
        self.name = name

    def __call__(self):
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
        t = threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__))
        therads.append(t)

    for i in nloops:
        therads[i].start()

    for i in nloops:
        therads[i].join()

    print 'all DONE at:',ctime()

if __name__ == '__main__':
    main()