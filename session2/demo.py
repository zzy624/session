# -*- coding:utf-8 -*-
from appium import webdriver
import time

def demo():
	desired_caps = {'platformName': 'Android',
	                'platformVersion': '4.4',
	                'deviceName': 'Android Emulator',
	                'appPackage': 'com.ibox.calculators',
	                'appActivity': '.CalculatorActivity',
	                }

	driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	# driver.swipe(100,100,100,400)
	driver.find_element_by_android_uiautomator('new UiSelector().text("6")').click()
	driver.find_element_by_android_uiautomator('new UiSelector().text("1")').click()
	driver.find_element_by_android_uiautomator('new UiSelector().text("2")').click()
	driver.find_element_by_id('com.ibox.calculators:id/plus').click()
	driver.find_element_by_android_uiautomator('new UiSelector().text("2")').click()
	driver.find_element_by_android_uiautomator('new UiSelector().text("4")').click()
	driver.find_element_by_id('com.ibox.calculators:id/equal').click()
	time.sleep(8)
	driver.quit()

if __name__ == '__main__':
	demo()
