# -*- coding:gb2312 -*-

import unittest  # 这里需要导入测试文件
import HTMLTestRunner
import time


# 导入目录，方便调用case模块
import sys
sys.path.append(r"D:\python\系统的自动化测试脚本\Website\test_case")
from test_case import all_tests


now_time = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
filename = "D:\\python\\系统的自动化测试脚本\\Website\\test_report\\report\\" + now_time + 'requort.html'
fp = open(filename, 'wb')


runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化整合报告', description=u'用例执行情况')
runner.run(all_tests.suite())



