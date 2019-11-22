# coding=utf-8

# 清空私有資源
import time
from time import sleep
from  selenium.webdriver.support.ui import WebDriverWait

from common.comfunction import User
from common.comfunction import com_xpath

# 清空私有資源，只需传入driver
def clean(driver):
    """ 清空私有資源"""
    User().root_private(driver)
    sleep(1)
    driver.find_element_by_xpath("//input[@type='checkbox']").click()
    el =com_xpath().com_listButton(driver,button='删除')
    WebDriverWait(driver,5,0.5).until()






















