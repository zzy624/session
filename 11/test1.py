# -*-coding:utf-8-*-

import os
import commands
import subprocess

# r1 = os.popen("adb devices")
#
# r2 = os.system("adb devices")

# print "结果:{0}".format(r2)
# print "结果:{0}".format(r1.read())

res =  subprocess.Popen(('dir','D:'), shell=False,stdout=subprocess.PIPE)
print res.communicate()

# with open("./test.txt",'w+') as f:
# res2 = subprocess.Popen("adb devices",stdout=subprocess.PIPE)
# print res2.wait()
# print res2.


# (status, output) = commands.getstatusoutput('adb devices')
# # for i in ss:
# # 	print(i)
# print(output)