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
folder = '哇哈哈' #  文件夹名字

# 启动浏览器
mode = 2
driver = execBrower(mode)
User().login(driver)
driver.implicitly_wait(5)
driver.find_element_by_xpath("//span[text()='哇哈哈']/..").click()
#  上传文件
version = "以新版本覆盖"
print_name = "比对上传文件"
uploadWordUrl = uploadPath + wordname1 + ".docx"
uploadPdfUrl1 = uploadPath + pdfname1 + ".pdf"
uploadPdfUrl2 = uploadPath + pdfname2 + ".pdf"
uploadPdfUrl3 = uploadPath + pdfname3 + ".PDF"
uploadPdfUrl4 = uploadPath + pdfname4 + ".pdf"
date = time.time()
print(date)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date)))
i = 0
# sleep(14)
# sleep(2)
com_xpath().com_preview(driver, pdfname1)
# 衔接TXT文档的位置
sleep(1)

buttont = "compare"
# buttont = 'cover'
el21 = com_xpath().com_previewButton(driver, buttont)
el21.click()
printName = "开始比对"
# driver.switch_to.frame('J_iframe')
# sleep(0.5)
#
# try:
#     driver.find_element_by_xpath("//span[@class='ant-tree-switcher ant-tree-switcher_close']/..").click()
# except Exception as e:
#     print(e)
driver.switch_to.default_content()
sleep(3)
driver.find_element_by_xpath("//span[@class='ant-modal-close-x']/..").send_keys(Keys.ENTER)
sleep(0.5)
el21 = com_xpath().com_previewButton(driver, buttont)
el21.click()
# driver.find_element_by_xpath("//span[@class='ant-tree-switcher ant-tree-switcher_close']/..").click()

# driver.find_element_by_xpath("//button[@class='ant-modal-close']").click()
sleep(1)
# tag = driver.find_element_by_xpath("//span[text()='1569236875']/../../..")
# driver.execute_script("arguments[0].scrollIntoView();", tag)
# driver.switch_to.active_element.send_Keys(Keys.ENTER)
driver.find_element_by_xpath("//span[text()='1569236875']").send_keys(Keys.ENTER)


# # el3 = driver.find_element_by_xpath("//span[text()='1569236875']/../../..")
# # ActionChains(driver).click_and_hold(el3).perform()
# driver.find_element_by_xpath("//span[text()='1569236875']/../../..").click()
# driver.find_element_by_xpath("//span[text()='1569236875']/../../..").send_keys(Keys.ENTER)
# driver.find_element_by_xpath("//button[@class='ant-btn']").click()
# driver.find_element_by_xpath("//span[@class='ant-modal-close-x']/..").send_keys(Keys.ENTER)


# js1 = "document.getElementsByClassName('ant-tree-treenode-switcher-close')[1].click()"
# driver.execute_script(js1)
# sleep(6)
# driver.quit()






# txt文档备份
# com_xpath().com_preview(driver, '天空1')
# driver.find_element_by_xpath("//span[text()='编辑文档']/..").click()
# sleep(3)
# buttont = "compare"
# sleep(5)
# el21 = com_xpath().com_previewButton(driver, buttont)
# el21.click()
# printName = "开始比对"
#
# sleep(0.5)
# print(driver.switch_to.active_element)
# sleep(1)
# driver.find_element_by_xpath("//span[text()='哇哈哈']/../../..").click()









