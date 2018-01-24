# -*- coding:gb2312

from selenium import webdriver
from active import Active

import unittest
import time

import HTMLTestRunner

class Automation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://mamadmintest.52yingzheng.com/#/login"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_automation(self):
        u'''��½ʵ��'''
        active = Active()
        self.driver.get(self.base_url + "/")
        active.login(self.driver)
        print ('��½�ɹ�')


    def test_quit(self):
        u'''�ǳ�ʵ��'''
        active = Active()
        self.driver.get(self.base_url + "/")
        active.login(self.driver)
        active.quite()
        print('�ǳ��ɹ�')


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(Automation('test_automation')))
        suite.addTest(unittest.makeSuite(Automation('test_quit')))
        return suite


if __name__=="__main__":
    unittest.main()
