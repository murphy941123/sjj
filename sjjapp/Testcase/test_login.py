# -*- coding: utf-8 -*-
import os,sys
import unittest
from base.base_action import BaseAction
from common.common_fun import Common
from common.myunit import StartEnd
from page.me_page import MePage
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# s = ReadExcel()
# s.GetExcel('../data/Login_sjj.xlsx')
class TestSjj(StartEnd):
    csv_file= '../data/login.csv'
    c = Common(BaseAction)
    #账号密码正确，登录成功
    # def test_login_success(self):
    #     l = MePage(self.driver)
    #     data=self.c.get_csv_data(self.csv_file,2)
    #     l.login_by_pwd(data[0],data[1])
    #     self.assertTrue(l.check_login_status())
    #
    # # 密码错误，登录失败
    # def test_login_failed1(self):
    #     l = MePage(self.driver)
    #     data = self.c.get_csv_data(self.csv_file,3)
    #     l.login_by_pwd(data[0],data[1])
    #     self.assertTrue(l.get_login_failed())
    #
    # #账号错误，登录失败
    # def test_login_failed2(self):
    #     l = MePage(self.driver)
    #     data = self.c.get_csv_data(self.csv_file,4)
    #     l.login_by_pwd(data[0],data[1])
    #     self.assertTrue(l.get_login_failed())

    # 手机验证码登录
    def test_login_sms_code(self):
        l = MePage(self.driver)
        data = self.c.get_csv_data(self.csv_file, 4)
        l.login_by_smscode(data[0])
        self.assertTrue(l.check_login_status())

if __name__ == '__main__':
    unittest.main(verbosity=2)


