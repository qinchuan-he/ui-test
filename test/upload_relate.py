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
from common.comfunction import up_analysis

folder_analysis = "解析"

def upload_all(driver,image_path=None,image_prefix=None):
    """ 上传所有文件，到私有根目录"""
    # 返回私有根目录
    User().root_private(driver)
    # 新建文件夹
    up_folder = str(time.time())
    User().createFolder(driver,folder=up_folder)
    # 进入文件夹
    driver.find_element_by_xpath("//span[text()='"+up_folder+"']/..").click()
    sleep(0.5)

    # 上传
    count = 0
    for i in up_list:
        com_xpath().com_localupload(driver,i)
        count+=1
        if count==10:
            if image_path:
                driver.get_screenshot_as_file(image_path+image_prefix+"-上传第一次截图"+str(time.time())+".png")
        # print("上传的是："+i)
    sleep(2)
    if image_path:
        driver.get_screenshot_as_file(image_path+image_prefix+"-上传第二次截图"+str(time.time())+".png")
    sleep(0.5)

def upload_fileanalysis(driver,image_path=None,image_prefix=None):
    """ 上传解析验证文件"""
    folder = folder_analysis+str(time.time())
    User().createFolder(driver,folder)
    driver.find_element_by_xpath("//span[text()='"+folder+"']/..").click()
    # 上传
    count = 0
    for i in up_analysis:
        count+=1
        com_xpath().com_localupload(driver,i)
        print("解析文件 %d 上传成功",count)

    sleep(0.5)





# mode = 2
# driver = execBrower(mode)
# User().login(driver)
# upload_all(driver)




