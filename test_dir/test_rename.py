# coding=utf-8
# import io
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# 报告
import pytest
# import unittest
# from HTMLTestRunner import HTMLTestRunner
from time import sleep
import time  # 生成时间戳用
# import os  # 上传autoit用
import sys
# import re  # 正则提取

# # """解决vscode中不能引用别的模块的问题"""
# import os
# #
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
#
# # print(sys.path)
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 引入公共方法
from common.newcomfunction import new_user
from common.comfunction import User
from common.comfunction import com_xpath
from common.comfunction import com_path
# from common.comfunction import team

# 2019/09/30
# 本次验证团队文件夹的重命名，是否更新时间和名字,成员新建，另外成员文件夹内上传，成员再修改名字
# 目前实现私有文件夹的重命名
#
# mode = 2
url = os.path.join(com_path(),"19种格式","图例提取文件","doc验证解析.doc") # 上传路径
file_name = "doc验证解析"
class Test_Rename:
    '''私有中重命名文件夹和文件'''
    def test_private(self, browser, base_url, images_path):
        """ 私有中重命名文件夹和文件"""
        print("base_url:" + base_url)
        new_user().new_login(browser, base_url)
        driver = browser
        folder = str(time.time())
        User().createFolder(driver, folder)
        sleep(0.5)
        driver.find_element_by_xpath("//span[text()='"+folder+"']").click()
        folder2 = str(time.time())
        User().createFolder(driver,folder2)
        sleep(0.5)
        # 上传文件
        com_xpath().com_localupload(driver,url)
        # 重命名文件夹
        el1 = driver.find_element_by_xpath("//span[text()='"+ folder2 +"']")
        ActionChains(driver).move_to_element(el1).perform()
        sleep(0.3)
        el2 = com_xpath().com_listmoreActions(driver,folder2)
        el2.click()
        sleep(0.5)
        # el3 = com_xpath().com_listmoreButton(driver,'重命名')
        # el3.click()
        com_xpath().com_listmoreButton(driver, '重命名')
        sleep(0.5)
        name = "重命名了.哈哈.后缀"
        com_xpath().com_listrename(driver,name)
        # 重命名截图
        driver.get_screenshot_as_file(os.path.join(images_path,"test_private-重命名文件夹截图",str(time.time()) + ".png"))
        sleep(5) # 等待上传
        driver.refresh()
        # 重命名文件
        el21 = driver.find_element_by_xpath("//span[text()='"+file_name+"']")
        ActionChains(driver).move_to_element(el21).perform()
        sleep(0.4)
        # el22 = com_xpath().com_listmoreActions(driver,file_name)
        # el22.click()
        com_xpath().com_listmoreActions(driver, file_name)
        sleep(0.5)
        # el23 = com_xpath().com_listmoreButton(driver,'重命名')
        # el23.click()
        com_xpath().com_listmoreButton(driver, '重命名')
        sleep(0.5)
        newname = "这个文件重命名了.cc.end"
        com_xpath().com_listrename(driver,newname)
        # 重命名截图
        driver.get_screenshot_as_file(os.path.join(images_path,"test_private-重命名文件截图",str(time.time()) + ".png"))
        sleep(1)


#
# if __name__ == '__main__':
#     pytest.main(["-sv", "test_rename.py"])






















