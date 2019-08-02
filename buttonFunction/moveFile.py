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
from common.comfunction import com_upload   # 公共上传函数
from common.comfunction import com_upload_min # 公共上传函数,时间缩短
from common.comfunction import com_xpath  # 公共的定位方法类
from common.comfunction import com_alert  #  公共的弹窗方法类
from common.comfunction import com_share  #  分享类公共方法

resultPath = "C:\\work\\1测试\\10自动化\\报告\\"

# 验证移动功能，文件移动，文件夹移动，移动的重名处理
# 移动文件夹，私有，根目录到子目录，子目录到根目录(直接重名验证)
# 移动文件夹，团队，根目录到子目录，子目录到根目录(直接重名验证)
# 移动文件，私有，子目录到根目录，根目录到子目录，移动重名问题（同类型，不同类型）,艾玛文件移动出来
# 移动文件，团队，子目录到根目录，根目录到子目录，移动文件重名问题（同类型，不同类型）

class test_move(unittest.TestCase):
    '''验证文件和文件夹的移动'''
    # 公共参数
    picturePath = "C:\\work\\1测试\\10自动化\\截图保存\\移动\\"  # 生成截图路径
    upload_url = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\图例提取文件\\"
    upload_name = "表格图片"
    upUrl = upload_url + upload_name + ".doc"

    mode = 1
    driver = execBrower(mode)
    user().login(driver)
    def test_moveFolder_private(self):
        '''私有中移动文件夹(重名)'''
        folder1 = str(time.time())
        # 子目录到根目录
        user().createFolder(self.driver, folder1)
        self.driver.find_element_by_xpath("//span[text()='"+folder1+"']").click()
        user().createFolder(self.driver, folder1)
        el11 = self.driver.find_elements_by_xpath("//input[@class='ant-checkbox-input']")
        el13 = self.driver.find_element_by_xpath("//span[text()='"+folder1+"']")
        ActionChains(self.driver).move_to_element(el13).perform()
        el11[1].click()
        button = "move"
        el12 = com_xpath().com_listButton(self.driver, button)
        el12.click()
        # 验证移动弹框取消功能
        type = "取 消"
        type1 = "私有"
        type3 = "确 定"
        com_alert().com_move(self.driver, self.picturePath, type3, folder1) # 验证移动选择自己的情况
        sleep(0.5)
        self.driver.find_element_by_xpath("//span[text()='"+type+"']/..").click()
        el12.click()
        com_alert().com_move(self.driver, self.picturePath, type3, type1)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="子目录到根目录移动")
        self.driver.find_element_by_xpath("//a[text()='私有']").click()
        sleep(1)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="根目:"+folder1+"为移动文件")
        # 根目录移动到子目录
        folder12 = str(time.time())
        user().createFolder(self.driver, folder12)
        self.driver.find_element_by_xpath("//span[text()='"+folder12+"']").click()
        user().createFolder(self.driver, folder1)
        self.driver.back()
        el15 = self.driver.find_element_by_xpath("//span[text()='" + folder1 + "']")
        el14 = self.driver.find_element_by_xpath(
            "//span[text()='"+folder1+"']/../../../../../../../../..//input[@class='ant-checkbox-input']")
        ActionChains(self.driver).move_to_element(el15).perform()
        print(el14)
        el14.click()
        el12.click()
        com_alert().com_move(self.driver, self.picturePath, type3, folder12)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="根目录移动到子目录")
        self.driver.find_element_by_xpath("//span[text()='"+folder12+"']").click()
        sleep(1)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="根目:" + folder1 + "为移动文件")

    def test_moveFolder_team(self):
        '''移动团队中文件夹（重名）'''
        team_name = team().check_team(self.driver)
        folder2 = str(time.time())
        # 新建文件夹
        user().createFolder(self.driver, folder2)
        self.driver.find_element_by_xpath("//span[text()='"+folder2+"']").click()
        user().createFolder(self.driver, folder2)
        el21 = self.driver.find_element_by_xpath("//span[text()='"+folder2+"']")
        ActionChains(self.driver).move_to_element(el21).perform()
        el22 = self.driver.find_elements_by_xpath("//input[@class='ant-checkbox-input']")
        el22[1].click()
        button = "move"
        el23 = com_xpath().com_listButton(self.driver, button)
        el23.click()
        button = "取 消"
        button2 = "确 定"
        com_alert().com_move(self.driver, self.picturePath, button2, folder=folder2) # 移动选择自己
        sleep(0.5)
        self.driver.find_element_by_xpath("//span[text()='"+button+"']/..").click()
        el23.click()
        com_alert().com_move(self.driver, self.picturePath, button2, folder=team_name)
        sleep(0.5)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="子目录移动到根目录")
        self.driver.back()
        sleep(0.5)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="移动目录为："+folder2)

        # 根目录移动到子目录
        folder21 = str(time.time())
        user().createFolder(self.driver, folder21)
        self.driver.find_element_by_xpath("//span[text()='"+folder21+"']").click()
        user().createFolder(self.driver, folder2)
        self.driver.back()
        el24 = self.driver.find_element_by_xpath("//span[text()='" + folder2 + "']")
        el25 = self.driver.find_element_by_xpath(
            "//span[text()='"+folder2+"']/../../../../../../../../..//input[@class='ant-checkbox-input']")
        ActionChains(self.driver).move_to_element(el24).perform()
        el25.click()
        el23.click()
        com_alert().com_move(self.driver, self.picturePath, button, folder21)
        self.driver.forward()
        sleep(0.5)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="根目录移动到子目录："+folder2)

    # 团队中移动文件
    def test_moveFile_team(self):
        '''移动团队中文件（重名）'''
        team_name = team().check_team(self.driver)
        folder3 = str(time.time())
        # 上传文件
        version = "以新版本覆盖"
        print_name = "团队根目录上传"
        com_upload_min(version, print_name, self.picturePath, self.upUrl, self.driver)
        user().createFolder(self.driver, folder3)
        self.driver.find_element_by_xpath("//span[text()='"+folder3+"']").click()
        print_name = "团队子目录上传"
        com_upload_min(version, print_name, self.picturePath, self.upUrl, self.driver)
        el31 = self.driver.find_element_by_xpath("//span[text()='"+self.upload_name+"']")
        el32 = self.driver.find_element_by_xpath(
            "//span[text()='"+self.upload_name+"']/../../../../../../../../..//input[@class='ant-checkbox-input']")
        ActionChains(self.driver).move_to_element(el31).perform()
        el32.click()
        button = "move"
        el33 = com_xpath().com_listButton(self.driver, button)
        el33.click()
        button = "取 消"
        com_alert().com_move(self.driver, self.picturePath, button, folder3)
        el33.click()
        button = "确 定"
        com_alert().com_move(self.driver, self.picturePath, button, team_name)
        com_alert().com_equal(self.driver, self.picturePath, print_name="移动冲突", version="保留两者")
        sleep(0.5)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="子目录移动到根目录")
        self.driver.back()
        sleep(0.5)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="移动目录为："+folder3)
        folder31 = str(time.time())
        user().createFolder(self.driver, folder31)
        self.driver.find_element_by_xpath("//span[text()='"+folder31+"']").click()
        com_upload_min(version, print_name, self.picturePath, self.upUrl, self.driver)
        self.driver.back()
        sleep(0.5)
        self.driver.find_element_by_xpath("//img[@type='teamFolder']").click()
        for i in range(15):
            try:
                el34 = self.driver.find_element_by_xpath("//span[text()='" + self.upload_name + "']")
                el35 = self.driver.find_element_by_xpath(
                    "//span[text()='" + self.upload_name + "']/../../../../../../../../..//input[@class='ant-checkbox-input']")
                ActionChains(self.driver).move_to_element(el34).perform()
                ActionChains(self.driver).move_to_element(el34).perform()
                el35.click()
                break
            except:
                ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
        el33.click()
        com_alert().com_move(self.driver, self.picturePath, button, folder31)
        com_alert().com_equal(self.driver, self.picturePath, print_name="移动冲突", version="保留两者")
        sleep(0.5)
        self.driver.forward()
        comHtml().screen_shot(self.driver, self.picturePath, print_name="根目录移动到子目录")

    # 私有中移动文件
    def test_moveFile_private(self):
        '''私有中移动文件（重名）'''
        user().root_private(self.driver)
        sleep(0.5)
        folder4 = str(time.time())
        version = "以新版本覆盖"
        print_name = "私有根目录上传"
        com_upload_min(version, print_name, self.picturePath, self.upUrl, self.driver)
        sleep(0.5)
        user().createFolder(self.driver, folder4)
        self.driver.find_element_by_xpath("//span[text()='"+folder4+"']").click()
        version = "以新版本覆盖"
        print_name = "私有子目录上传"
        com_upload_min(version, print_name, self.picturePath, self.upUrl, self.driver)
        el41 = self.driver.find_element_by_xpath("//span[text()='"+self.upload_name+"']")
        el42 = self.driver.find_element_by_xpath(
            "//span[text()='"+self.upload_name+"']/../../../../../../../../..//input[@class='ant-checkbox-input']")
        ActionChains(self.driver).move_to_element(el41).perform()
        el42.click()
        button = "move"
        el43 = com_xpath().com_listButton(self.driver, button)
        el43.click()
        type = "取 消"
        com_alert().com_move(self.driver, self.picturePath, type, folder4)
        type = "确 定"
        el43.click()
        com_alert().com_move(self.driver, self.picturePath, type, folder="私有")
        com_alert().com_equal(self.driver, self.picturePath, print_name="移动冲突", version="保留两者")
        comHtml().screen_shot(self.driver, self.picturePath, print_name="子目录移动到根目录")
        self.driver.back()
        folder41 = str(time.time())
        user().createFolder(self.driver, folder41)
        self.driver.find_element_by_xpath("//span[text()='"+folder41+"']").click()
        version = "以新版本覆盖"
        print_name = "私有子目录上传"
        com_upload_min(version, print_name, self.picturePath, self.upUrl, self.driver)
        self.driver.back()
        sleep(1)
        self.driver.find_element_by_xpath("//img[@type='folder']").click()
        for i in range(15):
            try:
                el44 = self.driver.find_element_by_xpath("//span[text()='" + self.upload_name + "']")
                el45 = self.driver.find_element_by_xpath(
                    "//span[text()='" + self.upload_name + "']/../../../../../../../../..//input[@class='ant-checkbox-input']")
                ActionChains(self.driver).move_to_element(el44).perform()
                ActionChains(self.driver).move_to_element(el44).perform()
                el45.click()
                break
            except:
                ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
        el43.click()
        type = "确 定"
        com_alert().com_move(self.driver, self.picturePath, type, folder=folder41)
        com_alert().com_equal(self.driver, self.picturePath, print_name="移动冲突", version="保留两者")
        sleep(0.5)
        self.driver.forward()
        sleep(1)
        comHtml().screen_shot(self.driver, self.picturePath, print_name="根目录移动到子目录")

    def test_quit(self):
        '''关闭浏览器'''
        self.driver.quit()


if __name__ == "__main__":
    case = unittest.TestSuite()
    case.addTest(test_move("test_moveFolder_private"))
    case.addTest(test_move("test_moveFolder_team"))
    case.addTest(test_move("test_moveFile_team"))
    case.addTest(test_move("test_moveFile_private"))
    case.addTest(test_move("test_quit"))

    fp = open(resultPath+"移动功能验证.html", "wb")
    runner = HTMLTestRunner(stream=fp, title="移动验证报告", description="验证文件夹、文件移动和移动重名")
    runner.run(case)
    fp.close()


