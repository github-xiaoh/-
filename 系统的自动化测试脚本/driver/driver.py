# -*- coding:gb2312 -*-

from selenium import webdriver
import unittest

class Driver_Firefox():

    def driver_Firefox(self):

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://mamadmintest.52yingzheng.com/#/login"
        self.verificationErrors = []
        self.accept_next_alert = True

