# -*-coding:utf-8-*-

from random import randrange
# from threading import Thread, currentThread
# from time import sleep, ctime


loops = (randrange(x,x+1) for x in xrange(randrange(3,7)))



if __name__ == '__main__':
    for i in loops:
        print i