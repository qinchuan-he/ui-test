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
    mode = 1
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
            el11 = com_xpath().com_previewButton(self.driver, buttonType)
            if el11 != "":
                el11.click()
                version = "以新版本覆盖"
                print_name = "预览收藏"
                com_alert().com_equal(self.driver, pic_path, print_name, version)
                sleep(1)
                self.driver.find_element_by_xpath("//span[contains(text(), '返回')]/..").click()
                sleep(1)
        except Exception as e:
            print(e)
            print("没有打开预览")

    #  列表中收藏
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
            com_alert().com_equal(self.driver, self.picturePath, print_name, version)
            sleep(1)

    #  文件夹内搜索中收藏
    def test_folderSearchStore(self):
        '''文件夹内搜索收藏'''
        searchKey = self.pdfname
        com_xpath().com_internalSearch(self.driver, searchKey)
        self.driver.find_element_by_xpath("//span[contains(text(),'团队共...')]/../..").click()
        sleep(1)
        print_name = "文件夹内收藏"
        version = "以新版本覆盖"
        try:
            WebDriverWait(self.driver, 5, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))# 未考虑txt
            self.driver.find_element_by_xpath("//div[contains(@class,'EmmaPage_fileViewBarList')]/div[3]").click()
            com_alert().com_equal(self.driver, self.picturePath, print_name, version)
        except Exception as e:
            print(e)
            print("超时未加载出来或者选中为txt")
        # self.driver.find_element_by_xpath("//button[@type='button']").click()
        sleep(0.5)

    #  边写边搜中收藏，列表和双屏.从文件夹内搜索中进入边写边搜
    def test_modifyStore(self):
        sleep(0.5)
        searchKey = "doc"
        com_xpath().com_internalSearch(self.driver, searchKey)
        searchTime = "时间不限"
        searchType = "Word文档"
        com_xpath().com_internalChooseType(self.driver, searchTime, searchType)
        self.driver.find_element_by_xpath("//span[text()='私有']/../..").click()
        sleep(3)
        #  进入编辑界面
        self.driver.find_element_by_xpath("//span[contains(@class,'GlobalSearchPage_cusFixButton')]").click()
        try:
            WebDriverWait(self.driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
            self.driver.find_element_by_xpath("//span[text()='边写边搜']/..").click()
            # searchKey2 = self.pdfname
            com_xpath().com_internalSearch(self.driver,self.pdfname)
            for i in range(10):
                el43 = self.driver.find_element_by_xpath("//span[contains(text(),'搜索结果数量：')]")
                el44 = int(re.findall("[0-9]+",el43.text)[0])
                if el44 > 0:
                    break
                else:
                    sleep(1)
            el45 = self.driver.find_element_by_xpath("//span[contains(text(),'团队共')]/../..")
            ActionChains(self.driver).move_to_element(el45).perform()
            # self.driver.find_element_by_xpath("//div[contains(@class,'SearchFileContentPanel_toolButton')]/i[@class='anticon']").click()
            self.driver.find_element_by_xpath(
                "//span[contains(text(),'团队共')]/../../../../../../../h4//i[@class='anticon']/..").click()
            print_name = "边写边搜列表收藏"
            version = "以新版本覆盖"
            com_alert().com_equal(self.driver, self.picturePath, print_name, version)
            sleep(1)
            el51 = self.driver.find_element_by_xpath("//span[contains(text(),'团队共')]/../..")
            ActionChains(self.driver).move_to_element(el51).perform()
            self.driver.find_element_by_xpath(
                "//span[contains(text(),'团队共')]/../../../../../../../h4//i[@class='anticon anticon-arrows-alt']/..").click()
            try:
                WebDriverWait(self.driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, "//div[text()='边写边搜']")))
                el46 = self.driver.find_elements_by_xpath("//i[@class='anticon anticon-more']")
                ActionChains(self.driver).move_to_element(el46[1]).perform()
                self.driver.find_element_by_xpath("//li[text()='收藏到私有']").click()
                print_name="边写边搜双屏收藏"
                com_alert().com_equal(self.driver, self.picturePath, print_name, version)
                self.driver.find_element_by_xpath("//i[@class='anticon anticon-shrink']").click()
                sleep(1)
                self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
            except Exception as e:
                print(e)
                print("双屏展开校验超时")
        except Exception as e:
            print(e)
            print("未从文件夹内搜索中打开编辑")





if __name__ == "__main__":
    testUnite = unittest.TestSuite()
    testUnite.addTest(test_store("test_viewStore"))
    testUnite.addTest(test_store("test_listStore"))
    testUnite.addTest(test_store("test_folderSearchStore"))
    testUnite.addTest(test_store("test_modifyStore"))

    fp = open(resultpath + "收藏验证.html", "wb")
    runner = HTMLTestRunner(stream=fp, title="收藏功能测试报告", description="预览，列表、搜索、边写边搜验证收藏")
    runner.run(testUnite)
    fp.close()



