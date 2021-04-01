import os
import time
import unittest
import warnings
import yaml
from common.desired_caps import appium_desired
import logging
from common.multi_appium import appium_start
#新建一个包含开始和结束方法的类
class StartEnd(unittest.TestCase):
    driver = None
    #读取yaml配置文件
    with open('../config/desired_caps.yml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore', ResourceWarning)
        # 启动appium服务端
        appium_start(self.data['ip'], self.data['port'])
        #启动app
        self.driver = appium_desired()
        logging.info("===test start===")

    @classmethod
    def tearDownClass(self):
        logging.info("===tear Down===")
        time.sleep(2)
        #关闭app
        self.driver.close_app()
        #断开与appium服务器的连接
        self.driver.quit()