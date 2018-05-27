# -*- coding:utf-8 -*-
import unittest

from appium import webdriver
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def login():
	desired_caps = {'platformName': 'Android',
	                'platformVersion': '7.0',
	                'deviceName': '192.168.31.171:5555',
	                'appPackage': 'com.cubic.autohome',
	                'appActivity': '.LogoActivity',
	                'unicodeKeyboard': True,
	                'resetKeyboard':True,
	                'noReset':False,
	                }

	driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	driver.implicitly_wait(30)

	driver.find_element_by_id('com.autohome.plugin.usergrowth:id/iv_signin_close').click()
	driver.find_element_by_id('com.cubic.autohome:id/owner_main_RadioButton').click()
	driver.find_element_by_id('com.autohome.main.me:id/owner_guest_login').click()
	driver.find_element_by_id('com.autohome.main.me:id/change_old_owner_login').click()
	driver.find_element_by_id('com.autohome.main.me:id/owner_login_input_usr').send_keys('18611740012')
	driver.find_element_by_id('com.autohome.main.me:id/owner_login_pwd_container').send_keys('zzy18611740012')
	driver.find_element_by_id('com.autohome.main.me:id/owner_login_commit').click()
	time.sleep(5)
	driver.quit()

if __name__ == '__main__':
	login()
