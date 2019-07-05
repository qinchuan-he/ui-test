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
from common.comfunction import execBrower # 启动浏览器函数
from common.comfunction import user  # 用户登录类
from common.comfunction import comHtml # 生成html报告类

# 上传19种格式并且预览，每个截图

resultpath = "C:\\work\\1测试\\10自动化\\报告\\"
class up_all(unittest.TestCase):
    '''上传19种格式'''
    # 启动浏览器,并且登录
    mode = 1
    driver = execBrower(mode)
    user().login(driver)
    
    # 公共的创建文件夹方法,私有根目录下创建一个文件夹
    el1=driver.find_element_by_xpath("//span[text()='新建']")
    sleep(1)
    ActionChains(driver).move_to_element(el1).perform()
    driver.find_element_by_xpath("//li[text()='新建文件夹']").click()
    folder1=int(time.time())
    print("新建文件夹：%s " %folder1)
    driver.switch_to.active_element.send_keys(folder1)
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    # 进入文件夹
    driver.find_element_by_xpath("//span[text()="+str(folder1)+"]").click()

    #上传office文件
    def upload_office(self):
        '''上传office文件'''
        # 公共参数
        picturePath="C:\\work\\1测试\\10自动化\\截图保存\\19种上传格式截图\\office\\"
        showPath="file:///C:/work/1测试/10自动化/截图保存/19种上传格式截图/office/"

        waitTime=5
        uploadwait= 15 #上传之后的等待时间
        # 上传文件
        # office相关
        fpath = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\office\\"
        word1name = "2017年12月11日-2017年12月15日发行监管部"
        word2name = "带图片表格文档"
        excel1name = "003_模板_TestLink测试用例导入"
        excle2name = "cyprex1.3测试用例"
        pptname = "小z素材-商务炫酷风格动态模板-003"
        # 新建office文件夹，并进入
        el1=self.driver.find_element_by_xpath("//span[text()='新建']")
        sleep(waitTime)
        ActionChains(self.driver).move_to_element(el1).perform()
        self.driver.find_element_by_xpath("//li[text()='新建文件夹']").click()
        office = "office"

        self.driver.switch_to.active_element.send_keys(office)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        print("创建office分类文件夹成功： %s" %office)
        sleep(1)
        self.driver.find_element_by_xpath("//span[text()="+"'"+office+"'"+"]").click()
        # 上传office文件
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(fpath+word1name+".doc")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(fpath+word2name+".docx")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(fpath+excel1name+".xls")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(fpath+excle2name+".xlsx")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(fpath+pptname+".ppt")
        sleep(40)
        self.driver.refresh() #刷新下页面
        # 截图并输出
        date1=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date1+".png")
        comHtml().print_html("office文件列表", picturePath, date1)  # 输出到html报告

        # 预览文件
        #点击
        self.driver.find_element_by_xpath("//span[text()=\'"+word1name+"\']/..").click()
        # 等待加载，准备截图
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
        sleep(1)
        date2=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date2+".png")
        comHtml().print_html(word1name, picturePath, date2)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 3, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//iframe")))

        # 预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+word2name+"\']/..").click()
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
        sleep(1)
        date3=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date3+".png")
        comHtml().print_html(word2name, picturePath, date3)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 3, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//iframe")))

        #预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+excel1name+"\']/..").click()
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
        sleep(1)
        date4=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date4+".png")
        comHtml().print_html(excel1name, picturePath, date4)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 3, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//iframe")))

        # 预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+excle2name+"\']/..").click()
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
        sleep(1)
        date5=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date5+".png")
        comHtml().print_html(excle2name, picturePath, date5)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 3, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//iframe")))

        # 预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+pptname+"\']/..").click()
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
        sleep(5)
        date6=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date6+".png")
        comHtml().print_html(pptname, picturePath, date6)  # 输出到html报告
        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 3, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//iframe")))

        # 返回到格式集合目录
        self.driver.find_element_by_xpath("//a[text()=\'"+str(self.folder1)+"\']").click() 
        print("office上传中的返回路径： %s" %str(self.folder1))

    # 上传图片文件  
    def upload_picture(self):
        '''上传picture文件'''
        # 公共参数
        picturePath="C:\\work\\1测试\\10自动化\\截图保存\\19种上传格式截图\\picture\\"
        showPath="file:///C:/work/1测试/10自动化/截图保存/19种上传格式截图/picture/"

        waitTime=5
        uploadwait= 15 #上传之后的等待时间

        # 上传文件
        # 图片相关

        tpath = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\图片\\"
        jpgname = "timg"
        pngname= "验证图片"
        bmpname = "BMP图片"


        # 新建图片文件夹，并进入
        el1=self.driver.find_element_by_xpath("//span[text()='新建']")
        sleep(waitTime)
        ActionChains(self.driver).move_to_element(el1).perform()
        self.driver.find_element_by_xpath("//li[text()='新建文件夹']").click()
        picture = "图片"

        self.driver.switch_to.active_element.send_keys(picture)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        print("创建picture分类文件夹成功： %s" %picture)
        sleep(1)
        self.driver.find_element_by_xpath("//span[text()="+"'"+picture+"'"+"]").click()
        # 上传picture文件
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(tpath+jpgname+".jpg")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(tpath+pngname+".png")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(tpath+bmpname+".bmp")

        sleep(15)
        self.driver.refresh() #刷新下页面
        # 截图并输出
        date1=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date1+".png")
        comHtml().print_html("图片文件列表", picturePath, date1)  # 输出到html报告

        # 预览文件
        #点击
        self.driver.find_element_by_xpath("//span[text()=\'"+jpgname+"\']/..").click()
        # 等待加载，准备截图
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'PreviewContent_imgViewer')]")))
        # 增加一个点击图片的操作
        self.driver.find_element_by_xpath("//div[contains(@class,'PreviewContent_imgViewer')]/img").click()
        sleep(1)
        date2=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date2+".png")
        comHtml().print_html(jpgname, picturePath, date2)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 3, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'PreviewContent_imgViewer')]")))

        # 预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+pngname+"\']/..").click()
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'PreviewContent_imgViewer')]")))
        sleep(1)
        date3=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date3+".png")
        comHtml().print_html(pngname, picturePath, date3)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 3, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'PreviewContent_imgViewer')]")))

        #预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+bmpname+"\']/..").click()
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'PreviewContent_imgViewer')]")))
        sleep(1)
        date4=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date4+".png")
        comHtml().print_html(bmpname, picturePath, date4)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 3, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'PreviewContent_imgViewer')]")))



        # 返回到格式集合目录
        self.driver.find_element_by_xpath("//a[text()=\'"+str(self.folder1)+"\']").click() 
    def upload_music(self):
        '''上传音频文件'''
        # 公共参数
        picturePath="C:\\work\\1测试\\10自动化\\截图保存\\19种上传格式截图\\music\\"
        showPath="file:///C:/work/1测试/10自动化/截图保存/19种上传格式截图/music/"
        waitTime=5
        uploadwait= 15 #上传之后的等待时间

        # 上传文件
        # 音频
        ypath = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\音频\\"
        pamname = "16k"
        wavname = "筷子兄弟《小苹果》"
        amrname = "另一种格式"
        mp3name = "群星 - 贾谊《过秦论》"
        m4aname = "世纪大道199号"

        # 新建音频文件夹，并进入
        el1=self.driver.find_element_by_xpath("//span[text()='新建']")
        sleep(waitTime)
        ActionChains(self.driver).move_to_element(el1).perform()
        self.driver.find_element_by_xpath("//li[text()='新建文件夹']").click()
        musicfolder = "音频"

        self.driver.switch_to.active_element.send_keys(musicfolder)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        print("创建music分类文件夹成功： %s" %musicfolder)
        sleep(1)
        self.driver.find_element_by_xpath("//span[text()="+"'"+musicfolder+"'"+"]").click()
        # 上传office文件
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(ypath+pamname+".pcm")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(ypath+wavname+".wav")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(ypath+amrname+".amr")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(ypath+mp3name+".mp3")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(ypath+m4aname+".m4a")
        sleep(30)
        self.driver.refresh() #刷新下页面
        # 截图并输出
        date1=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date1+".png")
        comHtml().print_html("音频文件列表", picturePath, date1)  # 输出到html报告

        # 预览文件
        #点击
        self.driver.find_element_by_xpath("//span[text()=\'"+pamname+"\']/..").click()
        sleep(waitTime)
        date2=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date2+".png")
        comHtml().print_html(pamname, picturePath, date2)  # 输出到html报告

        # 预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+wavname+"\']/..").click()
        sleep(waitTime)
        date3=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date3+".png")
        comHtml().print_html(wavname, picturePath, date3)  # 输出到html报告

        #预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+amrname+"\']/..").click()
        sleep(waitTime)
        date4=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date4+".png")
        comHtml().print_html(amrname, picturePath, date4)  # 输出到html报告

        # 预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+mp3name+"\']/..").click()
        sleep(waitTime)
        date5=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date5+".png")
        comHtml().print_html(mp3name, picturePath, date5)  # 输出到html报告

        # 预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+m4aname+"\']/..").click()
        sleep(waitTime)
        date6=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date6+".png")
        comHtml().print_html(m4aname, picturePath, date6)  # 输出到html报告
        # self.driver.quit()
        # 返回到格式集合目录
        self.driver.find_element_by_xpath("//a[text()=\'"+str(self.folder1)+"\']").click()    
    def upload_other(self):
        '''上传其他类型文件'''       
        # 公共参数
        picturePath="C:\\work\\1测试\\10自动化\\截图保存\\19种上传格式截图\\other\\"
        showPath="file:///C:/work/1测试/10自动化/截图保存/19种上传格式截图/other/"

        waitTime=5
        uploadwait= 15 #上传之后的等待时间

        # 上传文件
        # 其他
        qpath="C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\其他\\"
        pdfname = "146页年度报告"
        zipname = "测试解压"
        hmtlname = "厦门亿联网络技术股份有限公司 关于召开 2018 年年度股东大会的通知"
        rarname = "上传文件"
        txtname = "天空1"

        
        # 新建其他文件夹，并进入
        el1=self.driver.find_element_by_xpath("//span[text()='新建']")
        sleep(waitTime)
        ActionChains(self.driver).move_to_element(el1).perform()
        self.driver.find_element_by_xpath("//li[text()='新建文件夹']").click()
        other = "其他"

        self.driver.switch_to.active_element.send_keys(other)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        print("创建office分类文件夹成功： %s" %other)
        sleep(1)
        self.driver.find_element_by_xpath("//span[text()="+"'"+other+"'"+"]").click()
        # 上传other文件
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(qpath+pdfname+".PDF")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(qpath+zipname+".zip")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(qpath+hmtlname+".html")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(qpath+rarname+".rar")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(qpath+txtname+".txt")
        sleep(30)
        self.driver.refresh() #刷新下页面
        # 截图并输出
        date1=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date1+".png")
        comHtml().print_html("其他类型列表", picturePath, date1)  # 输出到html报告

        # 预览文件
        #点击
        self.driver.find_element_by_xpath("//span[text()=\'"+pdfname+"\']/..").click()
        # 等待加载，准备截图
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
        sleep(10)
        date2=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date2+".png")
        comHtml().print_html(pdfname, picturePath, date2)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 5, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//iframe")))

        #预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+hmtlname+"\']/..").click()
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
        sleep(3)
        date4=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date4+".png")
        comHtml().print_html(hmtlname, picturePath, date4)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 5, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//iframe")))

        # 预览下一个
        self.driver.find_element_by_xpath("//div/span[text()=\'"+txtname+"\']/..").click()
        WebDriverWait(self.driver, 15, 0.2).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
        sleep(3)
        date6=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date6+".png")
        comHtml().print_html(txtname, picturePath, date6)  # 输出到html报告
        self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        WebDriverWait(self.driver, 5, 0.2).until_not(ec.presence_of_element_located((By.XPATH, "//iframe")))

        # 预览下一个,处理压缩包
        self.driver.find_element_by_xpath("//div/span[text()=\'"+zipname+"\']/..").click()
        sleep(1)
        date3=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date3+".png")
        comHtml().print_html(zipname, picturePath, date3)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'取 消')]/..").click()

        sleep(1)
        # 预览下一个,处理压缩包
        self.driver.find_element_by_xpath("//div/span[text()=\'"+rarname+"\']/..").click()

        sleep(1)
        date5=str(int(time.time()))
        self.driver.get_screenshot_as_file(picturePath+date5+".png")
        comHtml().print_html(rarname, picturePath, date5)  # 输出到html报告

        self.driver.find_element_by_xpath("//span[contains(text(),'取 消')]/..").click()
        sleep(1)
        # 返回到格式集合目录
        self.driver.find_element_by_xpath("//a[text()=\'"+str(self.folder1)+"\']").click()

if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(up_all("upload_office"))
    testunit.addTest(up_all("upload_picture"))
    testunit.addTest(up_all("upload_music"))
    testunit.addTest(up_all("upload_other"))

    # 生成报告
    fp = open(resultpath+"19种格式上传验证.html", "wb")
    runner = HTMLTestRunner(stream=fp, title="上传预览测试报告", description="私有中19中格式上传和打开")
    runner.run(testunit)
    fp.close()
