# -*- coding:gb2312 -*-

from selenium import webdriver
from active import Active

import unittest
import time

# 导入上一级目录，方便调用myunit模块
import sys
sys.path.append(r"D:\python\系统的自动化测试脚本\Website\test_case\model")
import function_tools



class Auto_quit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://mamadmintest.52yingzheng.com/#/login"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_quit(self):
        u'''登出实例'''
        active = Active()
        self.driver.get(self.base_url + "/")
        active.login(self.driver)
        active.quite()

        # 提取当前时间做图片名
        function_tools.screenshot(self.driver)

        print('登出成功')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)



if __name__=="__main__":
    unittest.main()
