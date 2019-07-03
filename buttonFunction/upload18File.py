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
        mode=1
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
        word1path = fpath+"2017年12月11日-2017年12月15日发行监管部.doc"
        word2path = fpath+"带图片表格文档.docx"
        excel1path = fpath+"003_模板_TestLink测试用例导入.xls"
        excle2path = fpath+"cyprex1.3测试用例.xlsx"
        pptpath = fpath+"小z素材-商务炫酷风格动态模板-003.ppt"
        # 图片
        tpath = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\图片\\"
        jpgpath = tpath+"timg.jpg"
        pngpath = tpath+"验证图片.png"
        bmppath = tpath+"BMP图片.bmp"
        # 音频
        ypath = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\音频\\"
        pampath = ypath+"16k.pcm"
        wavpath = ypath+"筷子兄弟《小苹果》.wav"
        amrpath = ypath+"另一种格式.amr"
        mp3path = ypath+"群星 - 贾谊《过秦论》.mp3"
        m4apath = ypath+"世纪大道199号.m4a"
        # 其他
        qpath="C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\其他\\"
        pdfpath = qpath+"146页年度报告.PDF"
        zippath = qpath+"测试解压.zip"
        hmtlpath = qpath+"厦门亿联网络技术股份有限公司 关于召开 2018 年年度股东大会的通知.html"
        rarpath = qpath+"上传文件.rar"
        txtpath = qpath+"天空1.txt"

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
        driver.find_element_by_xpath("//input[@type='file']").send_keys(word1path)
        driver.find_element_by_xpath("//input[@type='file']").send_keys(word2path)
        date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        date1=str(int(time.time()))
        imageurl=picturePath+"word上传成功截图"+date
        driver.get_screenshot_as_file(picturePath+"word上传成功截图"+date1+".png")
        print("<a href=\""+picturePath+"word上传成功截图"+date1+".png"+"\">word上传成功截图</a>")

        print("<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='block';document.getElementById('fade').style.display='block'\">word上传成功截图</a>"
            +"<div id=\"light\" class=\"white_content\">"
            +"<a href = \"javascript:void(0)\" onclick = \"document.getElementById('light').style.display='none';document.getElementById('fade').style.display='none'\" style=\"align-content: center\">点这里关闭</a>"
            +"<img height=\"800\" width=\"1400\" src=\""+picturePath+"word上传成功截图"+date1+".png"+"\">"
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