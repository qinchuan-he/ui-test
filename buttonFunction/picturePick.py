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

#  验证图例表格提取和同句搜索，图例提取有三个操作（数据组），新增，更新，复制
# 1.新建word，插入图片，然后文件夹内搜索word，（第一步更新验证）----新建word用例中
# 2.文件夹内搜索中分享word，刷新文件夹内搜索（第二步复制验证）----新建word用例中
# 3.团队中上传word，并且打开预览（第三步新增验证）,并且验证同句搜索
# 4.团队中上传word（纯矢量图），并且打开预览（验证矢量图的提取）
# 5.团队中上传PDF，并且打开预览（验证PDF图片的提取）,并且验证同句搜索

class test_Pick(unittest.TestCase):
    '''图例表格提取验证和同句验证'''
    #  公共参数
    picturePath = "C:\\work\\1测试\\10自动化\\截图保存\\图例\\"  # 生成截图路径
    uploadPath = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\图例提取文件\\"  # 上传路径
    wordTextName = "表格图片"   # 后缀是doc
    wordOcrName = "纯矢量图"   # 后缀是docx
    pdfName = "图例验证文件"  # 后缀是pdf
    texturl = uploadPath+wordTextName+".doc"
    ocrurl = uploadPath+wordOcrName+".docx"
    pdfurl = uploadPath+pdfName+".pdf"
    folder = str(time.time())

    # 启动浏览器并登陆
    mode = 2
    driver = execBrower(mode)
    user().login(driver)
    team_name = team().check_team(driver)

    #  上传文件并预览
    def test_textPick(self):
        '''测试非矢量图的提取'''
        button = "upload"
        el11 = com_xpath().com_listButton(self.driver, button)
        el11.send_keys(self.texturl)
        version = "以新版本覆盖"
        print_name = "图例上传文件"
        com_alert().com_equal(self.driver, self.picturePath, print_name, version)
        try:
            WebDriverWait(self.driver, 20, 0.5).until(ec.element_to_be_clickable((By.XPATH, "//span[text()='"+self.wordTextName+"']/..")))
            self.driver.find_element_by_xpath("//span[text()='"+self.wordTextName+"']/..").click()
            try:
                WebDriverWait(self.driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
                # 查看图例
                self.driver.find_element_by_xpath("//div[contains(@class,'PreviewContent_imgButton')]").click()
                sleep(0.5)
                el12 = self.driver.find_element_by_xpath("//div[contains(@class,'https//testjianyuan.fir.ai')]")
                ActionChains(self.driver).move_to_element(el12)
                self.driver.find_element_by_xpath("//div[contains(@class,'FileImages_imageAction')]/div")
                name = "预览加入碎片"
                print_name = "预览图例加入碎片"
                com_alert().com_addFrager()



            except Exception as e:
                print(e)
                printName = "异常截图2"
                datename12 = str(int(time.time()))
                self.driver.get_screenshot_as_file(self.picturePath + datename12 + ".png")
                comHtml().print_html(printName, self.picturePath, datename12)

        except Exception as e:
            print(e)
            print("上传出现异常")
            printName = "异常截图1"
            datename12 = str(int(time.time()))
            self.driver.get_screenshot_as_file(self.picturePath+datename12+".png")
            comHtml().print_html(printName, self.picturePath, datename12)








