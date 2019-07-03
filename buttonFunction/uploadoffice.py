#coding=utf-8

import io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#报告
import unittest
from HTMLTestRunner import HTMLTestRunner
from time import sleep
import time   #生成时间戳用
import os    #上传autoit用
import sys
"""解决vscode中不能引用别的模块的问题"""
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# print(sys.path)
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

# 引入公共方法
from common.comfunction import execBrower
from common.comfunction import user

# 上传office相关文件
class up_office(unittest.TestCase):
    '''上传office相关文件'''
    def upload_office(self):
        '''上传office文件'''
        mode=2
        driver = execBrower(mode)
        user().login(driver)
        # 公共参数
        picturePath="C:\\work\\1测试\\10自动化\\截图保存\\19种上传格式截图\\office\\"
        showPath="file:///C:/work/1测试/10自动化/截图保存/19种上传格式截图/office/"
        resultpath = "C:\\work\\1测试\\10自动化\\报告\\"

        waitTime=5
        uploadwait= 15 #上传之后的等待时间
        # 私有根目录新建文件夹
        el1=driver.find_element_by_xpath("//span[text()='新建']")
        sleep(waitTime)
        ActionChains(driver).move_to_element(el1).perform()
        driver.find_element_by_xpath("//li[text()='新建文件夹']").click()
        folder1=int(time.time())
        print("新建文件夹：%s " %folder1)
        driver.switch_to.active_element.send_keys(folder1)
        driver.switch_to.active_element.send_keys(Keys.ENTER)
        # 进入文件夹
        driver.find_element_by_xpath("//span[text()="+str(folder1)+"]").click()

        # 上传文件
        # office相关
        fpath = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\office\\"
        word1name = "2017年12月11日-2017年12月15日发行监管部"
        word2name = "带图片表格文档"
        excel1name = "003_模板_TestLink测试用例导入"
        excle2name = "cyprex1.3测试用例"
        pptname = "小z素材-商务炫酷风格动态模板-003"
        # 新建office文件夹，并进入
        el1=driver.find_element_by_xpath("//span[text()='新建']")
        sleep(waitTime)
        ActionChains(driver).move_to_element(el1).perform()
        driver.find_element_by_xpath("//li[text()='新建文件夹']").click()
        office = "office"

        driver.switch_to.active_element.send_keys(office)
        driver.switch_to.active_element.send_keys(Keys.ENTER)
        print("创建office分类文件夹成功： %s" %office)
        sleep(1)
        driver.find_element_by_xpath("//span[text()="+"'"+office+"'"+"]").click()
        # 上传office文件
        driver.find_element_by_xpath("//input[@type='file']").send_keys(fpath+word1name+".doc")
        driver.find_element_by_xpath("//input[@type='file']").send_keys(fpath+word2name+".docx")
        driver.find_element_by_xpath("//input[@type='file']").send_keys(fpath+excel1name+".xls")
        driver.find_element_by_xpath("//input[@type='file']").send_keys(fpath+excle2name+".xlsx")
        driver.find_element_by_xpath("//input[@type='file']").send_keys(fpath+pptname+".ppt")
        sleep(20)
        # 截图并输出
        date1=str(int(time.time()))
        driver.get_screenshot_as_file(picturePath+date1+".png")

        print("<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='block';document.getElementById('fade').style.display='block'\">"+word1name+"等上传成功</a>"
            +"<div id=\"light\" class=\"white_content\">"
            +"<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='none';document.getElementById('fade').style.display='none'\" style=\"align-content: center\">点这里关闭</a>"
            +"<img height=\"800\" width=\"1400\" src=\""+picturePath+date1+".png"+"\">"
            +"</div>" 
            +"<div id=\"fade\" class=\"black_overlay\"></div>")

        # 预览文件
        #点击
        driver.find_element_by_xpath("//span[text=\'"+word1name+"\']").click()
        # 等待加载，准备截图
        WebDriverWait(driver, 15, 0.2).until(ec.presence_of_element_located(By.XPATH, "//iframe"))
        sleep(1)
        date2=str(int(time.time()))
        driver.get_screenshot_as_file(picturePath+date2+".png")
        print("<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='block';document.getElementById('fade').style.display='block'\">"+word1name+"预览</a>"
            +"<div id=\"light\" class=\"white_content\">"
            +"<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='none';document.getElementById('fade').style.display='none'\" style=\"align-content: center\">点这里关闭</a>"
            +"<img height=\"800\" width=\"1400\" src=\""+picturePath+date2+".png"+"\">"
            +"</div>" 
            +"<div id=\"fade\" class=\"black_overlay\"></div>")
        driver.find_element_by_xpath("//button/span[contains(text(),'返回']")
        WebDriverWait(driver, 5, 0.2).until_not(ec.presence_of_element_located(By.XPATH, "//iframe"))

        # 预览下一个
        driver.find_element_by_xpath("//span[text=\'"+word2name+"\']").click()
        WebDriverWait(driver, 15, 0.2).until(ec.presence_of_element_located(By.XPATH, "//iframe"))
        sleep(1)
        date3=str(int(time.time()))
        driver.get_screenshot_as_file(picturePath+date3+".png")
        print("<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='block';document.getElementById('fade').style.display='block'\">"+word2name+"预览</a>"
            +"<div id=\"light\" class=\"white_content\">"
            +"<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='none';document.getElementById('fade').style.display='none'\" style=\"align-content: center\">点这里关闭</a>"
            +"<img height=\"800\" width=\"1400\" src=\""+picturePath+date3+".png"+"\">"
            +"</div>" 
            +"<div id=\"fade\" class=\"black_overlay\"></div>")
        driver.find_element_by_xpath("//button/span[contains(text(),'返回']")
        WebDriverWait(driver, 5, 0.2).until_not(ec.presence_of_element_located(By.XPATH, "//iframe"))

        #预览下一个
        driver.find_element_by_xpath("//span[text=\'"+excel1name+"\']").click()
        WebDriverWait(driver, 15, 0.2).until(ec.presence_of_element_located(By.XPATH, "//iframe"))
        sleep(1)
        date4=str(int(time.time()))
        driver.get_screenshot_as_file(picturePath+date4+".png")
        print("<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='block';document.getElementById('fade').style.display='block'\">"+excel1name+"预览</a>"
            +"<div id=\"light\" class=\"white_content\">"
            +"<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='none';document.getElementById('fade').style.display='none'\" style=\"align-content: center\">点这里关闭</a>"
            +"<img height=\"800\" width=\"1400\" src=\""+picturePath+date4+".png"+"\">"
            +"</div>" 
            +"<div id=\"fade\" class=\"black_overlay\"></div>")
        driver.find_element_by_xpath("//button/span[contains(text(),'返回']")
        WebDriverWait(driver, 5, 0.2).until_not(ec.presence_of_element_located(By.XPATH, "//iframe"))

        # 预览下一个
        driver.find_element_by_xpath("//span[text=\'"+excle2name+"\']").click()
        WebDriverWait(driver, 15, 0.2).until(ec.presence_of_element_located(By.XPATH, "//iframe"))
        sleep(1)
        date5=str(int(time.time()))
        driver.get_screenshot_as_file(picturePath+date5+".png")
        print("<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='block';document.getElementById('fade').style.display='block'\">"+excle2name+"预览</a>"
            +"<div id=\"light\" class=\"white_content\">"
            +"<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='none';document.getElementById('fade').style.display='none'\" style=\"align-content: center\">点这里关闭</a>"
            +"<img height=\"800\" width=\"1400\" src=\""+picturePath+date5+".png"+"\">"
            +"</div>" 
            +"<div id=\"fade\" class=\"black_overlay\"></div>")
        driver.find_element_by_xpath("//button/span[contains(text(),'返回']")
        WebDriverWait(driver, 5, 0.2).until_not(ec.presence_of_element_located(By.XPATH, "//iframe"))
    
        # 预览下一个
        driver.find_element_by_xpath("//span[text=\'"+pptname+"\']").click()
        WebDriverWait(driver, 15, 0.2).until(ec.presence_of_element_located(By.XPATH, "//iframe"))
        sleep(1)
        date6=str(int(time.time()))
        driver.get_screenshot_as_file(picturePath+date6+".png")
        print("<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='block';document.getElementById('fade').style.display='block'\">"+pptname+"预览</a>"
            +"<div id=\"light\" class=\"white_content\">"
            +"<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='none';document.getElementById('fade').style.display='none'\" style=\"align-content: center\">点这里关闭</a>"
            +"<img height=\"800\" width=\"1400\" src=\""+picturePath+date6+".png"+"\">"
            +"</div>" 
            +"<div id=\"fade\" class=\"black_overlay\"></div>")
        driver.find_element_by_xpath("//button/span[contains(text(),'返回']")
        WebDriverWait(driver, 5, 0.2).until_not(ec.presence_of_element_located(By.XPATH, "//iframe"))

if __name__ == "__main__":
    testunite = unittest.TestSuite()
    testunite.addTest(up_office("upload_office"))

    # 生成报告
    fp = open(resultpath+'up_office.html','wb')
    runner = HTMLTestRunner(stream=fp, title='upoffice', description='执行情况：')
    runner.run(testunite)
    fp.close()
































