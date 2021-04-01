# -*- coding: utf-8 -*-
import csv
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
#新建一个公共类，存放读取csv表、Excel表等方法。
class Common(BaseAction):

    permission_button = By.XPATH, "//*[@text='始终允许']"
    agree_button = By.XPATH, "//*[@text='同意']"
    me_button = By.XPATH, "//android.widget.LinearLayout/android.widget.FrameLayout[4]"
    userinfo=By.XPATH, "//*[@text=18100000000]"
    userinfo_sms_button = By.XPATH, "//*[@text=18100000000]"
    chancel_button=By.XPATH, "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView[1]"
    setting_button=By.XPATH,"//android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.ImageView[2]"
    logout_button=By.XPATH,"//*[@text='退出登录']"
    back_button=By.CLASS_NAME,"android.widget.ImageButton"
    video_back=By.CLASS_NAME,"android.widget.ImageView"
    close_loc = By.CLASS_NAME,"android.widget.ImageButton"
    modify_success_toast='修改成功'
    save_success_toast='保存成功'
    next_one_loc=By.XPATH, "//*[@resource-id='qr-body']/android.view.View[3]"
    def __init__(self,driver):
        BaseAction.__init__(self, driver)

    def get_csv_data(self, csv_file, line):
        with open(csv_file, 'r', encoding='utf-8-sig') as  file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    def click_permission(self):
        try:
            permission_button = self.find_element(self.permission_button)
        except NoSuchElementException:
            print('no permission_button')
        else:
            permission_button.click()

    def click_agree(self):
        try:
            agree_button = self.find_element(self.agree_button)
        except NoSuchElementException:
            print('no agree_button')
        else:
            agree_button.click()
    #点击取消
    def click_chancel(self):
        try:
            chancel_button=self.find_element(self.chancel_button)
        except NoSuchElementException:
            print('no chancel_button')
        else:
            chancel_button.click()
    #点击设置
    def click_setting(self):
        try:
            setting= self.find_element(self.setting_button)
        except NoSuchElementException:
            print('no setting_button')
        else:
            setting.click()

    #点击退出登录
    def click_logout_button(self):
        try:
            logout_button = self.find_element(self.logout_button)
        except NoSuchElementException:
            print('no logout_button')
        else:
            logout_button.click()

    #修改成功提示
    def modify_success(self):
        return self.find_toast(self.modify_success_toast).text

    #保存成功提示
    def save_success(self):
        return self.find_toast(self.save_success_toast).text

    #点击返回
    def click_back(self):
        self.click(self.back_button)

    #关闭
    def click_close(self):
        self.click(self.close_loc)

    #点击‘我’
    def click_me(self):
        try:
            me_button = self.find_element(self.me_button)
        except NoSuchElementException:
            print('no me_button')
        else:
            me_button.click()

    #下一个
    def click_next_one(self):
        try:
            next_one = self.find_element(self.next_one_loc)
        except NoSuchElementException:
            print('没有下一个')
        else:
            next_one.click()
    #手机返回键
    def click_phone_back(self):
        self.driver.press_keycode(4)
