# coding=utf-8
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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

# 引入公共方法
from common.newcomfunction import new_user
from common.comfunction import User
from common.comfunction import com_xpath
from common.comfunction import com_path
# from common.comfunction import team

class Test_loading:
    """验证加载"""
    path = "D://loadingReport//"
    switch_path = "D://loadingReport//switch//"
    suffix=".txt"
    # def test_previewLoading(self, browser, base_url, images_path):
    def test_previewLoading(self, driver, filename):  # 对参数进行了改造
        """ 预览加载时间统计 """
        # new_user().new_login(browser, base_url)
        # driver = browser
        driver.find_element_by_xpath("//span[text()='1112']").click()
        sleep(1)
        driver.find_element_by_xpath("//span[text()='"+filename+"']").click()
        sleep(3)
        driver.find_element_by_xpath("//span[text()='内容搜索']/..").click()
        date1 = time.time()
        date2 = date1
        print("开始记录时间：%s" % date1)
        sleep(1)
        iframe = driver.find_element_by_xpath("//iframe")
        driver.switch_to.frame(iframe)
        for i in range(1000):
            try:
                count2 = driver.find_element_by_xpath("//span[@id='total_page']").text
                # print(count2)
                if int(count2) > 1:
                    date2 = time.time()
                    break
            except Exception as e:
                pass
            sleep(0.1)
        print("加载完成时间: %s"% date2)
        print("从只读模式进入耗时：%.2f 秒"%(date2-date1))
        s ='%.2f'%(date2-date1)
        f = open("D://1.txt","a")
        f.write("\r\n"+filename+"----只读模式进入加载耗时"+str(s)+"秒")
        f.close()
        file = open(self.path+filename+self.suffix,'a')
        file.write("\r\n"+str(s))
        file.close()
        driver.switch_to.default_content()

    # 从纯文本中切换到原格式
    # def test_switchHtml(self,browser,key):
    def test_switchHtml(self, driver,filename): # 调用改造参数
        """内容搜索中切换格式"""
        # 切换到纯文本
        sleep(0.5)
        # driver = browser
        driver.find_element_by_xpath("//span[text()='纯文本']/..").click()
        sleep(1)
        driver.find_element_by_xpath("//span[text()='原格式']/..").click()
        date3 = time.time()
        print("原格式点击时间 %s" %date3 )
        date4 = date3
        iframe2 = driver.find_element_by_xpath("//iframe")
        driver.switch_to.frame(iframe2)
        for i1 in range(1000):
            try:
                count3 = driver.find_element_by_xpath("//span[@id='total_page']").text
                if int(count3) > 1:
                    date4 = time.time()
                    print("加载完成时间：%s"%date4)
                    break
            except Exception as e:
                pass
            sleep(0.1)
        print("切换加载时间 %.2f 秒" % (date4-date3))
        result = '%.2f'%(date4-date3)
        f2= open("D://1.txt",'a')
        f2.write("\r\n"+filename+"-----切换加载时间:"+str(result)+"秒")
        f2.close()
        file2 = open(self.switch_path+filename+self.suffix,'a')
        file2.write("\r\n"+str(result))
        file2.close()
        driver.switch_to.default_content()
        sleep(2)


# if __name__ == "__main__":
#     pytest.main(["-sv","1test_previewloading.py"])















