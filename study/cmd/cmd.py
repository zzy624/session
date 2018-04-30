# -*-coding:utf-8-*-

import os
import commands
import subprocess


def System():
    print 'This is System'
    result = os.system('ls')
    print result

def Popen():
    print 'This is popen'
    result = os.popen('ls')
    # print dir(result)
    f = result.readlines()
    print f
    result.close()

def Commands():
    print 'This is Commands'
    status,result =commands.getstatusoutput('ls')
    print 'status: {0}'.format(status)
    print 'result: {0}'.format(result)

def Subprocess():
    print 'This is Subprocess popen'
    # with open('./log.txt','w') as f:
    result = subprocess.Popen('python',shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    # print result.stdout.readlines()
    result.stdin.write('print 1')
    result.stdin.close()
    print result.stdout.readlines()
    result.stdout.close()
    print 'This is Subprocess call'
    result2 = subprocess.call('ls',shell=True)
    # print result2
    # print 'This is Subprocess '
    # result3 = subprocess.

def GetRedis():

    redis = subprocess.Popen('ls',shell=True,stdout=subprocess.PIPE)
    # value = subprocess.Popen('print 1',shell=True,stdin=redis.stdout,stdout=subprocess.PIPE)
    # redis.stdin.write('print 1')
    print redis.communicate()

if __name__ == '__main__':
    # System()
    # Popen()
    # Commands()
    # Subprocess()
    GetRedis()