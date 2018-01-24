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
        u'''登陆实例'''
        active = Active()
        self.driver.get(self.base_url + "/")
        active.login(self.driver)
        print ('登陆成功')


    def test_quit(self):
        u'''登出实例'''
        active = Active()
        self.driver.get(self.base_url + "/")
        active.login(self.driver)
        active.quite()
        print('登出成功')


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
