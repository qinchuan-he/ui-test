# coding = utf-8

# 智能搜索验证,其中包含了jmeter报告的检查方法
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep
import time

from common.comfunction import User
from common.comfunction import OpenBrowser
from common.comfunction import highlight
from common.comparameter import symbol
from common.comfunction import com_xpath
from selenium.webdriver.common.keys import Keys
from common.comfunction import send_mail
from common.private import EmailProperty,folder_path
import os

class search_home(object):
    """ 智能搜索首页的相关操作，需要按照函数顺序来执行 """
    def lately_collection(self,driver,image_path=None, image_prefix=None):
        """ 最近收藏"""
        # 切换到智能搜索
        User().switch_navigation(driver, name="智能搜索")
        try:
            # 是否有最近收藏
            driver.find_element_by_xpath("//div[contains(@class,'GlobalSearchPage_searchBody')]")
            if image_path:
                driver.get_screenshot_as_file(image_path+image_prefix+"-收藏原格式"+str(time.time())+".png")

            try:
                WebDriverWait(driver,5,0.5).until(ec.element_to_be_clickable((By.XPATH,"//span[text()='纯文本']/..")))
                el1 = driver.find_element_by_xpath("//span[text()='纯文本']/..")
                highlight(driver,el1)
                el1.click()
                sleep(1)
                if image_path:
                    driver.get_screenshot_as_file(image_path+image_prefix+"-收藏原格式"+str(time.time())+".png")
            except Exception as e:
                print("未解析出纯文本")
        except Exception as e:
            print("没有收藏内容")

    def my_subscribe(self,driver,image_path=None,image_prefix=None):
        """ 我的订阅 ，前提是处于智能搜索页面"""
        # 进入我的订阅
        sleep(1)
        driver.find_element_by_xpath("//li[text()='我的订阅']").click()
        sleep(1)
        if image_path:
            driver.get_screenshot_as_file(image_path+image_prefix+"-订阅截图"+str(time.time())+".png")

    # 我的批注,前提是进入智能搜索首页
    def my_annotation(self,driver,image_path=None,image_prefix=None):
        """ 我的批注"""
        sleep(1)
        driver.find_element_by_xpath("//li[text()='我的批注']").click()
        sleep(1)
        if image_path:
            driver.get_screenshot_as_file(image_path+image_prefix+"-我的批注"+str(time.time())+".png")

class search_result(object):
    # 智能搜索
    def search(self,driver,image_path=None,image_prefix=None):
        # 切换到智能搜索
        User().switch_navigation(driver, name="智能搜索")
        el = com_xpath().smart_search(driver)
        el.send_keys("*")
        driver.switch_to.active_element.send_keys(Keys.ENTER)
        sleep(2)
        for i in symbol().english_symbol:
            el1 =  driver.find_element_by_xpath("//input[@type='text']")
            el1.send_keys(Keys.BACK_SPACE)
            el1.clear()
            el1.send_keys(i)
            driver.switch_to.active_element.send_keys(Keys.ENTER)
            sleep(3)
            if image_path:
                driver.get_screenshot_as_file(image_path+image_prefix+str(time.time())+".png")
        print("英文符号完毕")
        for i in symbol().china_symbol:
            el1 = driver.find_element_by_xpath("//input[@type='text']")
            el1.send_keys(Keys.BACK_SPACE)
            el1.clear()
            el1.send_keys(i)
            driver.switch_to.active_element.send_keys(Keys.ENTER)
            sleep(3)
            if image_path:
                driver.get_screenshot_as_file(image_path + image_prefix + str(time.time()) + ".png")
        print("中文符号完毕")

    def check_jmeter(self,driver,report_url,position,image_path=None,image_prefix=None):
        """
        检查jmeter执行情况
        :param driver:
        :param image:
        :param image_prefix:
        :return:
        """

        # 2020-06-05增加方法，创建jmeter报告截图
        jmeter_path = os.path.join(folder_path, '截图', 'jmeter报告')
        if os.path.exists(jmeter_path):
            for i in os.listdir(jmeter_path):
                os.remove(os.path.join(jmeter_path, i))
        else:
            os.mkdir(jmeter_path)

        sleep(10)
        driver.get(report_url)
        sleep(0.5)
        el = driver.find_elements_by_xpath("//div[@style='font-size:8pt;text-align:center;padding:2px;color:white;']")
        if len(el)>1:
            print("有问题")

            # 2020-06-05 增加，错误排序之后滚动
            el3s = driver.find_elements_by_xpath("//div[@class='tablesorter-header-inner']")
            screenshot = []
            screenshot_name = []
            for i in range(len(el3s)):
                if 'Error' in el3s[i].text:
                    if '%' in el3s[i].text:
                        ActionChains(driver).move_to_element(el3s[i]).perform()
                        sleep(0.5)
                        ActionChains(driver).double_click(el3s[i]).perform()
                        for loop in range(2):
                            sleep(0.5)
                            ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
                        images_url= os.path.join(jmeter_path,str(time.time())+'.png')
                        driver.get_screenshot_as_file(images_url)
                        screenshot.append(images_url)
                        screenshot_name.append('error'+str(i)+'.png')
                        break

            if image_path:
                driver.get_screenshot_as_file(image_path+image_prefix+str(time.time())+".png")
            # 2020-06-05 增加截图
            if position==1:
                send_mail("接口检查有问题",EmailProperty().EMAIL_ATTACHMENT1,screenshot,screenshot_name)
            elif position==2:
                send_mail("接口检查有问题", EmailProperty().EMAIL_ATTACHMENT2, screenshot, screenshot_name)
        else:
           s = str(el[0].text)
           a = s.split("\n",2)[0]
           if a=='OK':
               print("全部通过")
               # send_mail("没有问题", EmailProperty().EMAIL_ATTACHMENT2, EmailProperty().EMAIL_ATTACHMENT2, "哎临时用下.html")


        # sleep(5)
















# mode = 2
# driver = OpenBrowser(mode)
# User().login(driver)
# search_home().lately_collection(driver)
# # search_home().my_subscribe(driver)
# search_home().my_annotation(driver)
# search_result().search(driver)
# search_result().check_jmeter(driver,"http://192.168.1.49:8080/jmeter/report/index.html")
# sleep(10)
# driver.quit()








