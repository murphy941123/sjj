# -*- coding: utf-8 -*-
import time
import unittest
from common.myunit import StartEnd
from page.home_page import MePage, HomePage


class Test_Memorizing_word(StartEnd):

    #正序功能
    def test_1learning_mode1(self):
        H=HomePage(self.driver)
        H.learning_mode1()
        self.assertTrue(H.check_learning_mode1())

    # 乱序功能
    def test_2learning_mode2(self):
        H = HomePage(self.driver)
        H.learning_mode2()
        self.assertTrue(H.check_learning_mode2())

    #每日20个单词
    def test_3twenty_word(self):
        H = HomePage(self.driver)
        H.twenty_words()
        self.assertTrue(H.check_twenty_words())

    #每日30个单词
    def test_4thirty_words(self):
        H = HomePage(self.driver)
        H.thirty_words()
        self.assertTrue(H.check_thirty_words())

    #每日10个单词
    def test_5ten_words(self):
        H = HomePage(self.driver)
        H.ten_words()
        self.assertTrue(H.check_ten_words())




if __name__ == '__main__':
    unittest.main(verbosity=2)