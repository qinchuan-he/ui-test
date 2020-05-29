# coding=utf-8

# 造数据，两小时的检查，目前造合同防伪和智能审核的数据,扩展造别的数据，扩展拆分和合并
import sys
import os
# 解决执行不能跨包问题
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)
# print(sys.path)
from common.comfunction import OpenBrowser
from common.comfunction import User,url31,url32
import time
from time import sleep
import unittest
from HTMLTestRunner import HTMLTestRunner
from buttonFunction.function_contractrelated import contract_compare
from buttonFunction.function_contractrelated import contract_Proofreading
from buttonFunction.function_checkcontract import check_compare
from buttonFunction.function_checkcontract import check_proofreading
from buttonFunction.function_checkcontract import com_path
from common.private import UserProperty
# from upload_relate import upload_fileanalysis
resultpath = os.path.join(com_path(),"报告")
class Test_twohourse(unittest.TestCase):
    def test_create(self):
        """
        造比对和审校
        :return:
        """
        mode = 1
        driver = OpenBrowser(mode)
        driver.get(UserProperty().url)
        User().login(driver,UserProperty().user_check2)
        contract_compare(driver,url31,url32)
        sleep(1)
        contract_Proofreading(driver,url31)
        driver.quit()

    def test_split(self):
        """
        拆分
        :return:
        """

    def test_check(self):
        mode = 1
        driver = OpenBrowser(mode)
        driver.get(UserProperty().url)
        User().login(driver,UserProperty().user_check2)
        sleep(360)
        check_compare(driver,is_check="2")
        print("检查比对完毕")
        check_proofreading(driver,is_check="2")
        print("检查审校完毕")



if __name__=="__main__":
    case = unittest.TestSuite()
    case.addTest(Test_twohourse("test_create"))
    case.addTest(Test_twohourse("test_check"))
    fp = open(os.path.join(resultpath,"两小时的检查-ui.html"), "wb")
    runner = HTMLTestRunner(stream=fp, title="两小时的检查", description="检查比对和审校")
    runner.run(case)
    fp.close()


# 增加造解析数据
# upload_fileanalysis(driver)

# 增加数据，分享用






