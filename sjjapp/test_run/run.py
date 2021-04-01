import os
import sys
import time
import unittest
from BSTestRunner import BSTestRunner

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

test_dir = '../Testcase/'  #指定当前文件夹下的Interface目录
file = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')    #匹配开头为test的py文件

if __name__=="__main__":

    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))    # 取当前时间
    public_path = os.path.dirname(os.path.abspath(sys.argv[0]))       # 获取当前运行的.py文件所在的绝对路径
    filename = public_path + "\\" + now + "report.html"   #保存的报告路径和名称
    fp = open(filename, 'wb')
    runner = BSTestRunner(stream=fp,
                            title="书加加测试报告",
                            description="测试内容书加加内容测试"
                            )
    runner.run(file)     #执行测试套件
    fp.close()
    