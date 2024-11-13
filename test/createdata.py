# coding=utf-8

# 造数据，目前造合同防伪和智能审核的数据,扩展造别的数据
import sys
import os
# 解决执行不能跨包问题
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from common.comfunction import *
from buttonFunction.function_contractrelated import *
# from upload_relate import upload_fileanalysis
mode = 1
driver = OpenBrowser(mode)
driver.get(url)
User().login(driver)
url1 = str(com_path()+"19种格式\\比对文件\\合同1.doc")
url2 = com_path()+"19种格式\\比对文件\\合同1扫描件（8张合并）.pdf"
contract_compare(driver,url1,url2)
contract_Proofreading(driver,url1)

# 增加造解析数据
# upload_fileanalysis(driver)

# 增加数据，分享用






