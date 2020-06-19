# coding = utf-8

# 最终检查发报告的地方
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
from time import sleep

from common.comfunction import OpenBrowser
from common.comfunction import User
from common.private import UserProperty
from common.private import EmailProperty
from common.private import ReportProperty
from common.comfunction import send_mail,com_path
from test.smart_search import search_result
from common.comfunction import team
from common.comfunction import url25,url26,url27,url28
from buttonFunction.function_contractrelated import contratc_split
from buttonFunction.function_contractrelated import contract_combine

# 检查同步比对、查询等接口,扩展为功能性接口检查
def check_one():
    mode = 1
    driver = OpenBrowser(mode)
    search_result().check_jmeter(driver,ReportProperty().TWO_HOURS_REPORT_JMETER,2) # 2表示每隔两小时
    driver.quit()
    sleep(1)

# 检查智能比对和审校
def check_two():
    mode = 1
    driver = OpenBrowser(mode)
    driver.get(ReportProperty().TWO_HOURS_REPORT_UI)
    # driver.find_element_by_xpath("//td[contains(text(),'通过率= 100.00%')]")
    try:
        WebDriverWait(driver,1.5,0.5).until(ec.presence_of_element_located((By.XPATH,"//td[contains(text(),'通过率：100.00%')]")))
        print("没有问题")
        # send_mail("两小时检查没有问题", EmailProperty().EMAIL_ATTACHMENT2, EmailProperty().EMAIL_ATTACHMENT2, "twoHours_check.html")
    except Exception as e:
        print("存在问题，要发邮件")
        driver.get_screenshot_as_file(os.path.join(com_path(),"截图","检查报告截图.png"))
        add_file = [os.path.join(com_path(),"截图","智能比对列表截图.png"),os.path.join(com_path(),"截图","智能审核列表截图.png")
                    ,os.path.join(com_path(),"截图","检查报告截图.png")]
        add_name = ["compare.png","proofread.png","report.png"]
        send_mail("智能比对和审校检查存在问题", EmailProperty().EMAIL_ATTACHMENT3, add_file, add_name)
    driver.quit()

# 检查拆分和合并----2020-05-20 saas版本关闭协作空间入口
# mode = 1
# driver = OpenBrowser(mode)
# driver.get(UserProperty().url)
# User().login(driver,UserProperty().user_check2)
# team().dismiss_team(driver,"验证的团队")
# sleep(3)
# driver.refresh()
# sleep(2)
# team().check_team(driver,"验证的团队")
# contratc_split(driver,url25)
# contract_combine(driver,url26,url27,url28)
# sleep(7)
# driver.quit()

if __name__=="__main__":
    check_one()