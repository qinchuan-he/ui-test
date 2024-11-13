# coding = utf-8

# 解决执行不能跨包问题
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)

print(sys.path)

from common.comfunction import OpenBrowser
from test.smart_search import search_result
from common.private import ReportProperty
from common.private import folder_path


mode = 1
driver = OpenBrowser(mode)
# User().login(driver)
# search_home().lately_collection(driver)
# search_home().my_subscribe(driver)
# search_home().my_annotation(driver)
# search_result().search(driver)
# check_jmeter 方法传1代表15分钟检查，2代表2小时检查
# image_path = os.path.join(folder_path,'截图','jmeter报告')
search_result().check_jmeter(driver,ReportProperty().FIFTEEN_MINUTES_REPORT,1)
driver.quit()