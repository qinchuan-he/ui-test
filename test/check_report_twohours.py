# coding = utf-8
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

from common.comfunction import execBrower
from common.comfunction import User
from common.private import UserProperty
from common.private import EmailProperty
from common.private import ReportProperty
from common.comfunction import send_mail
from test.smart_search import search_result

mode = 1
driver = execBrower(mode)
search_result().check_jmeter(driver,ReportProperty().TWO_HOURS_REPORT_JMETER,2) # 2表示每隔两小时
driver.quit()
sleep(1)



mode = 1
driver = execBrower(mode)
driver.get(ReportProperty().TWO_HOURS_REPORT_UI)

# driver.find_element_by_xpath("//td[contains(text(),'通过率= 100.00%')]")
try:
    WebDriverWait(driver,1.5,0.5).until(ec.presence_of_element_located((By.XPATH,"//td[contains(text(),'通过率：100.00%')]")))
    print("没有问题")
    # send_mail("两小时检查没有问题", EmailProperty().EMAIL_ATTACHMENT2, EmailProperty().EMAIL_ATTACHMENT2, "twoHours_check.html")
except Exception as e:
    print("存在问题，要发邮件")
    send_mail("ui检查存在问题", EmailProperty().EMAIL_ATTACHMENT3, EmailProperty().EMAIL_ATTACHMENT3, "twoHours_check.html")
driver.quit()

