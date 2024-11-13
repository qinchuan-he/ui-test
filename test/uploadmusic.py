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
from common.comfunction import OpenBrowser
from common.comfunction import User
from common.comfunction import comHtml
from common.comfunction import com_path

resultpath = os.path.join(com_path(),"报告")

# 上传office相关文件
class up_music(unittest.TestCase):
    '''上传music相关文件'''
    mode=1
    driver = OpenBrowser(mode)
    User().login(driver)
            # # 私有资料根目录文件夹
    el1=driver.find_element_by_xpath("//span[text()='新建']")
    sleep(3)
    ActionChains(driver).move_to_element(el1).perform()
    driver.find_element_by_xpath("//li[text()='文件夹']").click()
    folder1=int(time.time())
    print("文件夹：%s " %folder1)
    driver.switch_to.active_element.send_keys(folder1)
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    # 进入文件夹
    driver.find_element_by_xpath("//span[text()="+str(folder1)+"]").click()

    def upload_music(self):
        '''上传music文件'''
        # 公共参数
        picturePath = com_path()+"截图\\"+"19种上传格式截图\\music\\"
        if not (os.path.exists(picturePath)):
            os.makedirs(picturePath)
        showPath="file:///C:/work/1测试/10自动化/截图保存/19种上传格式截图/music/"
        waitTime=5
        uploadwait= 15 #上传之后的等待时间

        # 上传文件
        # 音频
        ypath = com_path()+"19种格式\\音频\\"
        pamname = "16k"
        wavname = "m4a"
        amrname = "另一种格式"
        mp3name = "群星 - 贾谊《过秦论》"
        m4aname = "电话会议兴业证券"

        # 新建音频文件夹，并进入
        el1=self.driver.find_element_by_xpath("//span[text()='新建']")
        sleep(waitTime)
        ActionChains(self.driver).move_to_element(el1).perform()
        self.driver.find_element_by_xpath("//li[text()='文件夹']").click()
        musicfolder = "音频"

        self.driver.switch_to.active_element.send_keys(musicfolder)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        print("创建music分类文件夹成功： %s" %musicfolder)
        sleep(1)
        self.driver.find_element_by_xpath("//span[text()="+"'"+musicfolder+"'"+"]").click()
        # 上传office文件
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(ypath+pamname+".pcm")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(ypath+wavname+".wav")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(ypath+amrname+".amr")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(ypath+mp3name+".mp3")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(ypath+m4aname+".m4a")
        sleep(30)
        # 截图并输出
        date1=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date1+".png")
        comHtml().print_html("音频文件列表", picturePath, date1)  # 输出到html报告

        # 预览文件
        #点击
        self.driver.find_element_by_xpath("//span[text()=\'"+pamname+"\']/..").click()
        sleep(waitTime)
        date2=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date2+".png")
        comHtml().print_html(pamname, picturePath, date2)  # 输出到html报告

        # 预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+wavname+"\']/..").click()
        sleep(waitTime)
        date3=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date3+".png")
        comHtml().print_html(wavname, picturePath, date3)  # 输出到html报告

        #预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+amrname+"\']/..").click()
        sleep(waitTime)
        date4=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date4+".png")
        comHtml().print_html(amrname, picturePath, date4)  # 输出到html报告

        # 预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+mp3name+"\']/..").click()
        sleep(waitTime)
        date5=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date5+".png")
        comHtml().print_html(mp3name, picturePath, date5)  # 输出到html报告

        # 预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+m4aname+"\']/..").click()
        sleep(waitTime)
        date6=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date6+".png")
        comHtml().print_html(m4aname, picturePath, date6)  # 输出到html报告
        # self.driver.quit()
        # 返回到格式集合目录
        self.driver.find_element_by_xpath("//a[text()=\'"+str(self.folder1)+"\']").click()
        

if __name__ == "__main__":
    testunite = unittest.TestSuite()
    testunite.addTest(up_music("upload_music"))

    # 生成报告
    fp = open(resultpath+'up_music.html','wb')
    runner = HTMLTestRunner(stream=fp, title='upoffice', description='执行情况：')
    runner.run(testunite)
    fp.close()
































