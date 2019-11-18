# coding=utf-8

# 造数据，目前造合同防伪和合同审校的数据
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from common.comfunction import *
from buttonFunction.function_contractrelated import *
mode = 1
driver = execBrower(mode)
driver.get(url)
User().login(driver)
url1 = str(com_path()+"19种格式\\比对文件\\合同1.doc")
url2 = com_path()+"19种格式\\比对文件\\合同1扫描件（8张合并）.pdf"
contract_compare(driver,url1,url2)
contract_Proofreading(driver,url1)






