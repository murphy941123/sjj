# -*- coding: utf-8 -*-
import os,sys
import logging
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from common.desired_caps1 import appium_desired
from page.me_page import MePage
sys.path.append(os.getcwd())

class HomePage(MePage):
    search_loc = By.XPATH, "//*[@text='搜索图书音频']"
    search_but = By.XPATH, "//android.view.ViewGroup[2]/android.widget.TextView[1]"
    lesson_button = By.XPATH, "//*[@text='课程']"
    download_toast_loc = "已加入下载队列"
    home_page_loc = By.XPATH, "//android.widget.LinearLayout/android.widget.FrameLayout[1]"
    lesson_text = By.XPATH, "//*[@text='（英一）22考研英语名师全程伴学营']"
    lesson_loc= By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[1]"
    catalogue_loc = By.XPATH, "//*[@text='目录']"
    download_loc = By.XPATH, "//android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ImageView[1]"
    my_cache_loc = By.XPATH, "//*[@text='我的缓存']"
    living_lesson_loc=By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[5]"
    fanwen_lesson_loc = By.XPATH, "//android.widget.ScrollView / android.view.ViewGroup[1] / android.view.ViewGroup[7]"
    one_times_speed = By.XPATH, "//*[@text='1x']"
    one_point_two_times_speed = By.XPATH, "//*[@text='1.2x']"
    one_point_five_times_speed = By.XPATH, "//*[@text='1.5x']"
    two_times_speed = By.XPATH, "//*[@text='2x']"
    zero_point_five_times_speed = By.XPATH, "//*[@text='0.5x']"
    zero_point_eight_times_speed = By.XPATH, "//*[@text='0.8x']"
    speed_loc = By.XPATH, "//android.view.ViewGroup[1]/android.view.ViewGroup[4]"
    Is_the_cache = By.XPATH, "//android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]"
    full_screen_loc = By.XPATH, "//android.view.ViewGroup[1]/android.view.ViewGroup[6]"
    playback_loc = By.XPATH, "//android.view.ViewGroup[1]/android.view.ViewGroup[3]"
    stop_loc = By.XPATH, "//android.view.ViewGroup[1]/android.view.ViewGroup[1]"
    switch_line_loc = By.XPATH, "//android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]"
    line2_loc = By.XPATH, "//*[@text='线路二']"
    buy_loc = By.XPATH, "//*[@text='立即抢购']"
    recommended_course_loc = By.XPATH, "//*[@text='推荐课程']"
    choose_recommended_course_loc = By.XPATH, "//android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View[1]"
    Audio_speed_loc = By.XPATH, "//android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[6]"
    Next_loc = By.XPATH, "//android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[5]"
    Last_loc = By.XPATH, "//android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[4]"
    stop_or_play_loc = By.XPATH, "//android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[3]"
    Audio_playback_loc = By.XPATH, "//android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[2]"
    download_Audio_loc = By.XPATH, "//android.view.ViewGroup[8]/android.view.ViewGroup[1]/android.widget.ImageView[1]"
    play_pattern_loc = By.XPATH, "//android.view.ViewGroup[8]/android.view.ViewGroup[2]/android.widget.ImageView[1]"
    speed_play_loc = By.XPATH, "//android.view.ViewGroup[8]/android.view.ViewGroup[3]/android.widget.ImageView[1]"
    play_list_loc = By.XPATH, "//android.view.ViewGroup[8]/android.view.ViewGroup[4]/android.widget.ImageView[1]"
    origin_el = By.XPATH, "//android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]"
    destination_el = By.XPATH, "//android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[4]"
    choose_play_Audio_loc = By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]"
    close_play_list_loc = By.XPATH, "//*[@text='关闭']"
    unfold_loc = By.XPATH, "//*[@text='展开']"
    pack_up_loc = By.XPATH, "//*[@text='收起']"
    questions_area_loc = By.XPATH, "//*[@text='提问区']"
    discussion_area_loc = By.XPATH, "//*[@text='讨论区']"
    give_a_like = By.XPATH, "//*[@text='李花花 ：给老师点赞']"
    Audio_Icon_loc=By.XPATH,"//android.view.ViewGroup[1]/android.widget.ImageView[1]"
    Audio_back_loc=By.XPATH,"//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]"
    Learning_mode_loc = By.XPATH, "//*[@text='ic_learn@3x']"
    Review_to_consolidate_loc = By.XPATH, "//*[@text='ic_fxgg@3x']"
    The_new_words_loc = By.XPATH, "//*[@text='ic_scb@3x']"
    Browse_the_words_loc = By.XPATH, "//*[@text='ic_lldc@3x']"
    list_loc = By.XPATH, "// *[ @ text = 'ic_phb@3x']"
    remember_word_loc = By.XPATH, "//*[@text='背单词']"
    word_book_loc = By.XPATH, "//*[@text='20天背完六级核心词汇']"
    change_word_book_loc = By.XPATH, "//*[@text='更换词书']"
    start_remember_word_loc = By.XPATH, "//*[@text='开始背单词']"
    remember_loc=By.XPATH, "//*[@text='已记住']"
    dont_remember_loc=By.XPATH, "//*[@text='不认识']"
    last_loc = By.XPATH, "//*[@text='bt_previous%20_disabled@3x']"
    next_loc = By.XPATH, "//*[@text='bt_next@3x']"
    choose_word_meaning=By.XPATH, "//android.view.View[3]"
    scrambled_mode_loc=By.XPATH, "//*[@text='乱序']"
    normal_mode_loc=By.XPATH, "//*[@text='原序']"
    ten_words_loc = By.XPATH, "//*[@text='每次10词']"
    word_num_loc=By.XPATH, "//*[@text='每次20词']"
    thirty_words_loc = By.XPATH, "//*[@text='每次30词']"
    selection_sort_loc=By.XPATH, "//*[@text='大学英语']"
    word_process_loc=By.XPATH,"//*[@text='0/2000']"
    continue_loc=By.XPATH, "//*[@text='继续']"
    twenty_words_loc=By.XPATH, "//*[@text='1/20']"

    def __init__(self,driver):
        #init里面可以去写已经确定的这个模块所有前置功能
        BaseAction.__init__(self,driver)
        self.click_chancel()

    #搜索课程
    def search_lesson(self):
        logging.info('点击搜索框')
        self.click(self.search_loc)
        logging.info('点击搜索搜索图书音频并输入（英一）22考研英语名师全程伴学营')
        self.input_text(self.search_loc,'（英一）22考研英语名师全程伴学营')
        logging.info('点击搜索')
        self.click(self.search_but)
        logging.info('点击课程')
        self.click(self.lesson_button)
    def check_search_lesson(self):
        try:
             lesson_name=self.find_element(self.lesson_text).text
        except NoSuchElementException:
            print('课程已下架')
            return False
        else:
            if lesson_name=='（英一）22考研英语名师全程伴学营':
                self.get_screenshot('../screenshot/lesson/搜索课程.png')
                return True

    #直播课
    def living_lesson(self):
        logging.info('点击课程')
        self.click(self.lesson_loc)
        logging.info('点击目录')
        self.click(self.catalogue_loc)
        logging.info('点击直播')
        self.click(self.living_lesson_loc)
        logging.info('全屏')
        self.click(self.full_screen_loc)
        time.sleep(2)
        #1.2倍速播放
        logging.info('1.2倍速播放')
        self.click(self.one_times_speed)
        time.sleep(2)
        self.get_screenshot('../screenshot/lesson/1.2倍速度播放.png')
        #1.5倍速播放
        logging.info('1.5倍速播放')
        self.click(self.one_point_two_times_speed)
        time.sleep(2)
        self.get_screenshot('../screenshot/lesson/1.5倍速度播放.png')
        #2倍速播放
        logging.info('2倍速播放')
        self.click(self.one_point_five_times_speed)
        time.sleep(2)
        self.get_screenshot('../screenshot/lesson/2倍速度播放.png')
        #0.5倍速播放
        logging.info('0.5倍速播放')
        self.click(self.two_times_speed)
        time.sleep(2)
        self.get_screenshot('../screenshot/lesson/0.5倍速度播放.png')
        # 0.8倍速播放
        logging.info('0.8倍速播放')
        self.click(self.zero_point_five_times_speed)
        time.sleep(2)
        self.get_screenshot('../screenshot/lesson/0.8倍速度播放.png')
        #1倍速播放
        logging.info('1倍速播放')
        self.click(self.zero_point_eight_times_speed)
        time.sleep(2)
        self.get_screenshot('../screenshot/lesson/1倍速度播放.png')
        logging.info('快进')
        self.click(self.speed_loc)
        logging.info('快退')
        self.click(self.playback_loc)
        logging.info('暂停')
        self.click(self.stop_loc)
        time.sleep(2)
        self.get_screenshot('../screenshot/lesson/视频播放.png')
        self.driver.press_keycode(4)
        logging.info('点击展开')
        self.click(self.unfold_loc)
        time.sleep(2)
        logging.info('点击收起')
        self.click(self.pack_up_loc)
        #提问区
        logging.info('点击提问区')
        self.click(self.questions_area_loc)
        #讨论区
        logging.info('点击讨论区')
        self.click(self.discussion_area_loc)

    def check_living_lesson(self):
        try:
            give_a_like = self.find_element(self.give_a_like).text
        except NoSuchElementException:
            print('课程已下架')
            return False
        else:
            if give_a_like == '李花花 ：给老师点赞':
                self.get_screenshot('../screenshot/lesson/直播课.png')
                return True

    #音频播放
    def Audio_play(self):
        self.driver.press_keycode(4)
        logging.info('点击推荐课程')
        self.click(self.recommended_course_loc)
        logging.info('选择课程')
        self.click(self.choose_recommended_course_loc)
        logging.info('点击目录')
        self.click(self.catalogue_loc)
        #点击经典范文
        self.click(self.fanwen_lesson_loc)
        #快进
        self.click(self.Audio_speed_loc)
        #回放
        self.click(self.Audio_playback_loc)
        #下一首
        self.click(self.Next_loc)
        #上一首
        self.click(self.Last_loc)
        #暂停或者播放
        self.click(self.stop_or_play_loc)
        #下载
        self.click(self.download_Audio_loc)
        #选择播放模式
        self.click(self.play_pattern_loc)
        time.sleep(2)
        self.click(self.play_pattern_loc)
        time.sleep(2)
        self.click(self.play_pattern_loc)
        #倍速播放
        self.click(self.speed_play_loc)
        time.sleep(2)
        self.click(self.speed_play_loc)
        time.sleep(2)
        self.click(self.speed_play_loc)
        time.sleep(2)
        self.click(self.speed_play_loc)
        time.sleep(2)
        self.click(self.speed_play_loc)
        #播放列表
        self.click(self.play_list_loc)  #打开播放列表
        self.click(self.close_play_list_loc)    #关闭播放列表
        self.click(self.play_list_loc)  #打开播放列表
        self.click(self.choose_play_Audio_loc)
        # 拖拽播放
        start_el = self.find_element(self.origin_el)
        end_el = self.find_element(self.destination_el)
        self.drag(start_el, end_el)
        time.sleep(2)
        self.get_screenshot('../screenshot/lesson/音频播放.png')
        self.click(self.Audio_back_loc)
    def check_Audio_play(self):
        try:
            self.click(self.Audio_Icon_loc)
        except NoSuchElementException:
            logging.info("找不到音频小图标")
        else:
            return True

    def check_download_status(self):
        try:
            self.find_toast(self.download_toast_loc).text
        except NoSuchElementException:
            print('没有找到download_toast')
        else:
            logging.info('已加入下载队列')
            self.get_screenshot('../screenshot/已加入下载队列.jpg')
            return True

    #乱序功能
    def learning_mode1(self):
        logging.info('点击背单词')
        self.click(self.remember_word_loc)
        try:
            logging.info('更换单词书')
            self.click(self.change_word_book_loc)
            logging.info('选择单词书分类,大学英语')
            self.click(self.selection_sort_loc)
        except:
            logging.info('选择单词书分类,大学英语')
            self.click(self.selection_sort_loc)
        word_book=self.find_element(self.word_book_loc).text
        logging.info('选择{0}'.format(word_book))
        self.click(self.word_book_loc)
        logging.info('开始记单词')
        self.click(self.start_remember_word_loc)
        logging.info('已记住')
        self.click(self.remember_loc)
        logging.info('未记住')
        self.click(self.dont_remember_loc)
        self.click_phone_back()
        logging.info('学习模式')
        self.click(self.Learning_mode_loc)
        logging.info('选择乱序')
        self.click(self.scrambled_mode_loc)
        self.click(self.continue_loc)
        logging.info('选择每日20词并保存')
        self.click(self.word_num_loc)
        self.click(self.save_loc)
    def check_learning_mode1(self):
        try:
            word_process=self.find_element(self.word_process_loc).text
            print('找到：{0}'.format(word_process))
        except NoSuchElementException:
            print('没有找到0/2000')
        else:
            if word_process=='0/2000':
                print('乱序功能通过')
                return True

    #正序功能
    def learning_mode2(self):

        logging.info('开始记单词')
        self.click(self.start_remember_word_loc)
        logging.info('已记住')
        self.click(self.remember_loc)
        logging.info('未记住')
        self.click(self.dont_remember_loc)
        self.click_phone_back()
        logging.info('学习模式')
        self.click(self.Learning_mode_loc)
        logging.info('选择正序')
        self.click(self.normal_mode_loc)
        self.click(self.continue_loc)
        logging.info('选择每日20词并保存')
        self.click(self.word_num_loc)
        self.click(self.save_loc)
    def check_learning_mode2(self):
        try:
            word_process=self.find_element(self.word_process_loc).text
            print('找到：{0}'.format(word_process))
        except NoSuchElementException:
            print('没有找到0/2000')
        else:
            if word_process=='0/2000':
                print('正序功能通过')
                return True

    #每日20个单词
    def twenty_words(self):
        logging.info('开始记单词')
        self.click(self.start_remember_word_loc)
    def check_twenty_words(self):
        try:
            twenty_words = self.find_element(self.twenty_words_loc).text
            print('找到：{0}'.format(twenty_words))
        except NoSuchElementException:
            print('没有找到1/20')
        else:
            if twenty_words == '1/20':
                print('测试：选择每日20单词通过')
                return True

    # 每日30个单词词
    def thirty_words(self):
        self.click(self.close_loc)
        logging.info('学习模式')
        self.click(self.Learning_mode_loc)
        logging.info('选择每日10个单词并保存')
        self.click(self.thirty_words_loc)
        self.click(self.save_loc)
        logging.info('开始记单词')
        self.click(self.start_remember_word_loc)

    def check_thirty_words(self):
        try:
            thirty_words=self.find_element(self.thirty_words_loc).text
            print('找到：{0}'.format(thirty_words))
        except NoSuchElementException:
            print('没有找到1/20')
        else:
            if thirty_words == '1/20':
                print('测试：选择每日20单词通过')
                return True

    #每日10个单词
    def ten_words(self):
        self.click(self.close_loc)
        logging.info('学习模式')
        self.click(self.Learning_mode_loc)
        logging.info('选择每日10个单词并保存')
        self.click(self.ten_words_loc)
        self.click(self.save_loc)
        logging.info('开始记单词')
        self.click(self.start_remember_word_loc)
    def check_ten_words(self):
        try:
            ten_words = self.find_element(self.ten_words_loc).text
            print('找到：{0}'.format(ten_words))
        except NoSuchElementException:
            print('没有找到1/10')
        else:
            if ten_words == '1/10':
                print('测试：选择每日10单词通过')
                return True

if __name__ == '__main__':

    dr=appium_desired()
    h=HomePage(dr)
    h.search_lesson()
    h.living_lesson()
    h.learning_mode1()
    h.learning_mode2()
