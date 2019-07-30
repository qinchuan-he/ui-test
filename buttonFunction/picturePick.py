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

#  验证图例表格提取和同句搜索，图例提取有三个操作（数据组），新增，更新，复制
# 1.新建word，插入图片，然后文件夹内搜索word，（第一步更新验证）----新建word用例中
# 2.文件夹内搜索中分享word，刷新文件夹内搜索（第二步复制验证）----新建word用例中
# 3.团队中上传word，并且打开预览（第三步新增验证）,并且验证同句搜索
# 4.团队中上传word（纯矢量图），并且打开预览（验证矢量图的提取）
# 5.团队中上传PDF，并且打开预览（验证PDF图片的提取）,并且验证同句搜索

class test_Pick(unittest.TestCase):
    '''图例表格提取验证和同句验证'''
    #  公共参数
    picturePath = "C:\\work\\1测试\\10自动化\\截图保存\\图例\\"  # 生成截图路径
    uploadPath = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\图例提取文件\\"  # 上传路径
    wordTextName = "表格图片"   # 后缀是doc
    wordvectorName = "纯矢量图"   # 后缀是docx
    pdfName = "验证图例文件"  # 后缀是pdf
    texturl = uploadPath+wordTextName+".doc"
    vectorurl = uploadPath+wordvectorName+".docx"
    pdfurl = uploadPath+pdfName+".pdf"
    folder = str(time.time())
    searchTxt = "行业，投资"
    searchTxt1 = "行业"
    searchvector = ""
    searchPdf = "公司，报告"
    searchPdf1 = "报告"
    page_redirect = "4"  # 跳页
    page_redirect_error = "none" # 输入非数字的跳页
    table_word = "蓝帆医疗股份有限公司"
    table_pdf = "股票上市交易所"

    # 启动浏览器并登陆
    mode = 1
    driver = execBrower(mode)
    user().login(driver)
    team_name = team().check_team(driver)

    #  上传文件并预览
    def test_textPick(self):
        '''非矢量图的提取'''
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.texturl)
        version = "以新版本覆盖"
        print_name = "图例上传文件"
        com_alert().com_equal(self.driver, self.picturePath, print_name, version)
        sleep(20)
        try:
            WebDriverWait(self.driver, 20, 0.5).until(ec.element_to_be_clickable((By.XPATH, "//span[text()='"+self.wordTextName+"']/..")))
            self.driver.find_element_by_xpath("//span[text()='"+self.wordTextName+"']/..").click()
            try:
                WebDriverWait(self.driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
                # 查看图例
                try:
                    WebDriverWait(self.driver, 5, 0.5).until(ec.presence_of_element_located((
                        By.XPATH, "//div[contains(@class,'PreviewContent_imgButton')]")))
                    self.driver.find_element_by_xpath("//div[contains(@class,'PreviewContent_imgButton')]").click()
                    sleep(0.5)
                    el12 = self.driver.find_element_by_xpath("//div[contains(@class,'FileImages_imageBox')]")
                    ActionChains(self.driver).move_to_element(el12).perform()
                    sleep(0.5)
                    self.driver.find_element_by_xpath("//div[contains(@class,'FileImages_imageAction')]").click()
                    sleep(0.5)
                    self.driver.find_element_by_xpath("//span[text()='取 消']/..").click() # 验证取消弹框
                    # 再次加入
                    sleep(0.5)
                    el12.click()
                    # ActionChains(self.driver).move_to_element(el12).perform()
                    sleep(0.5)
                    self.driver.find_element_by_xpath("//div[contains(@class,'FileImages_imageAction')]").click()
                    name = "预览加入碎片"
                    print_name = "图例定位和加入碎片"
                    button = "确 定"
                    com_alert().com_addFrager(self.driver, name, self.picturePath, print_name, button)
                    sleep(0.5)
                    self.driver.find_element_by_xpath("//i[@class='anticon anticon-close']").click()
                except Exception as e:
                    print(e)
                    print_name = "没有提取到图例"
                    datename13 = str(time.time())
                    self.driver.get_screenshot_as_file(self.picturePath+datename13+".png")
                    comHtml().print_html(print_name, self.picturePath, datename13)
                iframe_id = self.driver.find_element_by_xpath("//iframe").get_attribute("id")
                self.driver.switch_to.frame(iframe_id)
                el13 = self.driver.find_element_by_xpath("//input[@id='searchstr']")
                # 搜索单个关键字
                el13.send_keys(self.searchTxt1)
                self.driver.switch_to.active_element.send_keys(Keys.ENTER)
                comHtml().screen_shot(self.driver, self.picturePath, print_name="单关键字截图")
                sleep(0.5)
                # 搜索多关键字
                el13.send_keys(self.searchTxt)
                self.driver.switch_to.active_element.send_keys(Keys.ENTER)
                comHtml().screen_shot(self.driver, self.picturePath, print_name="多关键字截图")
                sleep(0.5)
                # 点击同句
                self.driver.find_element_by_xpath("//input[@class='checkbox']").click()
                comHtml().screen_shot(self.driver, self.picturePath, print_name="同句截图")
                sleep(0.5)
                self.driver.find_element_by_xpath("//input[@id='same_sen']").click()
                comHtml().screen_shot(self.driver, self.picturePath, print_name="关闭同句截图")
                sleep(0.5)
                # 清空搜索内容
                self.driver.find_element_by_xpath("//span[@id='searchBtn']").click()
                comHtml().screen_shot(self.driver, self.picturePath, print_name="清空搜索内容")
                sleep(0.5)
                try:
                    # 纯文本查看
                    self.driver.switch_to.default_content()
                    WebDriverWait(self.driver, 1, 0.5).until_not(
                        ec.presence_of_element_located((
                            By.XPATH, "//label[@class='ant-radio-button-wrapper ant-radio-button-wrapper-disabled']")))
                    self.driver.find_element_by_xpath("//span[text()='纯文本']/..").click()
                    comHtml().screen_shot(self.driver, self.picturePath, print_name="纯文本查看")
                    # 切换回原格式
                    self.driver.find_element_by_xpath("//span[text()='原格式']/..").click()
                    self.driver.switch_to.frame(iframe_id)
                    sleep(0.5)
                except Exception as e:
                    print(e)
                    comHtml().screen_shot(self.driver, self.picturePath, print_name="没有纯文本")
                # 验证表格提取
                el14 = self.driver.find_element_by_xpath("//span[text()='"+self.table_word+"']")
                ActionChains(self.driver).move_to_element(el14).perform()
                comHtml().screen_shot(self.driver, self.picturePath, print_name="表格抽取验证")
                el14.click()
                ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
                comHtml().screen_shot(self.driver, self.picturePath, print_name="滚动验证")
                self.driver.switch_to.default_content()
                self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
                sleep(0.5)
                comHtml().screen_shot(self.driver, self.picturePath, print_name="退出预览")
                sleep(2)
            except Exception as e:
                print(e)
                printName = "预览异常"
                datename12 = str(time.time())
                self.driver.get_screenshot_as_file(self.picturePath + datename12 + ".png")
                comHtml().print_html(printName, self.picturePath, datename12)
                self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
                sleep(2)
        except Exception as e:
            print(e)
            printName = "上传异常"
            datename12 = str(time.time())
            self.driver.get_screenshot_as_file(self.picturePath+datename12+".png")
            comHtml().print_html(printName, self.picturePath, datename12)

    def test_vectorPick(self):
        '''矢量图提取提取'''
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.vectorurl)
        version = "以新版本覆盖"
        print_name = "图例上传文件"
        com_alert().com_equal(self.driver, self.picturePath, print_name, version)
        sleep(20)
        try:
            WebDriverWait(self.driver, 2, 0.5).until(
                ec.element_to_be_clickable((By.XPATH, "//span[text()='"+self.wordvectorName+"']/..")))
            self.driver.find_element_by_xpath("//span[text()='"+self.wordvectorName+"']/..").click()
            try:
                WebDriverWait(self.driver, 5, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
                try:
                    WebDriverWait(self.driver, 2, 0.5).until(
                        ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'PreviewContent_imgButton')]")))
                    self.driver.find_element_by_xpath("//div[contains(@class,'PreviewContent_imgButton')]").click()
                    sleep(0.5)
                    el12 = self.driver.find_element_by_xpath("//div[contains(@class,'FileImages_imageBox')]")
                    ActionChains(self.driver).move_to_element(el12).perform()
                    sleep(0.5)
                    self.driver.find_element_by_xpath("//div[contains(@class,'FileImages_imageAction')]").click()
                    sleep(0.5)
                    self.driver.find_element_by_xpath("//span[text()='取 消']/..").click()  # 验证取消弹框
                    # 再次加入
                    sleep(0.5)
                    el12.click()
                    sleep(0.5)
                    self.driver.find_element_by_xpath("//div[contains(@class,'FileImages_imageAction')]").click()
                    name = "预览中--加入。，碎片"
                    print_name = "图例定位和加入碎片"
                    button = "确 定"
                    com_alert().com_addFrager(self.driver, name, self.picturePath, print_name, button)
                    sleep(0.5)
                    self.driver.find_element_by_xpath("//i[@class='anticon anticon-close']").click()
                except Exception as e:
                    print(e)
                    comHtml().screen_shot(self.driver, self.picturePath, print("未提取出图例"))
                self.driver.find_element_by_xpath("//span[contains(text(), '返回')]/..").click()
                sleep(2)
            except Exception as e:
                print(e)
                comHtml().screen_shot(self.driver, self.picturePath, print_name="预览异常")
                self.driver.find_element_by_xpath("//span[contains(text(), '返回')]/..").click()
                sleep(2)
        except Exception as e:
            print(e)
            comHtml().screen_shot(self.driver, self.picturePath, print_name="上传异常")
    def test_pdfPick(self):
        '''PDF图例提取，同句，翻页'''
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.pdfurl)
        version = "以新版本覆盖"
        print_name = "图例上传文件"
        com_alert().com_equal(self.driver, self.picturePath, print_name, version)
        sleep(20)
        try:
            WebDriverWait(self.driver, 3, 0.5).until(
                ec.element_to_be_clickable((By.XPATH, "//span[text()='"+self.pdfName+"']/..")))
            self.driver.find_element_by_xpath("//span[text()='"+self.pdfName+"']/..").click()
            try:
                WebDriverWait(self.driver, 5, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
                try:
                    WebDriverWait(self.driver, 5, 0.5).until(ec.presence_of_element_located((
                        By.XPATH, "//div[contains(@class,'PreviewContent_imgButton')]")))
                    self.driver.find_element_by_xpath("//div[contains(@class,'PreviewContent_imgButton')]").click()
                    sleep(0.5)
                    el12 = self.driver.find_element_by_xpath("//div[contains(@class,'FileImages_imageBox')]")
                    ActionChains(self.driver).move_to_element(el12).perform()
                    sleep(0.5)
                    self.driver.find_element_by_xpath("//div[contains(@class,'FileImages_imageAction')]").click()
                    sleep(0.5)
                    self.driver.find_element_by_xpath("//span[text()='取 消']/..").click() # 验证取消弹框
                    # 再次加入
                    sleep(0.5)
                    el12.click()
                    # ActionChains(self.driver).move_to_element(el12).perform()
                    sleep(0.5)
                    self.driver.find_element_by_xpath("//div[contains(@class,'FileImages_imageAction')]").click()
                    name = "previewjoinfrage"
                    print_name = "图例定位和加入碎片"
                    button = "确 定"
                    com_alert().com_addFrager(self.driver, name, self.picturePath, print_name, button)
                    sleep(0.5)
                    self.driver.find_element_by_xpath("//i[@class='anticon anticon-close']").click()
                except Exception as e:
                    print(e)
                    print_name = "没有提取到图例"
                    datename13 = str(time.time())
                    self.driver.get_screenshot_as_file(self.picturePath+datename13+".png")
                    comHtml().print_html(print_name, self.picturePath, datename13)
                iframe_id = self.driver.find_element_by_xpath("//iframe").get_attribute("id")
                self.driver.switch_to.frame(iframe_id)
                el13 = self.driver.find_element_by_xpath("//input[@id='searchstr']")
                # 搜索单个关键字
                el13.send_keys(self.searchPdf1)
                self.driver.switch_to.active_element.send_keys(Keys.ENTER)
                comHtml().screen_shot(self.driver, self.picturePath, print_name="单关键字截图")
                sleep(0.5)
                # 搜索多关键字
                el13.send_keys(self.searchPdf)
                self.driver.switch_to.active_element.send_keys(Keys.ENTER)
                comHtml().screen_shot(self.driver, self.picturePath, print_name="多关键字截图")
                sleep(0.5)
                # 点击同句
                self.driver.find_element_by_xpath("//input[@class='checkbox']").click()
                comHtml().screen_shot(self.driver, self.picturePath, print_name="同句截图")
                sleep(0.5)
                self.driver.find_element_by_xpath("//input[@id='same_sen']").click()
                comHtml().screen_shot(self.driver, self.picturePath, print_name="关闭同句截图")
                sleep(0.5)
                # 翻页，上一页，上一页
                el31 = self.driver.find_element_by_xpath("//span[@class='arrow-left']")
                el31.click()
                el31.click()
                comHtml().screen_shot(self.driver, self.picturePath, print_name="上一页上一页")
                sleep(0.5)
                # 翻页，下一页，下一页
                el32 = self.driver.find_element_by_xpath("//span[@class='arrow-right']")
                el32.click()
                el32.click()
                comHtml().screen_shot(self.driver, self.picturePath, print_name="下一页下一页")
                sleep(0.5)
                # 跳页，4
                el33 = self.driver.find_element_by_xpath("//input[@id='current_page']")
                # el33.click()
                # el33.clear()
                ActionChains(self.driver).double_click(el33).perform()
                el33.send_keys(self.page_redirect)
                self.driver.switch_to.active_element.send_keys(Keys.ENTER)
                comHtml().screen_shot(self.driver, self.picturePath, print_name="跳到第四页")
                sleep(0.5)
                el33.click()
                el33.clear()
                el33.send_keys(self.page_redirect_error)
                self.driver.switch_to.active_element.send_keys(Keys.ENTER)
                comHtml().screen_shot(self.driver, self.picturePath, print_name="输入非数字")
                sleep(0.5)
                # 清空搜索内容
                self.driver.find_element_by_xpath("//span[@id='searchBtn']").click()
                comHtml().screen_shot(self.driver, self.picturePath, print_name="清空搜索内容")
                sleep(0.5)
                try:
                    # 纯文本查看
                    self.driver.switch_to.default_content()
                    WebDriverWait(self.driver, 1, 0.5).until_not(
                        ec.presence_of_element_located((
                            By.XPATH, "//label[@class='ant-radio-button-wrapper ant-radio-button-wrapper-disabled']")))
                    self.driver.find_element_by_xpath("//span[text()='纯文本']/..").click()
                    comHtml().screen_shot(self.driver, self.picturePath, print_name="纯文本查看")
                    # 切换回原格式
                    self.driver.find_element_by_xpath("//span[text()='原格式']/..").click()
                    self.driver.switch_to.frame(iframe_id)
                    sleep(0.5)
                except Exception as e:
                    print(e)
                    comHtml().screen_shot(self.driver, self.picturePath, print_name="没有纯文本")
                # 验证表格提取
                el14 = self.driver.find_element_by_xpath("//div[text()='"+self.table_pdf+"']")
                ActionChains(self.driver).move_to_element(el14).perform()
                comHtml().screen_shot(self.driver, self.picturePath, print_name="表格抽取验证")
                # 滚动验证
                el14.click()
                ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
                comHtml().screen_shot(self.driver, self.picturePath, print_name="滚动验证")
                self.driver.switch_to.default_content()
                self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
                sleep(0.5)
                comHtml().screen_shot(self.driver, self.picturePath, print_name="退出预览")
                sleep(2)
            except Exception as e:
                print(e)
                comHtml().screen_shot(self.driver, self.picturePath, print_name="预览异常")
                self.driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
                sleep(2)
        except Exception as e:
            print(e)
            comHtml().screen_shot(self.driver, self.picturePath, print_name="上传异常")






if __name__ == "__main__":
    testCase = unittest.TestSuite()
    testCase.addTest(test_Pick("test_textPick"))
    testCase.addTest(test_Pick("test_vectorPick"))
    testCase.addTest(test_Pick("test_pdfPick"))

    fp = open(resultPath+"图例提取验证.html", 'wb')
    runner = HTMLTestRunner(stream=fp, title="图例验证报告", description="图例，和对应文件同句验证")
    runner.run(testCase)
    fp.close()




