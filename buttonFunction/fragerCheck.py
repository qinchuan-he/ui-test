# coding=utf-8
import io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# 报告
import unittest
from HTMLTestRunner import HTMLTestRunner
from time import sleep
import time  # 生成时间戳用
import os  # 上传autoit用
import sys
import re # 正则提取
"""解决vscode中不能引用别的模块的问题"""
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# print(sys.path)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

# 引入公共方法
from common.comfunction import OpenBrowser  # 启动浏览器函数
from common.comfunction import User  # 用户登录类
from common.comfunction import comHtml  # 生成html报告类
from common.comfunction import team  # 团队类
from common.comfunction import com_upload # 公共上传函数
from common.comfunction import com_xpath  # 公共的定位方法类
from common.comfunction import com_alert  #  公共的弹窗方法类
from common.comfunction import com_path

# 零散功能验证，验证文件何文件夹名字长度，看板显示等

resultpath = os.path.join(com_path(),"报告")
class test_frager(unittest.TestCase):
    '''零散的验证，主要是ui方面的检查'''
    # 公共参数
    mode = 2
    picturePath = com_path()+"截图\\"+"零散\\"  # 生成截图路径
    if not (os.path.exists(picturePath)):
        os.makedirs(picturePath)
    print("============="+picturePath)
    fpath = com_path()+"19种格式\\office\\"
    word1name = "2017年12月11日-2017年12月15日发行监管部"
    lname = "赵客缦胡缨吴钩霜雪明银鞍照白马飒沓如流星十步杀一人千里不留行事了拂衣去深藏身与名闲过信陵饮脱剑膝前横将炙啖朱亥持觞劝侯嬴"

    # 启动浏览器
    driver = OpenBrowser(mode)
    User().login(driver)

    def test_filePath(self):
        '''检查文件夹路径'''

        folder1 = str(time.time())


        User().createFolder(self.driver, folder1)
        self.driver.find_element_by_xpath("//span[text()='"+folder1+"']").click()
        sleep(0.5)
        User().createFolder(self.driver, self.lname)
        self.driver.find_element_by_xpath("//span[text()='"+self.lname+"']").click()
        sleep(0.5)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="路径栏中名称显示")
        self.driver.back()
        sleep(0.5)
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.fpath + self.word1name + ".doc")
        sleep(7)
        button = "switch"
        el11 = com_xpath().com_listButton(self.driver, button)
        el11.click()
        sleep(0.5)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="平铺中截图")
        self.driver.find_element_by_xpath("//div[text()='"+self.word1name+"']").click()
        ActionChains(self.driver)
        self.driver.switch_to.active_element.send_keys(self.lname)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        sleep(0.5)
        el11.click()
        sleep(0.5)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="列表截图")
        sleep(1)
        team_name = team().check_team(self.driver)
        User().createFolder(self.driver, folder1)
        sleep(0.5)
        self.driver.find_element_by_xpath("//span[text()='"+folder1+"']").click()
        sleep(0.5)
        User().createFolder(self.driver, self.lname)
        self.driver.find_element_by_xpath("//span[text()='"+self.lname+"']").click()
        sleep(0.5)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="团队路径栏截图")
        sleep(0.5)
        self.driver.back()
        sleep(0.5)
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.fpath + self.word1name + ".doc")
        sleep(7)
        button = "switch"
        el12 = com_xpath().com_listButton(self.driver, button)
        el12.click()
        sleep(0.5)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="团队平铺中截图")
        self.driver.find_element_by_xpath("//div[text()='" + self.word1name + "']").click()
        self.driver.switch_to.active_element.send_keys(self.lname)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        sleep(0.5)
        el12.click()
        sleep(0.5)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="团队列表截图")
        sleep(1)
        searchKey = "doc"
        com_xpath().com_internalSearch(self.driver, searchKey)
        sleep(15)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="文件夹内搜索截图")
        sleep(0.5)
        self.driver.quit()



if __name__ == "__main__":

    case = unittest.TestSuite()
    case.addTest(test_frager("test_filePath"))

    fp = open(resultpath+"零散功能验证.html", "wb")
    runner = HTMLTestRunner(stream=fp, title="零散功能验证", description="验证文件名长度显示等")
    runner.run(case)
    fp.close()

















