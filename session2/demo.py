# -*- coding:utf-8 -*-
from appium import webdriver
import time

def demo():
	desired_caps = {'platformName': 'Android',
	                'platformVersion': '7.0',
	                'deviceName': 'UEUDU16C21008041',
	                'appPackage': 'com.cubic.autohome',
	                'appActivity': '.LogoActivity',
	                'unicodeKeyboard': True,
	                'resetKeyboard':True,
	                }

	driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	# driver.swipe(100,100,100,400)
	driver.implicitly_wait(10)
	time.sleep(4)
	driver.find_element_by_id('com.cubic.autohome:id/owner_main_RadioButton').click()
	driver.find_element_by_id('com.autohome.main.me:id/owner_guest_login').click()
	driver.find_element_by_id('com.autohome.main.me:id/change_old_owner_login').click()
	driver.find_element_by_id('com.autohome.main.me:id/owner_login_input_usr').send_keys('18611740012')
	driver.find_element_by_id('com.autohome.main.me:id/owner_login_pwd_container').send_keys('zzy18611740012')
	driver.find_element_by_id('com.autohome.main.me:id/owner_login_commit').click()
	time.sleep(2)
	driver.find_element_by_id('com.cubic.autohome:id/article_main_RadioButton').click()
	driver.find_element_by_id('com.autohome.main.article:id/search_box').click()
	driver.find_element_by_id('com.autohome.plugin.search:id/fragment_search_keyword_autocompleteview').send_keys('本田'.decode('utf8'))
	driver.find_elements_by_id('com.autohome.plugin.search:id/searchcontent')[0].click()
	driver.save_screenshot('bentian.jpg')
	time.sleep(2)
	driver.quit()

if __name__ == '__main__':
	demo()
