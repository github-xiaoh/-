# -*- coding:gb2312 -*-

from selenium import webdriver
import time
import xlrd
import xlwt



def screenshot(driver):

    # ��ȡ��ǰʱ����ͼƬ��
    now_time = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    filename = r"D:\python\ϵͳ���Զ������Խű�\Website\test_report\png\\" + now_time + '.png'
    driver.get_screenshot_as_file(filename)


def r_excel_data(num_h,num_l):
    # ��ȡexcel�ĵ��е�����
    excel_file = r"D:\python\ϵͳ���Զ������Խű�\Website\test_data\test_data.xlsx"
    table_open = xlrd.open_workbook(excel_file)   # ��xlrdģ���excel�ļ�

    # ��ȡexcel��������
    # count = len(table_open.sheets())
    # print(u"��������Ϊ%s" % count)

    # ��ȡ�����ݵ��С�����
    table = table_open.sheet_by_name("user_name&user_pwd")
    h = table.nrows
    l = table.ncols
    # print(u"��������Ϊ%s,����Ϊ%s"%(h,j))
    for i in range(0,num_h+1):
        rowValues = table.row_values(i)
        excel_data = rowValues[num_l]

    return excel_data
    # aaa = 2
    # ccc = 1
    # bbb = r_excel_data(aaa,ccc)
    # print(bbb)





