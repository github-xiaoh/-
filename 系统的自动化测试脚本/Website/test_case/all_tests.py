# -*- coding:gb2312 -*-


# ������һ��Ŀ¼���������caseģ��
import sys
sys.path.append(r"D:\python\ϵͳ���Զ������Խű�\Website\test_case\case")
from case import login,quit

import unittest  # ������Ҫ��������ļ�
import HTMLTestRunner
import time


def suite():

    suite = unittest.TestSuite()
    # �������������뵽�����������׼�����
    suite.addTest(unittest.makeSuite(login.Auto_login))
    suite.addTest(unittest.makeSuite(quit.Auto_quit))

    # # ִ�в����׼�
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)

    return suite



