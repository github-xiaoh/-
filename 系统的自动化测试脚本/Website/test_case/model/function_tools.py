# -*- coding:gb2312 -*-

from selenium import webdriver
import time

def screenshot(driver):

    # ��ȡ��ǰʱ����ͼƬ��
    now_time = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    filename = r"D:\python\ϵͳ���Զ������Խű�\Website\test_report\png\\" + now_time + '.png'
    driver.get_screenshot_as_file(filename)

