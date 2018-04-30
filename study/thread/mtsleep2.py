#!/usr/bin/env python
# -*-coding:utf-8-*-

import thread
from time import sleep,ctime

loops = [4,2]

def loop(nloop,nsec,lock):
    print 'start loop {0} at: {1}'.format(nloop,ctime())
    sleep(nsec)
    print 'loop {0} done at: {1}'.format(nloop,ctime())
    lock.release()

def main():
    print 'starting at:',ctime()
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        # print 'get lock {0}'.format(i)
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop,(i,loops[i],locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass

    print 'all DONE at:',ctime()

if __name__ == '__main__':
    main()