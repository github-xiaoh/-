# -*- coding:gb2312 -*-

import unittest  # ������Ҫ��������ļ�
import HTMLTestRunner
import time


# ����Ŀ¼���������caseģ��
import sys
sys.path.append(r"D:\python\ϵͳ���Զ������Խű�\Website\test_case")
from test_case import all_tests


now_time = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
filename = "D:\\python\\ϵͳ���Զ������Խű�\\Website\\test_report\\report\\" + now_time + 'requort.html'
fp = open(filename, 'wb')


runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'�Զ������ϱ���', description=u'����ִ�����')
runner.run(all_tests.suite())



