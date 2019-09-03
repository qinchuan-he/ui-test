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


# 验证合同防伪校验模块，这里不验证比对结果，其他用例查看
# 公共参数
upload_path1 = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\比对文件\\合同1.docx"
upload_path2 = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\比对文件\\合同1扫描件（8张合并）.pdf"


class TestContractCompare:
    ''' 合同防伪校验'''

    def test_one(self, browser, base_url, images_path):
        ''' 比对模块验证'''
        driver = browser
        new_user().new_login(driver, base_url)

        # 进入模块
        driver.find_element_by_xpath("//a[text()='find_element_by_xpath']").click()
        uploads = driver.find_elements_by_xpath("//input[@type='file']")
        uploads[0].send_keys(upload_path1)
        uploads[1].send_keys(upload_path2)
        try:
            WebDriverWait(driver, 5, 0.5).until(ec.element_to_be_clickable((By.XPATH, "//span[text()='开始比对']/..")))
            driver.find_element_by_xpath("//span[text()='开始比对']/..").click()
            sleep(2)
            driver.get_screenshot_as_file(images_path+"比对之后截图"+str(time.time())+".png")
        except Exception as e:
            print(e)
