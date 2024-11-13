# coding=utf-8
import io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
import sys
import re  # 正则提取

"""解决vscode中不能引用别的模块的问题"""
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

# 引入公共方法
from common.newcomfunction import new_user
from common.comfunction import com_path

# 验证智能比对模块，这里不验证比对结果，其他用例查看
# 公共参数
upload_path1 = com_path()+"19种格式\比对文件\\合同1.docx"
upload_path2 = com_path()+"19种格式\比对文件\\合同1扫描件（8张合并）.pdf"
name1 = "合同1"
name2 = "合同1扫描件（8张合并）"

class TestContractCompare:
    ''' 合同防伪模块'''

    def test_one(self, browser, base_url, images_path):
        ''' 智能比对'''
        print("base_url:"+base_url)
        new_user().new_login(browser, base_url)
        driver = browser
        # 进入模块
        driver.find_element_by_xpath("//a[text()='智能比对']").click()
        uploads = driver.find_elements_by_xpath("//input[@type='file']")
        uploads[0].send_keys(upload_path1)
        uploads[1].send_keys(upload_path2)
        try:
            WebDriverWait(driver, 5, 0.5).until(ec.element_to_be_clickable((By.XPATH, "//span[text()='开始比对']/..")))
            driver.find_element_by_xpath("//span[text()='开始比对']/..").click()
            sleep(2)
            driver.get_screenshot_as_file(images_path+"test_one-比对之后截图"+str(time.time())+".png")
            # 预览文件
            driver.find_element_by_xpath("//span[text()='"+name1+"']").click()
            try:
                WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
                sleep(5) # 加载时间
                driver.get_screenshot_as_file(images_path+"test_one-预览word"+str(time.time())+".png")
                # 预览纯文本，存在的话
                try:
                    WebDriverWait(driver, 3, 0.5)\
                        .until(ec.element_to_be_clickable((By.XPATH, "//span[text()='纯文本']/..")))
                    driver.find_element_by_xpath("//span[text()='纯文本']/..").click()
                    sleep(0.5)
                    driver.get_screenshot_as_file(images_path+"test_one-预览纯文本"+str(time.time())+".png")
                except Exception as e:
                    print(e)
                driver.back()
                sleep(0.5)
                # 预览另一个文件
                driver.find_element_by_xpath("//span[text()='"+name2+"']").click()
                try:
                    WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
                    sleep(3)
                    driver.get_screenshot_as_file(images_path+"test_one-预览pdf"+str(time.time())+".png")
                    driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
                    sleep(1)
                    driver.get_screenshot_as_file(images_path+"test_one-预览返回"+str(time.time())+".png")
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
