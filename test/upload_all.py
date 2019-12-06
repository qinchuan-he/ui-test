# coding=utf-8

#2019-12-02
#上传验证
# 新建一个文件夹，进入文件夹之后上传，截图
import time
from time import sleep
import os
from common.comfunction import execBrower
from common.comfunction import User
from common.comfunction import com_xpath
from common.comfunction import com_path
from common.comfunction import up_list

# 准备上传


def upload_all(driver,image_path=None,image_prefix=None):
    """ 上传所有文件"""
    # 返回私有根目录
    User().root_private(driver)
    # 新建文件夹
    up_folder = str(time.time())
    User().createFolder(driver,folder=up_folder)
    # 进入文件夹
    driver.find_element_by_xpath("//span[text()='"+up_folder+"']/..").click()
    sleep(0.5)

    # 上传
    for i in up_list:
        com_xpath().com_localupload(driver,i)
        print("循环："+i)
    sleep(15)


mode = 2
driver = execBrower(mode)
User().login(driver)
upload_all(driver)




