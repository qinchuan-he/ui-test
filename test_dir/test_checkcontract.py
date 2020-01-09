# coding=utf-8

import pytest
from common.newcomfunction import new_user
from common.comfunction import *
from buttonFunction.function_contractrelated import *
from buttonFunction.function_checkcontract import *
from common.comfunction import User


# 检查合同比对和审校，结果，于2020/01/07废弃，因为服务已经每两小时检查一次
file1_name="合同1"
file2_name="合同1扫描件（8张合并）"
class Test_checkcontract:
    '''合同检查'''
    def test_checkcontract(self,browser,base_url,images_path):
        ''' 智能比对和智能审核'''
        # new_user().new_login(browser,base_url)
        # driver = browser
        # check_compare(driver,images_path,"test_checkcontract")
        # check_proofreading(driver,images_path,"test_checkcontract")
        print("该检查点已废弃")








    # def test_proofreading(self,browser):
    #     '''检查当日审校'''


# if __name__=="__main__":
#     pytest.main(['-sv','test_checkcontract.py'])


