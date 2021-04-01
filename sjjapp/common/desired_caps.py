#coding=utf-8
__author__ = 'Murphy'
import os
import sys
import yaml
from appium import webdriver
import logging
import logging.config
sys.path.append(os.getcwd())
CON_LOG='../config/log.conf'
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), CON_LOG)
logging.config.fileConfig(log_file_path)
logging = logging.getLogger()

def appium_desired():
    base_dir = os.path.dirname(os.getcwd())
    with open('../config/desired_caps.yml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    desired_caps={}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['unlockType'] = data['unlockType']
    desired_caps['unlockKey'] = data['unlockKey']
    desired_caps['automationName'] = data['automationName']


    os.system('adb kill-server')
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    logging.info('设备信息：{}'.format(desired_caps['deviceName']))
    driver.implicitly_wait(2)
    return driver

