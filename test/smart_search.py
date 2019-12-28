# coding = utf-8

# 智能搜索验证
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep
import time

from common.comfunction import User
from common.comfunction import execBrower
from common.comfunction import highlight
from common.comparameter import symbol
from common.comfunction import com_xpath
from selenium.webdriver.common.keys import Keys

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














mode = 2
driver = execBrower(mode)
User().login(driver)
# search_home().lately_collection(driver)
# search_home().my_subscribe(driver)
# search_home().my_annotation(driver)
search_result().search(driver)
driver.quit()








