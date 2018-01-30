# -*- coding:gb2312 -*-

from selenium import webdriver
import time
import xlrd
import xlwt



def screenshot(driver):

    # 提取当前时间做图片名
    now_time = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    filename = r"D:\python\系统的自动化测试脚本\Website\test_report\png\\" + now_time + '.png'
    driver.get_screenshot_as_file(filename)


def r_excel_data(num_h,num_l):
    # 读取excel文档中的数据
    excel_file = r"D:\python\系统的自动化测试脚本\Website\test_data\test_data.xlsx"
    table_open = xlrd.open_workbook(excel_file)   # 用xlrd模块打开excel文件

    # 获取excel工作簿数
    # count = len(table_open.sheets())
    # print(u"工作簿数为%s" % count)

    # 获取表数据的行、列数
    table = table_open.sheet_by_name("user_name&user_pwd")
    h = table.nrows
    l = table.ncols
    # print(u"表格的行数为%s,列数为%s"%(h,j))
    for i in range(0,num_h+1):
        rowValues = table.row_values(i)
        excel_data = rowValues[num_l]

    return excel_data
    # aaa = 2
    # ccc = 1
    # bbb = r_excel_data(aaa,ccc)
    # print(bbb)





