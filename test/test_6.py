import time
from time import sleep
# from typing import List
import requests
import re
import pyxl
import os
from selenium.webdriver.common.action_chains import ActionChains
from  common.comfunction import OpenBrowser,User
import datetime
import math

def insert_frag():
    """ 加入碎片"""
    mode = 2
    driver = OpenBrowser(mode)
    user = '10023652214'
    User().login(driver,user)
    driver.get('https://testcyprex.fir.ai/files/6zQlJPLMMvV83n2O')
    sleep(3)
    el1 = driver.find_element_by_xpath("//p[contains(text(),'本年度报告摘要来自年度报告全文')]")
    print(el1)
    print(type(el1))
    action = ActionChains(driver)
    action.click_and_hold(el1)
    action.move_by_offset(200,0)
    action.release()
    action.perform()
    sleep(0.5)
    driver.find_element_by_xpath("//span[text()='加入碎片']/..").click()
    # el2 = driver.find_elements_by_xpath("//p[contains(text(),'本公司董事会、监事会及董事、监事、高级管理')]")
    # ActionChains(driver).move_to_element(el2).perform()


def compute(s:int):
    print(s/3600/24)

def  wff():
    a1 = time.mktime(time.strptime('2021-05-13 14:45:00','%Y-%m-%d %H:%M:%S'))
    a2 = time.mktime(time.strptime('2021-05-12 14:45:00', '%Y-%m-%d %H:%M:%S'))
    a = math.log(a1)
    a_2 = math.log(a2)
    print(a)
    print(a_2)
    print((a-a_2)*1000)
    print(time.time())
    ctime=""
    utime=""
    search_key="ss"
    # for i in range(3):  # 翻页查询
    #     url = "https://testapp.fir.ai/api/resource/search/?search_keywords=" + search_key + "&search_type=001" \
    #             "&start_time=&end_time=&is_correct=true&table_code=001&only_associate=0" \
    #              "&pid=-1&ordering=score&page=" + str(i + 1) + "&last=&ctime=" + ctime + "&utime=" + utime
    #     print(url)

def check_button():
    # button_list = ['标题','加粗','倾斜','下划线','文字颜色','项目符号','图片','表格','链接','下标','上标','文字背景','整体背景','保存']
    # for i in range(len(button_list)-1):
    #     for j in range(len(button_list)-1):
    #         print('{},{}'.format(button_list[i],button_list[j+1]))
    a = "2021"
    try:
        b = time.strptime(a, '%Y-%m-%d')
    except:
        a = a+'-01-01'

    print(a)

    s = datetime.datetime
    print(s.now())
    s = ""
    if s:
        print('-----')

# 问题
def queen(A, cur=0):
    if cur == len(A):
        print(A)
        return 0
    for col in range(len(A)):  # 遍历当前行的所有位置
        A[cur] = col
        for row in range(cur):  # 检查当前位置是否相克
            if A[row] == col or abs(col - A[row]) == cur - row:
                break
        else:  # 如果完成了整个遍历，则说明位置没有相克
            queen(A, cur+1)  # 计算下一行的位置

def cc_for():
    for num in range(10, 20):  # 迭代 10 到 20 之间的数字
        for i in range(2, num):  # 根据因子迭代
            if num % i == 0:  # 确定第一个因子
                j = num / i  # 计算第二个因子
                print('%d 等于 %d * %d' % (num, i, j))
                break  # 跳出当前循环
        else:  # 循环的 else 部分
            print('---------')
            print(num, '是一个质数')
    print('============')

if  __name__ == "__main__":
    # insert_frag()
    # compute(99000000)
    # wff()
    # check_button()
    queen([None]*4)
    # cc_for()