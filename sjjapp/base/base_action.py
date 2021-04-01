# -*- coding: utf-8 -*-
from time import sleep

import logging
from selenium.webdriver.support.wait import WebDriverWait
from common.desired_caps1 import appium_desired
#创建一个基类，封装元素查找，点击，输入等方法

class BaseAction():

    def __init__(self,driver):
    #driver实例化
        self.driver=driver

    #点击
    def click(self,loc):
        self.find_element(loc).click()
    #清除
    def clear(self,loc):
        self.find_element(loc).clear()
    #输入
    def input_text(self,loc,text):
        self.find_element(loc).send_keys(text)
    #拖拽
    def drag(self,loc1,loc2):
        return self.driver.drag_and_drop(loc1,loc2)

    #查找单个元素
    def find_element(self, loc):
        by=loc[0]
        value=loc[1]
        return self.driver.find_element(by,value)

    # 查找多个元素
    def find_elements(self, loc):
        by=loc[0]
        value=loc[1]
        return WebDriverWait(self.driver,5,1).until(lambda x:x.find_elements(by, value))

    def find_toast(self,value):
        message = '//*[@text=\'{}\']'.format(value)
        return WebDriverWait(self.driver, 5,1).until(lambda x: x.find_element_by_xpath(message))

    #触碰操作
    def tap(self,loc):
        by=loc[0]
        value=loc[1]
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.tap(by, value))

    #截图
    def get_screenshot(self,text):
        self.driver.save_screenshot(text)

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    #向上滑动
    def swipeUp(self):
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.2)
        y2 = int(l[1] * 0.9)
        self.driver.swipe(x1, y1, x1, y2, 800)

    #向下滑动
    def swipeDown(self):
        l = self.get_size()
        x1 = int(l[0] * 0.8)
        y1 = int(l[1] * 0.9)
        y2 = int(l[1] * 0.2)
        self.driver.swipe(x1, y1, x1, y2, 700)

    def assert_existed(self,loc,element):
        by = loc[0]
        value = loc[1]
        ele=self.driver.find_element(by, value).text
        assert ele==str(element),"断言{}元素存在,失败!".format(ele)
        logging.info('断言{}元素存在,成功'.format(ele))



if __name__ == '__main__':
    dr= appium_desired()
    b=BaseAction()
    print(b.get_size())
    sleep(2)
    b.swipeDown()

