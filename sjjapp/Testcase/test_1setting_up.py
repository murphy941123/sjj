# -*- coding: utf-8 -*-
import time
import unittest
from common.myunit import StartEnd
from page.home_page import MePage

class Test_Setting_up(StartEnd):

    #修改密码
    def test_change_password(self):
        M = MePage(self.driver)
        M.change_password_success()
        self.assertTrue(M.check_change_password())

    #清理缓存
    def test_clear_cache(self):
        M = MePage(self.driver)
        M.clear_ache()
        self.assertTrue(M.check_clear_ache())

    #检查更新
    def test_check_update(self):
        M = MePage(self.driver)
        M.check_update()
        self.assertTrue(M.check_check_update())

    #播放器切换
    def test_play_switch(self):
        M = MePage(self.driver)
        M.play_switch()
        time.sleep(2)
        self.assertTrue(M.check_play_switch())

    def test_user_agreement(self):
        M = MePage(self.driver)
        M.user_agreement()
        self.assertTrue(M.check_user_agreement())
        M.click_close()

    def test_privacy_policy(self):
        M = MePage(self.driver)
        M.privacy_policy()
        self.assertTrue(M.check_privacy_policy())
        M.click_close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
