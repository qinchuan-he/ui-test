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

# 上传office相关文件
class up_office(unittest.TestCase):
    '''上传office相关文件'''
    mode=2
    driver = execBrower(mode)
    user().login(driver)
        # # 私有根目录新建文件夹
    el1=driver.find_element_by_xpath("//span[text()='新建']")
    sleep(3)
    ActionChains(driver).move_to_element(el1).perform()
    driver.find_element_by_xpath("//li[text()='新建文件夹']").click()
    folder1=int(time.time())
    print("新建文件夹：%s " %folder1)
    driver.switch_to.active_element.send_keys(folder1)
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    # 进入文件夹
    driver.find_element_by_xpath("//span[text()="+str(folder1)+"]").click()


    def upload_office(self):
        '''上传office文件'''
        # 公共参数
        picturePath="C:\\work\\1测试\\10自动化\\截图保存\\19种上传格式截图\\picture\\"
        showPath="file:///C:/work/1测试/10自动化/截图保存/19种上传格式截图/picture/"

        waitTime=5
        uploadwait= 15 #上传之后的等待时间

        # 上传文件
        # 图片相关

        tpath = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\图片\\"
        jpgname = "timg"
        pngname= "验证图片"
        bmpname = "BMP图片"


        # 新建图片文件夹，并进入
        el1=self.driver.find_element_by_xpath("//span[text()='新建']")
        sleep(waitTime)
        ActionChains(self.driver).move_to_element(el1).perform()
        self.driver.find_element_by_xpath("//li[text()='新建文件夹']").click()
        picture = "图片"

        self.driver.switch_to.active_element.send_keys(picture)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        print("创建picture分类文件夹成功： %s" %picture)
        sleep(1)
        self.driver.find_element_by_xpath("//span[text()="+"'"+picture+"'"+"]").click()
        # 上传office文件
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(tpath+jpgname+".jpg")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(tpath+pngname+".png")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(tpath+bmpname+".bmp")

        sleep(10)
        # 截图并输出
        date1=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date1+".png")
        comHtml().print_html(jpgname, picturePath, date1)  # 输出到html报告

        # 预览文件
        #点击
        self.driver.find_element_by_xpath("//span[text()=\'"+jpgname+"\']/..").click()
        # 等待加载，准备截图
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'PreviewContent_imgViewer')]")))
        # 增加一个点击图片的操作
        self.driver.find_element_by_xpath("//div[@id='J_viewer']/img").click()
        sleep(1)
        date2=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date2+".png")
        comHtml().print_html(jpgname, picturePath, date2)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 5, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'PreviewContent_imgViewer')]")))

        # 预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+pngname+"\']/..").click()
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'PreviewContent_imgViewer')]")))
        sleep(1)
        date3=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date3+".png")
        comHtml().print_html(pngname, picturePath, date3)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 5, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'PreviewContent_imgViewer')]")))

        #预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+bmpname+"\']/..").click()
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'PreviewContent_imgViewer')]")))
        sleep(1)
        date4=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date4+".png")
        comHtml().print_html(bmpname, picturePath, date4)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 5, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'PreviewContent_imgViewer')]")))



        # 返回到格式集合目录
        self.driver.find_element_by_xpath("//a[text()=\'"+self.folder1+"\']")
        # self.driver.quit()

if __name__ == "__main__":
    testunite = unittest.TestSuite()
    testunite.addTest(up_office("upload_office"))

    # 生成报告
    fp = open(resultpath+'up_office.html','wb')
    runner = HTMLTestRunner(stream=fp, title='upoffice', description='执行情况：')
    runner.run(testunite)
    fp.close()
































