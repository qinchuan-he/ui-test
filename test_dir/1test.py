# coding=utf-8

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pytest
from time import sleep

# 引入公共方法
from common.newcomfunction import new_user
from test_dir.test_previewloading import Test_loading # 引用方法改名了，前面加了1

class Test_1:
    """test"""
    def test_loop(self, browser, base_url, images_path):
        new_user().new_login(browser,base_url)
        filename=['图例验证文件','146页年度报告','282页','336页','496页','625页']
        for i in range(len(filename)):
            try:
                Test_loading().test_previewLoading(browser, filename[i])
                Test_loading().test_switchHtml(browser,filename[i])
            except Exception as e:
                print(e)
            # browser.get("https://testcyprex.fir.ai/folders/8860")
            browser.get("https://cyprex.fir.ai/folders/2050")
            sleep(2)

if __name__=="__main__":
    pytest.main(["-sv","1test.py"])

















