# coding=utf-8
import io
# from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
# from selenium.webdriver.chrome.options import Options
# 报告
# import pytest
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
from common.comfunction import com_xpath
from common.comfunction import com_path

# 回收站验证
upload_url = os.path.join(com_path(),"19种格式","office","2017年12月11日-2017年12月15日发行监管部.doc")
upload_url2 = os.path.join(com_path(),"19种格式","其他","146页年度报告.PDF")
name = "2017年12月11日-2017年12月15日发行监管部"
name2 = "146页年度报告"


class Testrubbish:
    ''' 回收站验证'''

    def test_folder(self, browser, base_url, images_path):
        """ 删除恢复文件夹"""
        # 调用登录方法
        driver = browser
        new_user().new_login(browser, base_url)
        # 新建文件夹
        folder = str(time.time())
        User().createFolder(driver, folder)
        # 进入文件夹
        driver.find_element_by_xpath("//span[text()='" + folder + "']").click()
        # 上传文件
        driver.find_element_by_xpath("//input[@type='file']").send_keys(upload_url)
        driver.find_element_by_xpath("//input[@type='file']").send_keys(upload_url2)
        sleep(15)
        try:
            WebDriverWait(driver, 5, 0.5).until(
                ec.element_to_be_clickable((By.XPATH, "//span[text()='" + name2 + "']")))
            driver.find_element_by_xpath("//input[@type='checkbox']").click()
            el1 = com_xpath().com_listButton(driver, button="delete")
            el1.click()
            try:
                WebDriverWait(driver, 2, 0.5) \
                    .until(ec.presence_of_element_located((By.XPATH, "//div[@class='ant-modal-body']")))
                # driver.find_element_by_xpath("//span[text()='确 定']/..").click()
                el6 = driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-danger']")
                ActionChains(driver).move_to_element(el6).perform()
                el6.click()
            except Exception as e:
                print(e)
                print("弹框发生异常")
        except Exception as e:
            print(e)
            print("上传文件刷新异常")
        # 退出文件夹
        sleep(1)
        print("准备退出二级目录")
        driver.find_element_by_xpath("//a[text()='私有资料']").click()
        # driver.back()
        try:
            WebDriverWait(driver, 5, 0.5) \
                .until(ec.presence_of_element_located((By.XPATH, "//span[text()='" + folder + "']")))
            el2 = driver.find_element_by_xpath("//span[text()='" + folder + "']")
            ActionChains(driver).move_to_element(el2).perform()
            els3 = driver.find_elements_by_xpath("//input[@type='checkbox']")
            els3[1].click()
            el4 = com_xpath().com_listButton(driver, button="delete")
            el4.click()
            try:
                WebDriverWait(driver, 3, 0.5) \
                    .until(ec.presence_of_element_located((By.XPATH, "//div[@class='ant-modal-body']")))
                el6 = driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-danger']")
                ActionChains(driver).move_to_element(el6).perform()
                el6.click()
                sleep(0.5)
            except Exception as e:
                print(e)
                print("弹框发生异常")
        except Exception as e:
            print(e)
            print("刷新超时或者规则改变")
        sleep(1)
        # 进入回收站
        driver.find_element_by_xpath("//span[text()='回收站']/..").click()
        try:
            WebDriverWait(driver, 5, 0.5).until(ec.presence_of_element_located((By.XPATH, "//span[text()='名称']")))
            for i in range(15):
                try:
                    el4 = driver.find_element_by_xpath("//span[text()='" + name + "']")
                    ActionChains(driver).move_to_element(el4).perform()
                    # 点击前面选项框，多选
                    driver.find_element_by_xpath(
                        "//span[text()='" + name + "']/../../..//td[1]//input[@type='checkbox']").click()
                    print("找到了第一个文件")
                    el7 = driver.find_element_by_xpath("//span[text()='" + name2 + "']")
                    ActionChains(driver).move_to_element(el7).perform()
                    driver.find_element_by_xpath(
                        "//span[text()='" + name2 + "']/../../..//td[1]//input[@type='checkbox']").click()
                    print("找到了第二个文件")
                    driver.get_screenshot_as_file(os.path.join(images_path,"test_folder-回收站截图",str(time.time())+ ".png"))
                    break
                except Exception as e:
                    print(e)
                    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
                    print("往下滚动")
            # 恢复文件
            driver.find_element_by_xpath("//div[contains(@class,'recycling_workWrap')]/img[2]").click()
            print("点击恢复按钮")
            driver.refresh()
            WebDriverWait(driver, 5, 0.5).until(ec.presence_of_element_located((By.XPATH, "//span[text()='名称']")))
            # ActionChains(driver).send_keys(Keys.HOME).perform()
            for i2 in range(5):
                try:
                    el5 = driver.find_element_by_xpath("//span[text()='" + folder + "']")
                    ActionChains(driver).move_to_element(el5).perform()
                    # 点击选项框
                    driver.find_element_by_xpath(
                        "//span[text()='" + folder + "']/../../..//td[1]//input[@type='checkbox']").click()
                    print("找到了文件夹元素")
                    print("准备点击恢复文件夹")
                    # 恢复文件
                    driver.find_element_by_xpath("//div[contains(@class,'recycling_workWrap')]/img[2]").click()
                    print("点击恢复文件夹")
                    break
                except Exception as e:
                    print(e)
                    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
                    print("往后滚动")

            # 返回私有资料
            com_xpath().com_log(driver)
            driver.get_screenshot_as_file(os.path.join(images_path,"test_folder-恢复目录查看",str(time.time())+".png"))
            sleep(0.5)
            driver.find_element_by_xpath("//span[text()='" + folder + "']").click()
            sleep(0.5)
            driver.get_screenshot_as_file(os.path.join(images_path,"test_folder-恢复文件查看",str(time.time())+ ".png"))

        except Exception as e:
            print(e)


# if __name__ == '__main__':
#     pytest.main(["-sv", "test_rubbish.py"])
