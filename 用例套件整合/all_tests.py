# -*- coding:gb2312 -*-


#把 test_case 目录添加到 path 下，这里用的相对路径
from test_case import login_quit,baidu_fanyi
import unittest  # 这里需要导入测试文件
import HTMLTestRunner
import time



testunit = unittest.TestSuite()
# 将测试用例加入到测试容器（套件）中
testunit.addTest(unittest.makeSuite(baidu_fanyi.Baidu))
testunit.addTest(unittest.makeSuite(login_quit.Automation))

# # 执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(testunit)

now_time = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))

filename = "C:\\Users\\小h\Desktop\\" + now_time + 'requort.html'
fp = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化整合报告',description=u'用例执行情况')
runner.run(testunit)
