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
from common.comfunction import execBrower  # 启动浏览器函数
from common.comfunction import user  # 用户登录类
from common.comfunction import comHtml  # 生成html报告类
from common.comfunction import team  # 团队类
from common.comfunction import com_upload # 公共上传函数
from common.comfunction import com_xpath  # 公共的定位方法类
from common.comfunction import com_alert  #  公共的弹窗方法类
from common.comfunction import com_share  #  分享类公共方法

resultPath = "C:\\work\\1测试\\10自动化\\报告\\"
# 验证团队导入功能
# 1.私有中文件夹，上传文件
# 2.检查团队，进入团队，导入文件（截图弹窗，刷新之后截图导入结果）
# 3.团队中创建目录，进入目录导入（截图弹窗，刷新之后截图导入结果）
# 4.预览导入的文件（截图预览结果），然后退出

class test_teamImportFile(unittest.TestCase):
    '''验证团队导入功能'''
    # 设置公共参数
    picturePath = "C:\\work\\1测试\\10自动化\\截图保存\\19种上传格式截图\\other\\"  # 生成截图路径
    uploadPath = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\图例提取文件\\"  # 上传路径
    wordName = "结构复杂的文件"   # 后缀是doc
    wordurl = uploadPath+wordName+".doc"
    folder = str(time.time())

    # 启动浏览器,并且登录
    mode  = 2
    driver = execBrower(mode)
    user().login(driver)
    user().createFolder(driver, folder)
    #  进入文件夹上传文件
    driver.find_element_by_xpath("//span[text()='"+folder+"']/..").click()
    driver.find_element_by_xpath("//input[@type='file']").send_keys(wordurl)
    sleep(15)
    team_name = team().check_team(driver)

    #  进入团队，导入
    def test_teamRootImport(self):
        '''团队根目录导入'''
        button = "import1"
        el11 = com_xpath().com_listButton(self.driver, button)
        el11.click()
        com_alert().com_importalert(self.driver, self.folder, self.wordName, self.picturePath, print_name="导入结果")

    # 团队子目录导入
    def test_teamSubImport(self):
        '''团队子目录导入文件'''
        user().createFolder(self.driver, self.folder)
        self.driver.find_element_by_xpath("//span[text()='"+self.folder+"']/..").click()
        sleep(0.5)
        button = "import1"
        el11 = com_xpath().com_listButton(self.driver, button)
        el11.click()
        com_alert().com_importalert(self.driver, self.folder, self.wordName, self.picturePath, print_name="导入结果")
        sleep(2)
        try:
            WebDriverWait(self.driver, 10, 0.5).until(ec.element_to_be_clickable((By.XPATH, "//span[text()='"+self.wordName+"']/..")))
            self.driver.find_element_by_xpath("//span[text()='"+self.wordName+"']/..").click()
            try:
                WebDriverWait(self.driver, 7, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
                picname = "导入文件预览截图"
                datename22 = str(int(time.time()))
                self.driver.get_screenshot_as_file(self.picturePath+datename22+".png")
                comHtml().print_html(picname, self.picturePath, datename22)
            except Exception as e:
                print(e)
                print("预览等待超时")
        except Exception as e:
            print(e)
            print("等待超时没有打开预览")
            datename21 = str(int(time.time()))
            self.driver.get_screenshot_as_file(self.picturePath+datename21+".png")
            picname = "异常截图"
            comHtml().print_html(picname, self.picturePath, datename21)
        sleep(1)

    # 退出浏览器方法，兼容报错的情况
    def test_quit(self):
        '''退出浏览器'''
        self.driver.quit()

if __name__ == "__main__":
    testcase = unittest.TestSuite()
    testcase.addTest(test_teamImportFile("test_teamRootImport"))
    testcase.addTest(test_teamImportFile("test_teamSubImport"))
    testcase.addTest(test_teamImportFile("test_quit"))

    fp = open(resultPath+"团队导入测试结果.html", "wb")
    runner = HTMLTestRunner(stream=fp, title="测试团队导入功能", description="根目录和子目录的导入，并且预览")
    runner.run(testcase)
    fp.close()
















