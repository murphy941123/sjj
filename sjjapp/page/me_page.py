# -*- coding: utf-8 -*-
import os,sys
import logging
import time
import pymysql
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from common.common_fun import Common
from common.desired_caps1 import appium_desired
from common.multi_appium import appium_start

sys.path.append(os.getcwd())

class MePage(Common):

    c = Common(BaseAction)
    csv_file = '../data/login.csv'
    welcome_login_loc = By.XPATH,"//*[@text='欢迎登录']"
    pw_login_loc = By.XPATH,"//*[@text='密码登录>>']"
    input_phone_number_loc = By.XPATH,"//*[@text='请输入手机号码']"
    input_pw_loc = By.XPATH,"//*[@text='请输入登录密码']"
    login_loc = By.XPATH, "//*[@text='登录']"
    get_smscode_loc = By.XPATH,"//*[@text='获取验证码']"
    toast_message = "账号不存在或者密码错误！"
    setting_loc = By.XPATH, "//android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.ImageView[2]"
    logout_loc = By.XPATH, "//*[@text='退出登录']"
    message_center_loc = By.XPATH, "//android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]"
    advertising_loc = By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]"
    my_account_loc = By.XPATH, "//*[@text='我的账户']"
    account_recharge_loc = By.XPATH, "//*[@text='账户充值']"
    change_password_loc=By.XPATH,"//*[@text='修改密码']"
    old_password_loc=By.XPATH, "//*[@text='旧密码']"
    confirm_password_loc=By.XPATH,"//*[@text='确认密码']"
    new_password_loc=By.XPATH,"//*[@text='新密码，长度6-18位']"
    save_loc = By.XPATH, "//*[@text='保存']"
    clear_ache_loc=By.XPATH,"//*[@text='清除缓存']"
    clear_loc=By.XPATH,"//*[@text='清除']"
    check_update_loc=By.XPATH,"//*[@text='检查更新']"
    play_switch_loc=By.XPATH,"//*[@text='播放器切换']"
    exoplayer_loc=By.XPATH,"//*[@text='exoplayer']"
    ijkplayer_loc=By.XPATH,"//*[@text='ijkplayer']"
    chancel_loc=By.XPATH,"//*[@text='取消']"
    play_loc = By.XPATH, "//*[@text='ijkplayer']"
    user_agreement_loc=By.XPATH, "//*[@text='用户协议']"
    privacy_policy_loc=By.XPATH, "//*[@text='隐私政策']"
    nickname_loc=By.XPATH,"//*[@text='昵称']"
    nickname_editor_loc=By.CLASS_NAME,"android.widget.EditText"
    edit_data_loc=By.XPATH,"//*[@text='编辑资料']"
    name_loc=By.XPATH,"//*[@text='姓名']"
    sex_loc=By.XPATH,"//*[@text='性别']"
    choose_man_loc=By.XPATH,"//*[@text='男']"
    choose_woman_loc=By.XPATH,"//*[@text='女']"
    user_info=By.XPATH,"//*[@text='13281965965']"

    change_failed_toast='密码修改失败，原密码错误，如忘记，请找回'
    clear_ache_toast='清理完成'


    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    #密码登录
    def login_by_pwd(self,phone_number,pwd):
        self.click_me()
        self.click_chancel()
        self.click(self.welcome_login_loc)
        logging.info('===login===')
        self.click(self.pw_login_loc)
        logging.info('input_phone_number')
        self.input_text(self.input_phone_number_loc, phone_number)
        logging.info('===click_pw_login===')
        self.input_text(self.input_pw_loc,pwd)
        logging.info('===click_login===')
        self.click(self.login_loc)
        self.assert_existed(self.user_info,13281965965)
        self.click_chancel()

    #验证码登录
    def login_by_smscode(self,phone_number):
        self.click(self.welcome_login_loc)
        self.input_text(self.input_phone_number_loc, phone_number)
        self.click(self.get_smscode_loc)
        time.sleep(2)
        self.input_smscode()
        self.get_screenshot('../screenshot/获取验证码.png')
        logging.info('login success.png by smscode')
        self.click_chancel()

    # 修改密码成功
    def change_password_success(self):
        data = self.c.get_csv_data(self.csv_file, 1)
        self.login_by_pwd(data[0],data[1])
        logging.info('登录成功')
        self.click_setting()
        self.click(self.change_password_loc)
        self.input_text(self.old_password_loc,'123456')
        self.input_text(self.new_password_loc,'123456')
        self.input_text(self.confirm_password_loc,'123456')
        self.click(self.save_loc)

    def check_change_password(self):
        try:
            modify_success=self.find_toast(self.modify_success_toast).text
            print(modify_success)
        except NoSuchElementException:
            print('没有找到修改成功提示')
        else:
            if modify_success=='修改成功':
                logging.info('密码修改成功')
                self.get_screenshot("../screenshot/setting/密码修改成功.png")
                return True
            else:
                print(modify_success!='修改成功')
                return False


    #清理缓存
    def clear_ache(self):
        self.click(self.clear_ache_loc)
        self.click(self.clear_loc)
    def check_clear_ache(self):   #缓存清理完成
        try:
            clear_success_info=self.find_toast('清理完成').text
        except NoSuchElementException:
            print('没有找到清理完成提示')
        else:
            if clear_success_info=='清理完成':
                self.get_screenshot("../screenshot/setting/清理完成.png")
                return True
            else:
                print(clear_success_info!='清理完成')
                return False

    #检查更新
    def check_update(self):
        self.click(self.check_update_loc)
    def check_check_update(self):  # 缓存清理完成
        try:
            clear_success_info = self.find_toast('当前已经是最新版本').text
        except NoSuchElementException:
            print('没有找到当前已经是最新版本提示')
        else:
            if clear_success_info == '当前已经是最新版本':
                self.get_screenshot("../screenshot/setting/最新版本.png")
                return True
            else:
                logging.info(clear_success_info != '当前已经是最新版本')
                return False

    #播放器切换
    def play_switch(self):
        self.click(self.play_switch_loc)
        self.click(self.ijkplayer_loc)
        self.click(self.play_switch_loc)
        self.click(self.chancel_loc)
        self.click(self.play_switch_loc)
        self.click(self.exoplayer_loc)
    def check_play_switch(self):
        try:
            player=self.find_element(self.exoplayer_loc).text
        except NoSuchElementException:
            print('没有找到exoplayer')
        else:
            if player == 'exoplayer':
                time.sleep(1)
                self.get_screenshot("../screenshot/setting/exoplayer.png")
                return True
            else:
                print(player == 'exoplayer')
                return False
    #用户协议
    def user_agreement(self):
        self.click(self.user_agreement_loc)

    def check_user_agreement(self):
        try:
            title = self.find_element(self.user_agreement_loc).text
        except NoSuchElementException:
            print('没有找到用户协议')
        else:
            if title == '用户协议':
                self.get_screenshot("../screenshot/setting/用户协议.png")
                return True
            else:
                print(title != '用户协议')
                return False

    #隐私政策
    def privacy_policy(self):
        self.click(self.privacy_policy_loc)
    def check_privacy_policy(self):
        try:
            title = self.find_element(self.privacy_policy_loc).text
        except NoSuchElementException:
            print('没有找到隐私政策')
            return False
        else:
            if title == '隐私政策':
                self.get_screenshot("../screenshot/setting/隐私政策.png")
                return True
            else:
                print(title != '隐私政策')
                return False

    # 消息中心
    def message_center(self):
        self.click(self.message_center_loc)
        self.click(self.advertising_loc)

    def check_message_center(self):
        try:
            self.find_element(self.close_loc)
        except NoSuchElementException:
            print('没有找到关闭按钮')
            return False
        else:
            time.sleep(1)
            self.get_screenshot("../screenshot/消息内容.png")
            self.click(self.close_loc)
            self.click(self.back_button)
            return  True

    #修改昵称
    def nickname_editor(self):
        self.click(self.edit_data_loc)
        self.click(self.nickname_loc)
        self.clear(self.nickname_editor_loc)
        self.input_text(self.nickname_editor_loc,'测试')
        self.click(self.save_loc)

    def check_nickname_editor(self):
        try:
            modify_success=self.find_toast(self.modify_success_toast).text
        except NoSuchElementException:
            print('没有找到昵称')
            return False
        else:
            if  modify_success=='修改成功':
                self.get_screenshot("../screenshot/昵称修改成功.png")
                return True
            else:
                print(modify_success!='修改成功')
                return False

    def input_real_name(self):
        self.click(self.name_loc)
        self.clear(self.nickname_editor_loc)
        self.input_text(self.nickname_editor_loc,'张三')
        self.click(self.save_loc)

    def check_input_real_name(self):
        try:
            save_success=self.find_toast(self.modify_success_toast).text
        except NoSuchElementException:
            print('没有修改成功')
            return False
        else:
            if save_success=='修改成功':
                self.get_screenshot('../screenshot/姓名修改成功.png')
                return True
            else:
                print(save_success!='修改成功')
                return False

    def choose_sex(self):
        self.click(self.sex_loc)
        self.click(self.chancel_loc)
        self.click(self.sex_loc)
        self.click(self.choose_man_loc)
        self.click(self.sex_loc)
        self.click(self.choose_woman_loc)

    def check_choose_sex(self):
        try:
            modify_success=self.find_toast(self.modify_success_toast).text
        except NoSuchElementException:
            print('没有修改成功')
            return False
        else:
            if modify_success=='修改成功':
                self.get_screenshot('../screenshot/性别修改成功.png')
                return True
            else:
                print(modify_success!='修改成功')
                return False

    def my_account(self):
        self.click(self.my_account_loc)
        time.sleep(2)
        self.get_screenshot("../screenshot/账户消费.png")
        self.click(self.account_recharge_loc)
        time.sleep(2)
        self.get_screenshot("../screenshot/账户充值.png")





    def check_login_status(self):
        try:
            self.find_element(self.userinfo)
        except NoSuchElementException:
            logging.error('login failed')
            self.get_screenshot('login failed.png')
        else:
            logging.info('login success.jpg')
            self.get_screenshot('login success.png')
            return True

    def check_change_password1(self):   #原密码错误
        try:
            change_success_info=self.find_toast(self.change_failed_toast).text
        except NoSuchElementException:
            print('没有找到修改失败提示')
        else:
            if change_success_info=='密码修改失败，原密码错误，如忘记，请找回':
                self.get_screenshot("../screenshot/原密码错误.jpg")
            else:
                print('提示错误')

    def get_login_failed(self):
        try:
             self.find_toast(self.toast_message).text
        except NoSuchElementException:
            print('NO toast_message')
        else:
            logging.info('login failed.jpg')
            self.get_screenshot('login failed.jpg')
            return True



    #获取并输入验证码（测试环境下）
    def input_smscode(self):
        conn = pymysql.connect(host='rm-m5e3kq2fg7k4jy343qo.mysql.rds.aliyuncs.com', user='chenli',
                               password='Cqtouch2014', database='booklnbak')
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(self.sql)
        result = cur.fetchall()
        #获取到验证码
        sms_code = result[0]['content']
        #循环
        i = -1
        while i < 4:
            i = i + 1
            r = int(sms_code[i]) + 7
            print(r)
            self.driver.press_keycode(r)

if __name__ == '__main__':
    driver=appium_desired()
    M=MePage(driver)
    M.change_password_success()
    # M.check_change_password()
    # M.change_password_failed()
    # M.clear_ache()
    # M.check_update()
    # M.play_switch()
    # M.message_center()
    # M.nickname_editor()

