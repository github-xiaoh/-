# -*- coding:gb2312 -*-

from selenium import webdriver
import time

def screenshot(driver):

    # 提取当前时间做图片名
    now_time = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    filename = r"D:\python\系统的自动化测试脚本\Website\test_report\png\\" + now_time + '.png'
    driver.get_screenshot_as_file(filename)

