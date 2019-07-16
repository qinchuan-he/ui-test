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
from common.comfunction import com_share # 分享按钮点击之后的判断

# 分享功能验证，以PDF文件验证，预览中，边写边搜中，艾玛中（碎片分享），文件夹中（工具栏），文件夹内搜索中，比对报告中分享
# 不包含比对分享
resultpath = "C:\\work\\1测试\\10自动化\\报告\\"


class test_singleFileShare(unittest.TestCase):
    '''分享功能验证'''
    # 公共参数

    picturePath = "C:\\work\\1测试\\10自动化\\截图保存\\19种上传格式截图\\other\\" # 生成截图路径
    showPath = "file:///C:/work/1测试/10自动化/截图保存/19种上传格式截图/other/" # 截图输出路径，目前废弃
    qpath = "C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\19种格式\\其他\\"    # 上传路径
    pdfname = "146页年度报告"    # 上传文件名
    folder12 = "分享"   # 新建的分享文件夹
    # 启动浏览器
    mode = 2
    driver = execBrower(mode)
    user().login(driver)
    driver.implicitly_wait(30)

    # 创建文件夹
    el1 = driver.find_element_by_xpath("//span[text()='新建']")
    sleep(1)
    ActionChains(driver).move_to_element(el1).perform()
    driver.find_element_by_xpath("//li[text()='新建文件夹']").click()
    folder1 = int(time.time())
    print("新建文件夹：%s " % folder1)
    driver.switch_to.active_element.send_keys(folder1)
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    # 进入文件夹
    # driver.find_element_by_xpath("//span[text()="+str(folder1)+"]").click()
    # 检查团队
    team_name = team().check_team(driver)

    # 预览分享
    def test_viewshare(self):
        '''上传并预览分享'''

        self.driver.find_element_by_xpath("//a[contains(@class,'GlobalHeader_logo')]").click()
        self.driver.find_element_by_xpath("//span[text()=" + str(self.folder1) + "]").click()
        # 创建文件夹
        el12 = self.driver.find_element_by_xpath("//span[text()='新建']")
        sleep(1)
        ActionChains(self.driver).move_to_element(el12).perform()
        self.driver.find_element_by_xpath("//li[text()='新建文件夹']").click()

        print("新建文件夹：%s " % self.folder12)
        self.driver.switch_to.active_element.send_keys(self.folder12)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        sleep(1)
        self.driver.find_element_by_xpath("//span[text()=" + "'" + self.folder12 + "'" + "]").click()
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.qpath + self.pdfname + ".PDF")
        sleep(30)
        self.driver.refresh()  # 刷新是为了防止，上传之后没有刷新出来结果
        sleep(2)
        self.driver.find_element_by_xpath("//span[text()='" + self.pdfname + "']/..").click()  # 打开文件预览
        try:
            WebDriverWait(self.driver, 15, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
            self.driver.find_element_by_xpath("//i[@aria-label='图标: share-alt']").click()
            sleep(1)
            # 选择团队,分享
            self.driver.find_element_by_xpath("//span[text()='" + self.team_name + "']/..").click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//span[text()='确 定']/..").click()
            # 截图
            date12 = str(int(time.time()))
            self.driver.get_screenshot_as_file(self.picturePath + date12 + ".png")
            comHtml().print_html("预览分享", self.picturePath, date12)
            # 返回预览
            try:
                WebDriverWait(self.driver, 10, 0.5).until_not(
                    ec.presence_of_element_located((By.XPATH, "//span[text()='分享给团队']")))
                # 兼容版本冲突
                try:
                    WebDriverWait(self.driver, 5, 0.5).until(
                        ec.presence_of_element_located((By.XPATH, "//div[text()='版本冲突']")))
                    # print("找到了")
                    self.driver.find_element_by_xpath("//span[text()='保留两者']/..").click()
                    sleep(0.5)
                except Exception as e:
                    print(e)
                    print("没有版本冲突")
            except Exception as e:
                print(e)
                self.driver.find_element_by_xpath("//span[@class='ant-modal-close-x']").click()
            self.driver.find_element_by_xpath("//span[contains(text(), '返回')]/..").click()
        except Exception as e:
            print(e)
            print("没有打开预览")
        # 截图并输出
        sleep(4)
        date1 = str(int(time.time()))
        self.driver.get_screenshot_as_file(self.picturePath + date1 + ".png")
        comHtml().print_html("预览返回列表截图", self.picturePath, date1)  # 输出到html报告

    # 列表分享
    def test_listShare(self):
        '''列表模式分享'''
        el21 = self.driver.find_element_by_xpath("//span[text()='"+self.pdfname+"']")
        ActionChains(self.driver).move_to_element(el21).perform()
        self.driver.find_element_by_xpath("//input[@class='ant-checkbox-input']").click()
        sleep(0.5)
        try:
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-share-alt']").click()
            sleep(0.5)
            # 选择团队,分享
            self.driver.find_element_by_xpath("//span[text()='" + self.team_name + "']/..").click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//span[text()='确 定']/..").click()
            # 截图
            date12 = str(int(time.time()))
            self.driver.get_screenshot_as_file(self.picturePath + date12 + ".png")
            comHtml().print_html("列表分享", self.picturePath, date12)
            # 检查弹框是否关闭
            try:
                WebDriverWait(self.driver, 10, 0.5).until_not(
                    ec.presence_of_element_located((By.XPATH, "//span[text()='分享给团队']")))
                # 兼容版本冲突
                try:
                    WebDriverWait(self.driver, 5, 0.5).until(
                        ec.presence_of_element_located((By.XPATH, "//div[text()='版本冲突']")))
                    # print("找到了")
                    self.driver.find_element_by_xpath("//span[text()='保留两者']/..").click()
                    sleep(0.5)
                except Exception as e:
                    print(e)
                    print("没有版本冲突")
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

    # 边写边搜中分享
    def test_modifyShare(self):
        '''边写边搜分享'''
        # 新建文件,word
        sleep(0.5)
        el31 = self.driver.find_element_by_xpath("//i[@class='anticon anticon-plus']/..")
        ActionChains(self.driver).move_to_element(el31).perform()
        sleep(0.5)
        self.driver.find_element_by_xpath("//li[text()='新建文档']").click()
        try:
            WebDriverWait(self.driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
            self.driver.find_element_by_xpath("//span[text()='边写边搜']/..").click()
            self.driver.find_element_by_xpath(
                "//input[@placeholder='搜文件，也可以通过“#”搜标签']").send_keys(self.pdfname)
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)
            # 等待加载,根据搜索字段必有结果，所以判断结果数
            for i in range(10):
                el30 = self.driver.find_element_by_xpath("//span[contains(text(),'搜索结果数量：')]")
                count = int(re.findall("[0-9]+", el30.text)[0])
                if count > 0:
                    break
                else:
                    # print("休眠第 %d 次" % i)
                    sleep(1)
            el31 = self.driver.find_element_by_xpath("//span[text()='私有'][1]/..")
            ActionChains( self.driver).move_to_element(el31).perform()
            el33 = self.driver.find_elements_by_xpath("//i[@class='anticon anticon-share-alt']/..")
            el33[1].click()
            sleep(1)
            self.driver.find_element_by_xpath("//span[text()='验证的团队']/..").click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//span[text()='确 定']/..").click()
            # 截图
            date31=str(int(time.time()))
            self.driver.get_screenshot_as_file(self.picturePath+date31+".png")
            comHtml().print_html("边写边搜列表分享", self.picturePath, date31)
            # 检查弹框是否关闭
            try:
                WebDriverWait(self.driver, 10, 0.5).until_not(
                    ec.presence_of_element_located((By.XPATH, "//span[text()='分享给团队']")))
                # 兼容版本冲突
                try:
                    WebDriverWait(self.driver, 5, 0.5).until(
                        ec.presence_of_element_located((By.XPATH, "//div[text()='版本冲突']")))
                    # print("找到了")
                    self.driver.find_element_by_xpath("//span[text()='保留两者']/..").click()
                    sleep(0.5)
                except Exception as e:
                    print(e)
                    print("没有版本冲突")
                ActionChains( self.driver).move_to_element(el31).perform()
                sleep(0.5)
                el34 = self.driver.find_elements_by_xpath(
                    "//span[text()='私有'][1]/../../../../../../../h4//i[@class='anticon anticon-arrows-alt']/..")
                el34[0].click()
                # 检查是否展开
                try:
                    WebDriverWait(self.driver, 10, 0.5).until(
                        ec.presence_of_element_located((By.XPATH, "//div[text()='边写边搜']")))
                    sleep(1)
                    el35 = self.driver.find_elements_by_xpath("//i[@class='anticon anticon-more']")
                    ActionChains(self.driver).move_to_element(el35[1]).perform()  # 第一个图标是边写边搜那栏的，这里是第二个
                    self.driver.find_element_by_xpath("//li[text()='分享']").click()
                except Exception as e:
                    print(e)

            except Exception as e:
                print(e)
                print("弹框关闭出现异常")

        except Exception as e:
            print(e)

    # # 文件夹内搜索分享
    # def test_folderSearchShare(self):
    #     '''文件夹内搜索分享'''
    #     # 搜索文件



if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(test_singleFileShare("test_viewshare"))
    testunit.addTest(test_singleFileShare("test_listShare"))

    fp = open(resultpath + "分享验证.html", "wb")
    runner = HTMLTestRunner(stream=fp, title="分享功能测试报告", description="分享功能回归验证")
    runner.run(testunit)
    fp.close()



