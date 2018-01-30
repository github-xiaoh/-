# -*- coding:gb2312 -*-


from selenium.webdriver.common.action_chains import ActionChains    # 鼠标移动模块
import time
# 导入目录，方便调用function_tools模块
import sys
sys.path.append(r"D:\python\系统的自动化测试脚本\Website\test_case\model")
from function_tools import r_excel_data


class Active():

    def login(self,driver):
        self.driver = driver
        self.user1 = 1
        self.name_pwd = (0,1)
        # 取ID为txtLoginCode的网页元素(用户名输入元素)
        elem_user = self.driver.find_element_by_xpath('//*[@id="app"]/form/div[1]/div/div/input')
        # 清空输入
        elem_user.clear()
        # 键入用户名
        elem_user.send_keys(r_excel_data(self.user1,self.name_pwd[0]))
        # 取ID为txtPwd的网页元素(密码输入元素)
        elem_pass = self.driver.find_element_by_xpath('/html/body/div/form/div[2]/div/div/input')
        # 清空输入
        elem_pass.clear()
        # 键入密码
        elem_pass.send_keys(int(r_excel_data(self.user1,self.name_pwd[1])))
        # 取ID为btnLogin的登录按钮
        elem_login = self.driver.find_element_by_xpath('/html/body/div/form/div[3]/div/button')
        # 点击登录按钮
        elem_login.click()
        time.sleep(2)


    def quite(self):

        above = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[3]/div/span")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(above).perform()
        time.sleep(2)
        elem_quit = self.driver.find_element_by_xpath("/html/body/ul/li[2]")
        elem_quit.click()
        time.sleep(1)
        quit_button = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/button[2]")
        quit_button.click()