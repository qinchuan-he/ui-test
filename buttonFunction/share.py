#coding=utf-8

import io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#报告
import unittest
from HTMLTestRunner import HTMLTestRunner
from time import sleep
import time   #生成时间戳用
import os    #上传autoit用
import sys
"""解决vscode中不能引用别的模块的问题"""
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# print(sys.path)
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


# 引入公共方法
from common.comfunction import execBrower # 启动浏览器函数
from common.comfunction import user  # 用户登录类
from common.comfunction import comHtml # 生成html报告类
from common.comfunction import team #团队类

# 分享功能验证，以PDF文件验证，预览中，边写边搜中，艾玛中（碎片分享），文件夹中（工具栏和更多），文件夹内搜索中
resultpath = "C:\\work\\1测试\\10自动化\\报告\\"
class test_share(unittest.TestCase):
    '''分享功能验证'''
        # 公共参数
    
    picturePath="C:\\work\\1测试\\10自动化\\截图保存\\19种上传格式截图\\other\\"
    showPath="file:///C:/work/1测试/10自动化/截图保存/19种上传格式截图/other/"
    # 启动浏览器
    mode = 2
    driver = execBrower(mode)
    user().login(driver)
    driver.implicitly_wait(30)

    # 创建文件夹
    el1=driver.find_element_by_xpath("//span[text()='新建']")
    sleep(1)
    ActionChains(driver).move_to_element(el1).perform()
    driver.find_element_by_xpath("//li[text()='新建文件夹']").click()
    folder1=int(time.time())
    print("新建文件夹：%s " %folder1)
    driver.switch_to.active_element.send_keys(folder1)
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    # 进入文件夹
    # driver.find_element_by_xpath("//span[text()="+str(folder1)+"]").click()    
    # 检查团队
    team().check_team(driver)
    def test_viewshare(self):
        '''上传并分享'''
        qpath = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\其他\\"
        pdfname = "146页年度报告"

        self.driver.find_element_by_xpath("//a[contains(@class,'GlobalHeader_logo')]").click()
        self.driver.find_element_by_xpath("//span[text()="+str(self.folder1)+"]").click()
            # 创建文件夹
        el12=self.driver.find_element_by_xpath("//span[text()='新建']")
        sleep(1)
        ActionChains(self.driver).move_to_element(el12).perform()
        self.driver.find_element_by_xpath("//li[text()='新建文件夹']").click()
        folder12 = "分享"
        print("新建文件夹：%s " %folder12)
        self.driver.switch_to.active_element.send_keys(folder12)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        sleep(1)
        self.driver.find_element_by_xpath("//span[text()="+"'"+folder12+"'"+"]").click()
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(qpath+pdfname+".PDF")
        sleep(30)
        self.driver.refresh()
        # 截图并输出
        sleep(4)
        date1=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date1+".png")
        comHtml().print_html("其他类型列表", self.picturePath, date1)  # 输出到html报告

if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(test_share("test_viewshare"))

    fp = open(resultpath+"分享验证.html", "wb")
    runner = HTMLTestRunner(stream = fp,title="分享功能测试报告", description="分享功能回归验证" )
    runner.run(testunit)
    fp.close()

    

