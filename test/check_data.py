# coding=utf-8

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.comfunction import User
from common.comfunction import OpenBrowser
from common.comfunction import team
from common.comfunction import up_analysis
from common.comfunction import folder_analysis
from test.upload_relate import upload_fileanalysis
from common.comfunction import get_urlname
from common.comfunction import com_xpath
import random

import time
from time import sleep


class analysis(object):
    """ 解析验证"""

    # 检查解析，传入团队名称，目前使用默认名称.传入检查范围,html,text,all
    def check_analysis(self,driver,file_name=None, checkrange=None, teamname=None, image_path=None, image_prefix=None):
        """ 检查word解析"""
        if teamname:
            team().check_team()
        else:
            User().root_private(driver)

        # driver.find_element_by_xpath("//span[contains(text(),'"+folder_analysis+"')]").click()
        sleep(0.5)
        if image_path:
            driver.get_screenshot_as_file(image_path+image_prefix+"-检查文件上传时间"+str(time.time())+".png")
        driver.find_element_by_xpath("//span[text()='"+file_name+"']/..").click()
        WebDriverWait(driver,15,0.5).until(ec.presence_of_element_located((By.XPATH,"//iframe")))
        el1 = com_xpath().com_previewButton(driver,button="innerSearchModel")
        if el1.is_enabled():
            print("解析成功")
            sleep(0.5)
            el1.click()
            WebDriverWait(driver,10,0.5).until(ec.presence_of_element_located((By.XPATH,"//iframe")))
            sleep(0.5)
            # 有范围表示要检查
            if checkrange:
                print("进入范围")
                if checkrange=='html':
                    if image_path:
                        driver.get_screenshot_as_file(image_path+image_prefix+"-原格式展示"+str(time.time())+".png")
                    try:
                        driver.find_element_by_xpath("//div[text()='图例']").click()
                        sleep(0.5)
                        if image_path:
                            sleep(0.5)
                            driver.find_element_by_xpath("//div[contains(@class,'FileImages_imageBox')]").click()
                            driver.get_screenshot_as_file(image_path+image_prefix+"-图例定位截图"+str(time.time())+"")
                        driver.find_element_by_xpath("//i[@class='anticon anticon-close']").click()
                    except Exception as e:
                        print("没有提取出图例")
                    frame = driver.find_element_by_xpath("//iframe")
                    driver.switch_to.frame(frame)
                    driver.find_element_by_xpath("//input[@type='text']").send_keys("股份，公司")
                    driver.switch_to.active_element.send_keys(Keys.ENTER)
                    sleep(2)
                    driver.switch_to.default_content()
                    driver.find_element_by_xpath("//div[contains(@class,'SameParaSearch_sameParaItemBox')]").click()
                    if image_path:
                        driver.get_screenshot_as_file(image_path+image_prefix+"-列表定位截图"+str(time.time())+".png")
                elif checkrange=='text':
                    el2 = driver.find_element_by_xpath("//span[text()='纯文本']/..")
                    if el2.is_enabled():
                        el2.click()
                        sleep(0.5)
                        WebDriverWait(driver,5,0.5).until(ec.presence_of_element_located((By.XPATH,"//span[text()='同句']")))
                        # # 本次测试验证开始
                        # number = [0,1,2,3,4,5,6,7,8,9]
                        # english_symbol = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+",
                        #                   "=", ";", ":", "'", "<", ">", ".", "?", "/", "\\", "|"]
                        # china_symbol = ["·", "~", "！", "@", "#", "￥", "%", "……", "&", "*", "（", "）", "——", "-", "+",
                        #                   "=", "；", "：", "’", "《", "》", "。", "？", "、", "、", "|"]
                        # english = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","o","r","s","t","u","v","w","x","y"
                        #     ,"z"]
                        # more = ["r,p","s,m"]
                        # chinese = ["公司","股份","科技","建设","集团","发现","金额","风险","证券","航天","宏图","国信证券"]
                        # # for i in chinese:
                        # for i in range(60):
                        #     # driver.find_element_by_xpath("//input[@type='text']").send_keys(i)
                        #     driver.find_element_by_xpath("//input[@type='text']").\
                        #         send_keys(chinese[random.randint(0,11)]+","+chinese[random.randint(0,11)])
                        #     # driver.find_element_by_xpath("//input[@type='text']").send_keys(
                        #     #     chinese[random.randint(0, 7)] + "," + i)
                        #     driver.switch_to.active_element.send_keys(Keys.ENTER)
                        #     sleep(2.5)
                        #     driver.get_screenshot_as_file("C:\\Users\\fir\\Pictures\\QQ浏览器截图\\"+str(time.time())+".png")
                        #     driver.find_element_by_xpath("//input[@type='text']").clear()
                        #
                        # # 本次测试验证结束
                        driver.find_element_by_xpath("//input[@type='text']").send_keys("股份，公司")
                        driver.switch_to.active_element.send_keys(Keys.ENTER)
                        sleep(1.5)
                        if  image_path:
                            driver.get_screenshot_as_file(image_path+image_prefix+"-纯文本截图"+str(time.time())+".png")
                    else:
                        print("纯文本未提取成功")
                else:
                    print("传入参数非规定的")
            else:
                " 这里就是全量检查"
                if image_path:
                    driver.get_screenshot_as_file(image_path + image_prefix + "-原格式展示" + str(time.time()) + ".png")
                try:
                    driver.find_element_by_xpath("//div[text()='图例']").click()
                    sleep(0.5)
                    if image_path:
                        sleep(0.5)
                        driver.find_element_by_xpath("//div[contains(@class,'FileImages_imageBox')]").click()
                        driver.get_screenshot_as_file(image_path + image_prefix + "-图例定位截图" + str(time.time()) + "")
                    driver.find_element_by_xpath("//i[@class='anticon anticon-close']").click()
                except Exception as e:
                    print("没有提取出图例")
                frame = driver.find_element_by_xpath("//iframe")
                driver.switch_to.frame(frame)
                driver.find_element_by_xpath("//input[@type='text']").send_keys("股份，公司")
                driver.switch_to.active_element.send_keys(Keys.ENTER)
                sleep(2)
                driver.switch_to.default_content()
                driver.find_element_by_xpath("//div[contains(@class,'SameParaSearch_sameParaItemBox')]").click()
                sleep(1)
                if image_path:
                    driver.get_screenshot_as_file(image_path + image_prefix + "-列表定位截图" + str(time.time()) + ".png")
                sleep(0.5)
                el2 = driver.find_element_by_xpath("//span[text()='纯文本']/..")
                if el2.is_enabled():
                    el2.click()
                    sleep(0.5)
                    WebDriverWait(driver, 5, 0.5).until(
                        ec.presence_of_element_located((By.XPATH, "//span[text()='同句']")))
                    driver.find_element_by_xpath("//input[@type='text']").send_keys("股份，公司")
                    driver.switch_to.active_element.send_keys(Keys.ENTER)
                    sleep(1.5)
                    driver.find_element_by_xpath("//div[contains(@class,'SameParaSearch_sameParaItemBox')]").click()
                    if image_path:
                        driver.get_screenshot_as_file(image_path + image_prefix + "-纯文本截图" + str(time.time()) + ".png")
                else:
                    print("纯文本未提取成功")
            # 退出内容搜索

        else:
            if image_path:
                driver.get_screenshot_as_file(image_path+image_prefix+"-解析未成功"+str(time.time())+".png")
            print("解析未成功")
        sleep(0.5)
        driver.quit()


class share(object):
    """ 检查列表分享"""
    def check_share(self,driver):
        pass






mode = 2
driver = OpenBrowser(mode)
User().login(driver)
# analysis().check_analysis(driver,get_urlname(up_analysis[0]))
# analysis().check_analysis(driver,"验证图例文件")
analysis().check_analysis(driver,"验证图例文件")

















