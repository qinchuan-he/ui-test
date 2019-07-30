# coding=utf-8
import io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# 报告
import unittest
from HTMLTestRunner import HTMLTestRunner
from time import sleep
import time  # 生成时间戳用
import os  # 上传autoit用
import sys
import re # 正则提取
"""解决vscode中不能引用别的模块的问题"""
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# print(sys.path)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 引入公共方法
from common.comfunction import execBrower  # 启动浏览器函数
from common.comfunction import user  # 用户登录类
from common.comfunction import comHtml  # 生成html报告类
from common.comfunction import team  # 团队类
from common.comfunction import com_upload # 公共上传函数
from common.comfunction import com_xpath  # 公共的定位方法类
from common.comfunction import com_alert  #  公共的弹窗方法类
from common.comfunction import com_share  #  分享类公共方法

resultPath = "C:\\work\\1测试\\10自动化\\报告\\"

# 验证上传文件，批量上传图片

class upload(unittest.TestCase):
    '''上传20张图片'''
    # 上传参数
    picturePath = "C:\\work\\1测试\\10自动化\\截图保存\\test\\"  # 生成截图路径
    url = "C:\\Users\\fir\\Desktop\\上传文件\\html文件\\"
    png = ".png"
    jpg = ".jpg"

    urlpdf = "C:\\Users\\fir\\Desktop\\上传文件\\pdf比对\\市场比对文件\\250-500页\\"
    pdf = ['290页', '294页', '298页', '299页', '307页', '328页', '329页', '330页', '336页']


    # 登录
    mode = 2
    driver = execBrower(mode)
    user().login(driver)
    # 创建文件夹
    folder = str(time.time())
    print(folder)
    user().createFolder(driver, folder)
    sleep(0.5)
    driver.find_element_by_xpath("//span[text()='"+folder+"']").click()
    sleep(1)
    def upload_picture(self):
        '''上传图片'''
        u1 = self.url + "1" + self.png
        u2 = self.url + "2" + self.png
        u3 = self.url + "3" + self.png
        u4 = self.url + "4" + self.png

        u5 = self.url + "5" + self.png
        u6 = self.url + "6" + self.png
        u7 = self.url + "7" + self.png
        u8 = self.url + "8" + self.png
        u9 = self.url + "9" + self.png

        item = """C:\\Users\\fir\\Desktop\\上传文件\\html文件\\1.png
            C:\\Users\\fir\\Desktop\\上传文件\\html文件\\2.png"""      # 多行字符串，我不知道怎么使用变量
        item = '''C:\\Users\\fir\\Desktop\\上传文件\\html文件\\1.png   
            C:\\Users\\fir\\Desktop\\上传文件\\html文件\\2.png'''      # 多行字符串，我不知道怎么使用变量
        item = '%s\n%s' % (u1, u2)          # 多行字符串，正规写法
        item = u1+"\n"+u2                   # 多行字符串
        item = '{}\n{}'.format (u1, u2)     # 多行字符串，占位符写法
        item = '{u1}\n{u2}\n{u3}\n{u4}'.format(u1=u1, u2=u2, u3=u3, u4=u4)  # 多行字符串，这样有个好处是参数重复使用
        item2 = '%s\n%s\n%s\n%s\n%s' % (u5, u6, u7, u8, u9)
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(item)  #准备分批的
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(item2)  # 准备分批的
        for i in range(3):              # 以前的
            self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + str(i+1) + self.png)


        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "1" + self.png)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "2" + self.png)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "3" + self.png)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "4" + self.png)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "5" + self.png)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "6" + self.png)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "7" + self.png)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "8" + self.png)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "9" + self.png)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "10" + self.png)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "11" + self.png)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "12" + self.png)
        # # jpg图片
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "13" + self.jpg)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "14" + self.jpg)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "15" + self.jpg)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "16" + self.jpg)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "17" + self.jpg)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "18" + self.jpg)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "19" + self.jpg)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "20" + self.jpg)
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.url + "21" + self.jpg)
        # com_alert().com_equal(self.driver, self.picturePath, print_name="出现冲突", version="取 消")
        sleep(5)
        datename = str(time.time())
        comHtml().screen_shot(self.driver, self.picturePath, print_name="验证上传重名")
    def upload_pdf(self):
        item = self.urlpdf+self.pdf[4]+".pdf"
        for i in range(4):
            item = item + "\n" + self.urlpdf+self.pdf[5+i]+".pdf"
        item2 = self.urlpdf+self.pdf[0]+".pdf"
        for i2 in range(7):
            item2 = item2 + "\n" + self.urlpdf+self.pdf[1+i2]+".pdf"
        print(item)
        print(item2)
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(item)  # 准备分批的
        sleep(3)
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(item2)
        com_alert().com_equal(self.driver, self.picturePath, print_name="出现冲突", version="取 消")



if __name__ == "__main__":
    case = unittest.TestSuite()
    case.addTest(upload("upload_picture"))
    case.addTest(upload("upload_pdf"))

    fp = open(resultPath+"验证上传.html", "wb")
    runner = HTMLTestRunner(stream=fp, title="test", description="验证上传重名")
    runner.run(case)
    fp.close()












