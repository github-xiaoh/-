# -*- coding:gb2312 -*-


# 导入上一级目录，方便调用case模块
import sys
sys.path.append(r"D:\python\系统的自动化测试脚本\Website\test_case\case")
from case import login,quit

import unittest  # 这里需要导入测试文件
import HTMLTestRunner
import time


def suite():

    suite = unittest.TestSuite()
    # 将测试用例加入到测试容器（套件）中
    suite.addTest(unittest.makeSuite(login.Auto_login))
    suite.addTest(unittest.makeSuite(quit.Auto_quit))

    # # 执行测试套件
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)

    return suite



