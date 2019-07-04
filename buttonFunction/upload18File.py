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
# 上传19种格式并且预览，每个截图

class test_upload(unittest.TestCase):
    '''上传19种类型验证'''
    def all_test(self):
        '''所有的上传'''
        mode=2
        driver=execBrower(mode)
        user().login(driver)

        # 公共参数
        picturePath="C:\\work\\1测试\\10自动化\\截图保存\\19种上传格式截图\\office\\"

        showPath="file:///C:/work/1测试/10自动化/截图保存/19种上传格式截图/office/"

        waitTime=5
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
        # 图片
        tpath = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\图片\\"
        jpgname = "timg.jpg"
        pngname= "验证图片.png"
        bmpname = "BMP图片.bmp"
        # 音频
        ypath = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\音频\\"
        pamname = "16k.pcm"
        wavname = "筷子兄弟《小苹果》.wav"
        amrname = "另一种格式.amr"
        mp3name = "群星 - 贾谊《过秦论》.mp3"
        m4aname = "世纪大道199号.m4a"
        # 其他
        qpath="C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\其他\\"
        pdfname = "146页年度报告.PDF"
        zipname = "测试解压.zip"
        hmtlname = "厦门亿联网络技术股份有限公司 关于召开 2018 年年度股东大会的通知.html"
        rarname = "上传文件.rar"
        txtname = "天空1.txt"

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
        # print("//span[text()=\'"+word1name+"\']")
        # WebDriverWait(driver, 15,0.2).until(ec.element_to_be_clickable(By.XPATH,"//span[text()=\'"+word1name+"\']"))

        date1=str(int(time.time()))
        driver.get_screenshot_as_file(picturePath+date1+".png")

        print("<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='block';document.getElementById('fade').style.display='block'\">"+word1name+"上传成功</a>"
            +"<div id=\"light\" class=\"white_content\">"
            +"<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='none';document.getElementById('fade').style.display='none'\" style=\"align-content: center\">点这里关闭</a>"
            +"<img height=\"800\" width=\"1400\" src=\""+picturePath+date1+".png"+"\">"
            +"</div>" 
            +"<div id=\"fade\" class=\"black_overlay\"></div>")
        


 


if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(test_upload("all_test"))

    # 报告
    fp = open('C:\\work\\1测试\\10自动化\\报告\\test.html','wb')
    runner = HTMLTestRunner(stream=fp, title='test报告', description='执行情况：')
    runner.run(testunit)
    fp.close()