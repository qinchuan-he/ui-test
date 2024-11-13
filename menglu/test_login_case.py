# coding=utf-8

import os,sys
# 解决Linux中找不到引用问题
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)

# from common.import_elements import import_elements
from common.driver import driver
from common.mothod import *
import unittest
from HTMLTestRunner import HTMLTestRunner


resultpath = os.path.join(r"D:\4services", "报告")
class TestLoginCase(unittest.TestCase):

    # def __init__(self,*args, **kwargs):
    #     print('-------------GHJ')
    # #     # self.elements = "登录"
    #     # self.elements = import_elements("登录")
    #     # self.code = self.elements[0]
    #     # self.user = self.elements[1]
    #     # self.password = self.elements[2]
    #     # self.submit = self.elements[3]
    #     self.driver = driver

    @classmethod
    def setUp(self):

        print("开始测试")
    #
    # # @classmethod
    # # def testDown(self):
    # #     print("测试完成11")
    @classmethod
    def tearDown(self):
        print("测试完成")



    # def login(self,code,user,password):
    #     self.driver.find_element_by_xpath(self.code).send_keys(code)
    #     self.driver.find_element_by_xpath(self.user).send_keys(user)
    #     self.driver.find_element_by_xpath(self.password).send_keys(password)
    #     Mothed().sleep(3)
    #     self.driver.find_element_by_xpath(self.submit).click()

    # 方法待修改
    def test_login(self):
        # print(code,user,password)
        code_x = "//input[@placeholder='公司代码']"
        print('---------何秦川------')
        Mothed().by_path(code_x).send_keys("1234")
        # print('--------------12312------------')
        # Mothed.by_path(self.code).send_keys(code)
        # Mothed.by_path(self.user).send_keys(user)
        # Mothed.by_path(self.password).send_keys(password)
        # Mothed.by_path(self.submit).click()

    # def test_login_success(self):
    #     print('----------ABC----------')
    #     # self.test_login("fat","jk","jkl")
    #     self.test_login()
    #     # nickname= self.browser.find_element_by_xpath('//span[contains(text(),"梦露")]')
    #     # self.assertIn('梦露',nickname)
    #     print(111)
    #     # Mothed().sleep(5)
    #     # Mothed().sleep(5)
    #     # return 5


    # def login_null(self):
    #     self.login('','','')
    #     # tip = self.browser.find_element_by_xpath('//div[@id="errorTip"]').text
    #     # self.assertEqual(tip,"代码、用户名、密码不能为空！")
    #     print(222)
    #     # Mothed().sleep(5)
    #     Mothed.sleep(5)

if __name__ == "__main__":
    # unittest.main()

    TestLoginCase().test_login_success()   # 执行

    # TestLoginCase().login_null()


    # case = unittest.TestSuite()
    # case.addTest(TestLoginCase("test_login"))
    # fp = open(resultpath+"零散功能验证.html", "wb")
    # runner = HTMLTestRunner(stream=fp, title="移动验证报告", description="验证文件夹、文件移动和移动重名")
    # runner.run(case)
    # fp.close()
