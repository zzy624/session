#coding: UTF-8  
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
import os
device=MonkeyRunner.waitForConnection()
device.startActivity(component="***") #component内容是要启动的类，包括包名和类名，如果对于一个apk不知道其启动类的话，可以先启动该app，然后用adb查看当前运行的最上层的类  
MonkeyRunner.sleep(5)
os.popen("adb shell uiautomator dump & adb pull /sdcard/window_dump.xml F:\\")   #下载当前布局，并回传到本机的F盘根目录，这个时候就可以查看布局坐标了  
device.touch(909,1620,u'DOWN_AND_UP')
MonkeyRunner.sleep(10)
result = device.takeSnapshot()
MonkeyRunner.sleep(2)
result.writeToFile('F:\\a.png','png')
print("Image success!!")
MonkeyRunner.sleep(20)  

