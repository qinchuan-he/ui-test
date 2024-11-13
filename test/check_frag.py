import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)
from common.comfunction import OpenBrowser,User
from common.private import UserProperty
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
# 加入碎片检查

def check_frag():
    """"""
    mode = 1
    driver = OpenBrowser(mode)
    User().login(driver,UserProperty.user_check1)
    driver.get('https://cyprex.fir.ai/files/DrqxJ1xM6EPQl27z')
    sleep(3)
    el1 = driver.find_element_by_xpath("//p[contains(text(),'本年度报告摘要来自年度报告全文')]")
    action = ActionChains(driver)
    action.click_and_hold(el1)
    action.move_by_offset(100,0)
    action.release()
    action.perform()
    sleep(0.5)
    driver.find_element_by_xpath("//span[text()='加入碎片']/..").click()
    sleep(5)
    driver.quit()

if __name__=="__main__":
    check_frag()





