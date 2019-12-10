# coding=utf-8

import pytest
from common.newcomfunction import new_user
from common.comfunction import *
from buttonFunction.function_contractrelated import *
from buttonFunction.function_checkcontract import *
from common.comfunction import User


# 检查合同比对和审校，结果
file1_name="合同1"
file2_name="合同1扫描件（8张合并）"
class Test_checkcontract:
    '''合同检查'''
    def test_checkcontract(self,browser,base_url,images_path):
        ''' 合同防伪校验和合同审校'''
        new_user().new_login(browser,base_url)
        driver = browser

        check_conpare(driver,images_path,"test_checkcontract")
        check_poorfreading(driver,images_path,"test_checkcontract")








    # def test_poorfreading(self,browser):
    #     '''检查当日审校'''


# if __name__=="__main__":
#     pytest.main(['-sv','test_checkcontract.py'])


