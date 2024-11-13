# coding=utf-8
# import io
# from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# 报告
import pytest
import os
# import unittest
# from HTMLTestRunner import HTMLTestRunner
from time import sleep
import time  # 生成时间戳用
# import os  # 上传autoit用
import sys
# import re  # 正则提取

# """解决vscode中不能引用别的模块的问题"""
# import os
#
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
#
# # print(sys.path)
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 引入公共方法
from common.newcomfunction import new_user
from common.comfunction import User
# from common.comfunction import com_xpath
from common.comfunction import com_path
# from common.comfunction import team
from common.comfunction import com_operation

# 2019/11/11
# 尝试见远编辑器的验证，新建word文档
#
#
# mode = 2
url  = com_path()+"19种格式\\图例提取文件\\doc验证解析.doc"    # 上传路径
file_name = "doc验证解析"
class Test_createword:
    '''私有中新建远文档'''
    def test_word(self, browser, base_url, images_path):
        """ 私有中新建远文档"""
        print("base_url:" + base_url)
        new_user().new_login(browser,base_url)
        driver = browser
        folder = str(time.time())
        User().createFolder(driver,folder)
        driver.find_element_by_xpath("//span[text()='"+folder+"']").click()
        User().create_file(driver,file_type="见远文档(.docx)")
        sleep(10)
        el1 = driver.find_element_by_xpath("//iframe")
        driver.switch_to.frame(el1)
        WebDriverWait(driver,20,0.5).until(ec.presence_of_element_located((By.XPATH,"//canvas[@id='id_target_cursor']")))
        sleep(15)
        el2 = driver.find_element_by_xpath("//canvas[@id='id_target_cursor']")
        ActionChains(driver).move_to_element(el2).send_keys("本王编辑的内容，重要的内容").perform()
        ActionChains(driver).move_to_element(el2).send_keys(Keys.ENTER).perform()
        ActionChains(driver).move_to_element(el2).send_keys("现对你公司推荐的杭州福膜新材料科技股份有限"
                                                            "公司（以下简称）首发申请文件提出反"
                                                            "馈意见，请你公司在30日内对下列问题逐项落实并提供书面回复和"
                                                            "电子文档。若涉及对招股说明书的修改，请以楷体加粗标明。我会"
                                                            "收到你公司的回复后，将根据情况决定是否再次向你公司发出"
                                                            "反馈意见。如在30日内不能提供书面回复，请向我会提交延期"
                                                            "回复的申请。若对本反馈意见有任何问"
                                                            "题，请致电我会审核人员。").perform()
        sleep(0.5)
        driver.get_screenshot_as_file( os.path.join(images_path,"test_word-编辑了内容",str(time.time()) + ".png"))
        driver.switch_to.default_content()
        sleep(0.5)
        com_operation().com_close_preview(driver)
        sleep(1)




# if __name__ == '__main__':
#     pytest.main(["-sv", "test_private_createword.py"])






















