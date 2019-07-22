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

# 收藏功能验证，以PDF文件验证，预览中，边写边搜中，文件夹中（工具栏），文件夹内搜索中
# 不包含比对报告收藏

resultpath = "C:\\work\\1测试\\10自动化\\报告\\"
# 收藏
class test_store(unittest.TestCase):
    '''测试收藏功能'''
    # 公共参数
    picturePath = "C:\\work\\1测试\\10自动化\\截图保存\\19种上传格式截图\\other\\" # 生成截图路径
    showPath = "file:///C:/work/1测试/10自动化/截图保存/19种上传格式截图/other/" # 截图输出路径，目前废弃
    qpath = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\其他\\"    # 上传路径
    pdfname = "146页年度报告"    # 上传文件名
    folder12 = time.time()   #  新建的文件夹，私有中边写边搜用

    # 启动浏览器
    mode = 2
    driver = execBrower(mode)
    user().login(driver)
    driver.implicitly_wait(30)
    # 检查团队
    team_name = team().check_team(driver)

    # 上传预览中收藏
    def test_viewStore(self):
        '''团队预览中收藏'''

        # 上传文件
        uploadUrl = self.qpath + self.pdfname + ".PDF"
        version = "以新版本覆盖"
        print_name = "预览收藏--上传"
        pic_path = self.picturePath
        com_upload(version, print_name, pic_path, uploadUrl, self.driver)
        self.driver.refresh()
        sleep(3)
        # 点击文件
        self.driver.find_element_by_xpath("//span[text()='"+self.pdfname+"']/..").click()
        try:
            #  确认文件已打开预览
            WebDriverWait(self.driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
            buttonType = "store"  # 表明是收藏按钮
            el11 = com_xpath().com_preview(self.driver, buttonType)
            if el11 != "":
                el11.click()
                version = "以新版本覆盖"
                print_name = "预览收藏"
                com_alert().com_equal(self.driver, pic_path, print_name, version)
                self.driver.find_elements_by_xpath("//span[contains(text(),'返回')]")
                sleep(1)
        except Exception as e:
            print(e)
            print("没有打开预览")

    def test_listStore(self):
        '''列表中收藏'''
        el21 = self.driver.find_element_by_xpath("//span[text()='"+self.pdfname+"']")
        ActionChains(self.driver).move_to_element(el21).perform()
        el22 = self.driver.find_elements_by_xpath("//input[@class='ant-checkbox-input']")
        #  新上传覆盖过所以这里在第一个（排除全选按钮）
        el22[1].click()
        type = 'store'
        el23 = com_xpath().com_listButton(self.driver, type)
        if el23 != "":
            el23.click()
            version = "以新版本覆盖"
            print_name = "列表收藏"
            com_alert().com_equal(self.driver, self.picturePath, print_name, type)
            sleep(1)



    # def test_folderSearchStore(self):
    #     '''文件夹内搜索收藏'''

    # def test_modifyStore(self):
    #     '''边写边搜中收藏'''


if __name__ == "__main__":
    testUnite = unittest.TestSuite()
    testUnite.addTest(test_store("test_viewStore"))
    testUnite.addTest(test_store("test_listStore"))

    fp = open(resultpath + "收藏验证.html", "wb")
    runner = HTMLTestRunner(stream=fp, title="收藏功能测试报告", description="预览，列表、搜索、边写边搜验证收藏")
    runner.run(testUnite)
    fp.close()



