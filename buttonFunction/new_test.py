# coding=utf-8
import io
import sys
import re # 正则提取
"""解决vscode中不能引用别的模块的问题"""
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
from buttonFunction.fragerCheck import test_frager
def getconfig():
    d = {
        "http://192.168.153.1:5556/wd/hub":"chrome"
        #  ,"http://192.168.1.72:5558/wd/hub":"chrome"
        # , "http://192.168.1.31:5559/wd/hub": "chrome"
         }
    return d
from selenium import webdriver
for host,browser in getconfig().items():
    print(host)
    print(browser)
    # driver = webdriver.Remote(
    #     command_executor="http://127.0.0.1:4444/wd/hub",
    #     desired_capabilities={'platform':'ANY',
    #                           'browserName':browser,
    #                           'vwesion':'',
    #                           'javascriptEnabled':True
    #                           }
    # )
    # test_frager()
    test_frager().test_filePath()
    # driver.get("http://www.baidu.com")
    # driver.find_element_by_id("kw").send_keys("hello")
    # driver.find_element_by_id("su").click()
    # time.sleep(3)
    # driver.quit()


# class config:
#     lists = ["chrome"]
#     for i in lists:
#         print(i)
#         driver = webdriver.Remote(
#             command_executor="http://127.0.0.1:4444/wd/hub",
#             desired_capabilities={'platform': 'ANY',
#                                   'browserName': i,
#                                   'vwesion': '',
#                                   'javascriptEnabled': True
#                                   }
#         )
#         driver.get("http://www.baidu.com")
#         driver.find_element_by_id("kw").send_keys("hello")
#         driver.find_element_by_id("su").click()
#         time.sleep(3)
#         driver.quit()









