# coding=utf-8

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
from time import sleep

from common.comfunction import User
from test.upload_relate import folder_analysis
from common.comfunction import up_analysis
from common.comfunction import get_urlname
from common.comfunction import highlight

class check_analysis:
    """ 检查pdf和word解析结果的"""
    def analysis_PDF(self,driver,image_path=None,image_prefix=None):
        """ 检查PDF后缀的文件的解析"""
        # 进入私有根目录
        User().root_private(driver)
        el1 = driver.find_element_by_xpath("//span[contains(text(),'"+folder_analysis+"')]/..")
        el1[0].click()
        file_name = get_urlname(up_analysis[0])
        driver.find_element_by_xpath("//span[text()='"+file_name+"']").click()
        sleep(0.5)
        WebDriverWait(driver, 5, 0.5).until(ec.presence_of_element_located((By.XPATH,"//iframe")))
        el2 = driver.find_element_by_xpath("//span[text()='内容搜索']/..")
        highlight(driver,el2)
        if image_path:
            driver.get_screenshot_as_file(image_path+image_prefix+"-内容搜索按钮"+".png")
        el2.click()









