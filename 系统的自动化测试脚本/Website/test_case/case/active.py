# -*- coding:gb2312 -*-


from selenium.webdriver.common.action_chains import ActionChains    # ����ƶ�ģ��
import time
# ����Ŀ¼���������function_toolsģ��
import sys
sys.path.append(r"D:\python\ϵͳ���Զ������Խű�\Website\test_case\model")
from function_tools import r_excel_data


class Active():

    def login(self,driver):
        self.driver = driver
        self.user1 = 1
        self.name_pwd = (0,1)
        # ȡIDΪtxtLoginCode����ҳԪ��(�û�������Ԫ��)
        elem_user = self.driver.find_element_by_xpath('//*[@id="app"]/form/div[1]/div/div/input')
        # �������
        elem_user.clear()
        # �����û���
        elem_user.send_keys(r_excel_data(self.user1,self.name_pwd[0]))
        # ȡIDΪtxtPwd����ҳԪ��(��������Ԫ��)
        elem_pass = self.driver.find_element_by_xpath('/html/body/div/form/div[2]/div/div/input')
        # �������
        elem_pass.clear()
        # ��������
        elem_pass.send_keys(int(r_excel_data(self.user1,self.name_pwd[1])))
        # ȡIDΪbtnLogin�ĵ�¼��ť
        elem_login = self.driver.find_element_by_xpath('/html/body/div/form/div[3]/div/button')
        # �����¼��ť
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