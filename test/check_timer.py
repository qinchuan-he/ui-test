# coding = utf-8

# 解决执行不能跨包问题
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

print(sys.path)

from common.comfunction import execBrower
from smart_search import search_result


mode = 2
driver = execBrower(mode)
# User().login(driver)
# search_home().lately_collection(driver)
# search_home().my_subscribe(driver)
# search_home().my_annotation(driver)
# search_result().search(driver)
search_result().check_jmeter(driver,"http://192.168.1.49:8080/jmeter/report/index.html",1)
driver.quit()