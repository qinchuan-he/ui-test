import time
from time import sleep
# from typing import List
import requests
import re
import openpyxl
import os
from selenium.webdriver.common.action_chains import ActionChains
from  common.comfunction import OpenBrowser,User


def insert_frag():
    """ 加入碎片"""
    mode = 2
    driver = OpenBrowser(mode)
    user = '10023652214'
    User().login(driver,user)
    driver.get('https://testcyprex.fir.ai/files/6zQlJPLMMvV83n2O')
    sleep(3)
    el1 = driver.find_element_by_xpath("//p[contains(text(),'本年度报告摘要来自年度报告全文')]")
    print(el1)
    print(type(el1))
    action = ActionChains(driver)
    action.click_and_hold(el1)
    action.move_by_offset(200,0)
    action.release()
    action.perform()
    driver.find_element_by_xpath("//span[text()='加入碎片']").click()
    # el2 = driver.find_elements_by_xpath("//p[contains(text(),'本公司董事会、监事会及董事、监事、高级管理')]")
    # ActionChains(driver).move_to_element(el2).perform()





if  __name__ == "__main__":
    insert_frag()



