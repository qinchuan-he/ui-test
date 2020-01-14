# coding=utf-8

import time
from time import sleep

from common.comfunction import User,execBrower,com_path
from buttonFunction.function_contractrelated import contract_Proofreading
from buttonFunction.function_checkcontract import check_proofreading

mode = 2
driver = execBrower(mode)
User().login(driver)
url1 = str(com_path()+"19种格式\\比对文件\\合同1.doc")
contract_Proofreading(driver,url1)
User().switch_navigation(driver,name="智能审核")
for i in range(36):
    els = driver.find_elements_by_xpath("//div[@class='ant-row']/div[3]")
    print(len(els))
    print(els[1])
    content = els[1].text
    print(content)
    if content=="要素快照风险报告":
        print("审核成功")
        break
    elif content=="审校失败再次审校":
        print("审核失败")
        break
    elif i==35:
        print("审核超时")
        break
    else:
        sleep(10)

sleep(2)



check_proofreading(driver,is_check="2")
driver.quit()


