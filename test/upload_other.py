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
from common.comfunction import execBrower
from common.comfunction import user
from common.comfunction import comHtml

resultpath = "C:\\work\\1测试\\10自动化\\报告\\"

# 上传其他相关文件
class up_other(unittest.TestCase):
    '''上传office相关文件'''

    mode=2
    driver = execBrower(mode)
    user().login(driver)
    waitTime = 5


            # 私有根目录文件夹
    el1=driver.find_element_by_xpath("//span[text()='新建']")
    sleep(waitTime)
    ActionChains(driver).move_to_element(el1).perform()
    driver.find_element_by_xpath("//li[text()='文件夹']").click()
    folder1=int(time.time())
    print("文件夹：%s " %folder1)
    driver.switch_to.active_element.send_keys(folder1)
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    # 进入文件夹
    driver.find_element_by_xpath("//span[text()="+str(folder1)+"]").click()


    def upload_other(self):
        '''上传其他文件'''

        # 公共参数
        picturePath="C:\\work\\1测试\\10自动化\\截图保存\\19种上传格式截图\\other\\"
        showPath="file:///C:/work/1测试/10自动化/截图保存/19种上传格式截图/other/"

        waitTime=5
        uploadwait= 15 #上传之后的等待时间

        # 上传文件
        # 其他
        qpath="C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\其他\\"
        pdfname = "146页年度报告"
        zipname = "测试解压"
        hmtlname = "厦门亿联网络技术股份有限公司 关于召开 2018 年年度股东大会的通知"
        rarname = "上传文件"
        txtname = "天空1"

        
        # 新建office文件夹，并进入
        el1=self.driver.find_element_by_xpath("//span[text()='新建']")
        sleep(waitTime)
        ActionChains(self.driver).move_to_element(el1).perform()
        self.driver.find_element_by_xpath("//li[text()='文件夹']").click()
        other = "其他"

        self.driver.switch_to.active_element.send_keys(other)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        print("创建office分类文件夹成功： %s" %other)
        sleep(1)
        self.driver.find_element_by_xpath("//span[text()="+"'"+other+"'"+"]").click()
        # 上传office文件
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(qpath+pdfname+".PDF")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(qpath+zipname+".zip")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(qpath+hmtlname+".html")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(qpath+rarname+".rar")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(qpath+txtname+".txt")
        sleep(30)
        # 截图并输出
        date1=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date1+".png")
        comHtml().print_html("其他类型列表", picturePath, date1)  # 输出到html报告

        # 预览文件
        #点击
        self.driver.find_element_by_xpath("//span[text()=\'"+pdfname+"\']/..").click()
        # 等待加载，准备截图
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
        sleep(10)
        date2=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date2+".png")
        comHtml().print_html(pdfname, picturePath, date2)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 5, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//iframe")))

        #预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+hmtlname+"\']/..").click()
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
        sleep(3)
        date4=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date4+".png")
        comHtml().print_html(hmtlname, picturePath, date4)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 5, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//iframe")))

        # 预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+txtname+"\']/..").click()
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
        sleep(5)
        date6=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date6+".png")
        comHtml().print_html(txtname, picturePath, date6)  # 输出到html报告
        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 5, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//iframe")))

        # 预览下一个,处理压缩包
        self.driver.find_element_by_xpath("//div/span[text()=\'"+zipname+"\']/..").click()
        sleep(1)
        date3=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date3+".png")
        comHtml().print_html(zipname, picturePath, date3)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'取 消')]/..").click()

        # self.driver.refresh()
        sleep(1)
        # 预览下一个,处理压缩包
        self.driver.find_element_by_xpath("//div/span[text()=\'"+rarname+"\']/..").click()

        sleep(1)
        date5=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date5+".png")
        comHtml().print_html(rarname, picturePath, date5)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'取 消')]/..").click()
        sleep(1)
        # 返回到格式集合目录
        self.driver.find_element_by_xpath("//a[text()=\'"+str(self.folder1)+"\']").click()
        # self.driver.quit()

if __name__ == "__main__":
    testunite = unittest.TestSuite()
    testunite.addTest(up_other("upload_other"))

    # 生成报告
    fp = open(resultpath+'up_other.html','wb')
    runner = HTMLTestRunner(stream=fp, title='upoffice', description='执行情况：')
    runner.run(testunite)
    fp.close()
































