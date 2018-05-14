# -*- coding:utf-8 -*-
import unittest

from appium import webdriver
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def loginout():
	desired_caps = {'platformName': 'Android',
	                'platformVersion': '7.0',
	                'deviceName': '127.0.0.1:62001',
	                'appPackage': 'com.cubic.autohome',
	                'appActivity': '.LogoActivity',
	                'unicodeKeyboard': True,
	                'resetKeyboard':True,
	                'noReset':True,
	                }

	driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	driver.implicitly_wait(30)

	driver.find_element_by_id('com.cubic.autohome:id/owner_main_RadioButton').click()
	driver.find_element_by_id('com.autohome.main.me:id/owner_user_content_setting').click()

	# 获取设备分辨率
	window_size = driver.get_window_size()
	width = window_size.get("width")
	height = window_size.get("height")
	# 滑动屏幕
	driver.swipe(width / 2, height-1, width / 2,1, 200)

	driver.find_element_by_id('com.autohome.plugin.setting:id/owner_userinfo_logout').click()
	driver.find_element_by_id('com.cubic.autohome:id/rightBtn').click()
	time.sleep(2)
	driver.quit()

if __name__ == '__main__':
	loginout()
