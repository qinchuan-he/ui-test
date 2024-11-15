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
from common.comfunction import com_share  #  分享类公共方法
from common.comfunction import com_path


resultPath = com_path()+"报告\\"
# 验证比对功能，比对分为纯文本和图片两种比对
class test_compare(unittest.TestCase):
    '''测试比对'''
    #  公共参数
    picturePath = com_path()+"截图\\"+"19种上传格式截图\\other\\"  # 生成截图路径
    if not (os.path.exists(picturePath)):
        os.makedirs(picturePath)
    uploadPath = com_path()+"19种格式\\比对文件\\" #  上传路径
    wordname1 = "合同1"
    pdfname1 = "合同"
    pdfname2 = "合同1扫描件（8张合并）"
    pdfname3 = "36页"  # 后缀是大写的PDF
    pdfname4 = "30页图片"
    folder = str(time.time()) #  文件夹名字

    # 启动浏览器
    mode = 1
    driver = OpenBrowser(mode)
    User().login(driver)
    driver.implicitly_wait(45)
    # 检查团队
    team_name = team().check_team(driver)
    driver.find_element_by_xpath("//div[contains(@class,'GlobalHeader_logo')]").click()
    sleep(0.5)
    driver.find_element_by_xpath("//a[text()='私有资料']").click()
    driver.switch_to_alert().accept()
    #  文件夹，存放比对文件
    User().createFolder(driver, folder)
    # 进入文件夹
    driver.find_element_by_xpath("//span[text()='"+folder+"']/..").click()
    #  上传文件
    version = "以新版本覆盖"
    print_name = "比对上传文件"
    uploadWordUrl = uploadPath + wordname1 + ".docx"
    uploadPdfUrl1 = uploadPath + pdfname1 + ".pdf"
    uploadPdfUrl2 = uploadPath + pdfname2 + ".pdf"
    uploadPdfUrl3 = uploadPath + pdfname3 + ".PDF"
    uploadPdfUrl4 = uploadPath + pdfname4 + ".pdf"
    driver.find_element_by_xpath("//input[@type='file']").send_keys(uploadWordUrl)
    driver.find_element_by_xpath("//input[@type='file']").send_keys(uploadPdfUrl1)
    driver.find_element_by_xpath("//input[@type='file']").send_keys(uploadPdfUrl2)
    # driver.find_element_by_xpath("//input[@type='file']").send_keys(uploadPdfUrl3)
    # driver.find_element_by_xpath("//input[@type='file']").send_keys(uploadPdfUrl4)
    #  上传等待时间,比对不要看解析，速度加快2019/09/24
    # print('开始时间：'+ time.strftime('%Y-%m-%d %H:%M:S', time.localtime(time.time())))
    for i in range(1):
        sleep(3)
        com_alert().com_equal(driver, version="保留两者")
    # # sleep(14)
    # sleep(4)


    #  比对纯文字型文件
    def test_text(self):
        '''纯文字的word和PDF比对'''
        try:
            com_xpath().com_preview(self.driver, self.pdfname1)
            buttont = "compare"
            el21 = com_xpath().com_previewButton(self.driver, buttont)
            el21.click()
            printName = "开始比对"
            com_alert().com_alertCompare(self.driver, self.folder, self.wordname1, self.picturePath, printName)
            datename = str(int(time.time()))
            self.driver.get_screenshot_as_file(self.picturePath+datename+".png")
            # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            printName = "比对结果"
            comHtml().print_html(printName, self.picturePath, datename)
            #  生成报告
            self.driver.find_element_by_xpath("//span[text()='生成报告']/..").click()
            try:
                WebDriverWait(self.driver, 15, 0.5).until(ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'ComparisonReportHeader_comHeaderTitle')]")))
                # 比对报告截图
                datename2 = str(int(time.time()))
                printName = "比对报告"
                self.driver.get_screenshot_as_file(self.picturePath+datename2+".png")
                comHtml().print_html(printName, self.picturePath, datename2)
                #  返回
                self.driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-sm']").click()
                sleep(0.5)

            except Exception as e:
                print(e)
                print("比对报告超时")
            #  退出比对结果
            self.driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-sm']").click()
            sleep(0.5)
            #  退出预览
            self.driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-sm']").click()
        except Exception as e:
            comHtml().screen_shot(self.driver, self.picturePath, print_name="上传出现异常")
        sleep(3)

    #  含有ocr的比对报告
    def test_ocr(self):
        '''和扫描件比对'''
        com_xpath().com_preview(self.driver, self.pdfname1)
        buttont = "compare"
        el21 = com_xpath().com_previewButton(self.driver, buttont)
        el21.click()
        printName = "开始比对"
        com_alert().com_alertCompare(self.driver, self.folder, self.pdfname2, self.picturePath, printName)
        datename = str(int(time.time()))
        self.driver.get_screenshot_as_file(self.picturePath + datename + ".png")
        printName = "比对结果"
        comHtml().print_html(printName, self.picturePath, datename)
        #  生成报告
        self.driver.find_element_by_xpath("//span[text()='生成报告']/..").click()
        try:
            WebDriverWait(self.driver, 15, 0.5).until(ec.presence_of_element_located(
                (By.XPATH, "//div[contains(@class,'ComparisonReportHeader_comHeaderTitle')]")))
            # 比对报告截图
            datename2 = str(int(time.time()))
            printName = "比对报告"
            self.driver.get_screenshot_as_file(self.picturePath + datename2 + ".png")
            comHtml().print_html(printName, self.picturePath, datename2)
            # 下载
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-download']/..").click()
            sleep(0.5)
            datename21 = str(int(time.time()))
            print_name = "下载报告"
            self.driver.get_screenshot_as_file(self.picturePath+datename21+".png")
            comHtml().print_html(print_name, self.picturePath, datename21)
            sleep(1)

            #  收藏
            self.driver.find_element_by_xpath("//i[@class='anticon']/..").click()
            sleep(0.5)
            print_name = "比对报告收藏"
            version = "以新版本覆盖"
            com_alert().com_equal(self.driver, self.picturePath, print_name, version)
            # 验证功能，再次收藏
            sleep(1)
            self.driver.find_element_by_xpath("//i[@class='anticon']/..").click()
            sleep(0.5)
            print_name = "比对报告收藏"
            version = "以新版本覆盖"
            com_alert().com_equal(self.driver, self.picturePath, print_name, version)
            # 分享
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-share-alt']/..").click()
            sleep(0.5)
            print_name = "比对报告分享"
            version = "以新版本覆盖"
            # com_alert().com_equal(self.driver, self.picturePath, print_name, version)
            com_share(self.team_name, version, print_name, self.picturePath, self.driver)
            # 验证再次分享功能
            sleep(1)
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-share-alt']/..").click()
            sleep(0.5)
            print_name = "比对报告分享"
            version = "以新版本覆盖"
            # com_alert().com_equal(self.driver, self.picturePath, print_name, version)
            com_share(self.team_name, version, print_name, self.picturePath, self.driver)

            sleep(2)
            #  返回
            self.driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-sm']").click()
            sleep(0.5)

        except Exception as e:
            print(e)
            print("比对报告超时")
        #  退出比对结果
        self.driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-sm']").click()
        sleep(8)  # 等待下载完毕
        #  退出预览
        self.driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-sm']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




if __name__ == "__main__":
    testCase = unittest.TestSuite()
    testCase.addTest(test_compare("test_text"))
    testCase.addTest(test_compare("test_ocr"))

    fp = open(resultPath+"比对验证.html", "wb")
    runner = HTMLTestRunner(stream=fp, title="比对测试结果", description="纯文本和ocr的验证")
    runner.run(testCase)
    fp.close()









































