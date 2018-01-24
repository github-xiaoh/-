# -*- coding:gb2312 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://fanyi.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    #有道搜索用例
    def test_youdao_search(self):
        u'''翻译加油'''
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("baidu_translate_input").send_keys(u"加油")
        # translate = driver.find_elements_by_id('translate-button')
        # translate.click()
        time.sleep(2)
        print("加油")
        # print(driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div[1]/p[2]/span").text)
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
        unittest.main()