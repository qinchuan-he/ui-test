# coding=utf-8

# 清空私有資源
import time
from time import sleep
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


from common.comfunction import User
from common.comfunction import com_xpath
from common.comfunction import com_alert
from common.comfunction import OpenBrowser

# 清空私有資源，只需传入driver
def clean_private(driver):
    """ 清空私有資源"""
    User().root_private(driver)
    sleep(1)
    el1 = driver.find_elements_by_xpath("//input[@type='checkbox']")
    if len(el1)>1:
        el1[0].click()
        sleep(1.5)
        el =com_xpath().com_listButton(driver,button='delete')
        el.click()
        sleep(1)
        com_alert().com_delete(driver,button='确定')
        sleep(1)
    com_xpath().com_contentcatalog(driver,button='回收站')
    sleep(0.5)
    try:
        sleep(0.5)
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        sleep(0.5)
        driver.find_element_by_xpath("//img[contains(@class,'recycling_fileIco')]").click()
        sleep(0.5)
        com_alert().com_delete(driver,button='确定')
        sleep(0.5)
    except Exception as e:
        pass



mode = 2
driver = OpenBrowser(mode)
User().login(driver)
clean_private(driver)
User().login_out(driver)
driver.quit()
























