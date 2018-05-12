# __author__ = 'vistest'
# -*-coding:utf-8-*-
import os
import time
import subprocess

# 连接手机
def connect_phone():
	subprocess.call('adb connect 127.0.0.1:62001')
	subprocess.call('adb devices')

#启动应用
def start_app(activity):
	subprocess.call('adb shell am start -n ' + activity)
	time.sleep(10)
	subprocess.call('adb shell screencap /sdcard/home_screen.png')
	subprocess.call('adb pull /sdcard/home_screen.png ./home_screen.png')

#返回首页
def back_home(key):
	subprocess.call('adb shell input keyevent ' + key)

#获取输入法
def get_input():
	r = subprocess.Popen('adb shell settings get secure default_input_method',stdout=subprocess.PIPE)
	print(u'当前默认输入法为：{0}'.format(r.stdout.read()))

# 安装应用
def install_apk(apk):
	subprocess.call('adb install -r ' + apk)

# 卸载应用
def uninstall_apk(apk):
	subprocess.call('adb uninstall ' + apk)


if __name__ == '__main__':
	apk = r'C:\Users\Administrator\Desktop\autosession\apk\com.cubic.autohome_9.0.5_905.apk'
	activity = 'com.cubic.autohome/.LogoActivity'
	key = 'KEYCODE_HOME'
	apkname = 'com.cubic.autohome'

	install_apk(apk)
	start_app(activity)
	back_home(key)
	get_input()
	uninstall_apk(apkname)

