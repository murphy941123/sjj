# -*- coding: utf-8 -*-
import unittest
from common.myunit import StartEnd
from page.home_page import HomePage

class Test_Buy(StartEnd):

    def test_1search_lesson(self):
        H = HomePage(self.driver)
        H.search_lesson()
        self.assertTrue(H.check_search_lesson())

    def test_2living_play(self):
        H = HomePage(self.driver)
        H.living_lesson()
        self.assertTrue(H.check_living_lesson())

    def test_3Audio_play(self):
        H = HomePage(self.driver)
        H.Audio_play()
        self.assertTrue(H.check_Audio_play())


if __name__ == '__main__':
    unittest.main(verbosity=2)