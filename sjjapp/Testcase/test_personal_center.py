# -*- coding: utf-8 -*-
import unittest
from common.myunit import StartEnd
from page.home_page import MePage
class Test_Personal_Center(StartEnd):

    def test_1message_center(self):
        M=MePage(self.driver)
        M.message_center()
        self.assertTrue(M.check_message_center())

    def test_2nickname_edit(self):
        M = MePage(self.driver)
        M.nickname_editor()
        self.assertTrue(M.check_nickname_editor())

    def test_3real_name(self):
        M = MePage(self.driver)
        M.input_real_name()
        self.assertTrue(M.check_input_real_name())

    def test_4choose_sex(self):
        M = MePage(self.driver)
        M.choose_sex()
        self.assertTrue(M.check_choose_sex())
        M.click_back()

    def test_5my_account(self):
        M = MePage(self.driver)
        M.my_account()


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # suite = unittest.TestSuite()
    # suite.addTest(Test_Personal_Center("test_1message_center"))
    # suite.addTest(Test_Personal_Center("test_3real_name"))
    # suite.addTest(Test_Personal_Center("test_2nickname_edit"))
    # suite.addTest(Test_Personal_Center("test_4choose_sex"))
    # suite.addTest(Test_Personal_Center("test_5my_account"))
