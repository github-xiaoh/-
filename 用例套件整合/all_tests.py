# -*- coding:gb2312 -*-


#�� test_case Ŀ¼��ӵ� path �£������õ����·��
from test_case import login_quit,baidu_fanyi
import unittest  # ������Ҫ��������ļ�
import HTMLTestRunner
import time



testunit = unittest.TestSuite()
# �������������뵽�����������׼�����
testunit.addTest(unittest.makeSuite(baidu_fanyi.Baidu))
testunit.addTest(unittest.makeSuite(login_quit.Automation))

# # ִ�в����׼�
# runner = unittest.TextTestRunner()
# runner.run(testunit)

now_time = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))

filename = "C:\\Users\\Сh\Desktop\\" + now_time + 'requort.html'
fp = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'�Զ������ϱ���',description=u'����ִ�����')
runner.run(testunit)
