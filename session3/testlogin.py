# -*- coding:utf-8 -*-
import unittest

from appium import webdriver
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Test1(unittest.TestCase):

	def setUp(self):
		desired_caps = {'platformName': 'Android',
		                'platformVersion': '7.0',
		                'deviceName': '127.0.0.1:62001',
		                'appPackage': 'com.cubic.autohome',
		                'appActivity': '.LogoActivity',
		                'unicodeKeyboard': True,
		                'resetKeyboard': True,
		                'noReset': False,
		                }
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(30)

	def tearDown(self):
		time.sleep(5)
		self.driver.quit()

	def testlogin(self):
		self.driver.find_element_by_id('com.autohome.plugin.usergrowth:id/iv_signin_close').click()
		self.driver.find_element_by_id('com.cubic.autohome:id/owner_main_RadioButton').click()
		self.driver.find_element_by_id('com.autohome.main.me:id/owner_guest_login').click()
		self.driver.find_element_by_id('com.autohome.main.me:id/change_old_owner_login').click()
		self.driver.find_element_by_id('com.autohome.main.me:id/owner_login_input_usr').send_keys('18611740012')
		self.driver.find_element_by_id('com.autohome.main.me:id/owner_login_pwd_container').send_keys('zzy18611740012')
		self.driver.find_element_by_id('com.autohome.main.me:id/owner_login_commit').click()

if __name__ == '__main__':
	unittest.main()
