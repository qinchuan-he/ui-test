# coding=utf-8
import io
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# from PIL import Image # 图像处理
# from PIL import ImageChops # 图像处理
# from PIL.PngImagePlugin import PngImageFile
from time import sleep
import time  # 生成时间戳用
import os  # 上传autoit用
# 发送邮件
import smtplib
from email.mime.text import MIMEText  # 正文
from email.header import Header  # 头部
from email.mime.multipart import MIMEMultipart  # 上传附件用
from common.private import EmailProperty
from common.private import UserProperty

# 服务器上传
# import paramiko

# 公共参数
url = UserProperty().url
user = UserProperty().user
pwd = UserProperty().pwd



driver_new = None
# 启动浏览器
def OpenBrowser(mode,overtime=None):

    global driver_new  # 2020-04-30,关键字驱动增加
    opt = Options()
    opt.add_argument('--disable--gpu')
    opt.add_argument('--headless')
    opt.add_argument('--no-sandbox')
    opt.add_argument("--auto-open-devtools-for-tabs")
    path = UserProperty().BROWER_PATH
    if mode == 1:
        driver = webdriver.Chrome(options=opt, executable_path=path)
    else:
        driver = webdriver.Chrome(path)
    driver.set_window_size(1400, 900)  # 设置窗口大小

    if overtime:
        pass
    else:
        driver.implicitly_wait(30)
    sleep(1)
    driver_new = driver
    return driver

def CloseBrowsers(driver=None):
    """ 关闭浏览器"""
    global driver_new
    if not driver:
        driver=driver_new
    driver.quit()

# 设置上传文件、报告、截图的根路径
def com_path():
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # folder_path = root_path+"\\自动化验证文档\\"   # 2020/01/09调整，这个路径不适用
    folder_path = os.path.join(root_path,"自动化验证文档")
    return folder_path



# 登录相关
class User:
    # 登录
    global driver_new
    def login(self,driver=None,new_user=None):
        if not driver:
            driver=driver_new
        driver.get(url)
        # 2023-01-28 调整，目前首页默认微信登录，需要点按钮跳转到账号登录
        # driver.find_element_by_xpath("//span[text()='账号登录']/..").click()
        driver.find_elements_by_xpath("//span[text()='账号登录']/..")[0].click()
        if new_user:
            driver.find_element_by_id("username_no").send_keys(new_user)
        else:
            driver.find_element_by_id("username_no").send_keys(user)
        driver.find_element_by_id("password").send_keys(pwd)
        # 2023-01-28 调整，增加同意隐私政策
        sleep(0.5)
        driver.find_elements_by_xpath("//input[@id='agreement']")[0].click()
        sleep(0.5)
        el = driver.find_elements_by_xpath("//span[text()='登 录']/..")
        el[0].click()
        # sleep(1.5)
        # driver.find_element_by_xpath("//a[text()='私有资料']").click()
        # User().root_private(driver)
        # WebDriverWait(driver, 10, 0.2).until(ec.presence_of_element_located((By.XPATH, "//span[text()='笔记摘录']")))
        # 2023-01-28 调整，由于增加了首次登录提示，这里点击提示
        sleep(3)
        driver.find_elements_by_xpath("//span[text()='我已知晓']/..")[0].click()

    def login2(self,driver=None,new_user=None,password=None):
        """ 登录错误使用"""
        if not driver:
            driver=driver_new
        if not password:
            password = pwd
        driver.get(url)
        driver.find_element_by_xpath("//span[text()='账号登录']").click()
        if new_user:
            driver.find_element_by_id("username_no").send_keys(new_user)
        else:
            driver.find_element_by_id("username_no").send_keys(user)
        driver.find_element_by_id("password").send_keys(password)
        el = driver.find_elements_by_xpath("//span[text()='登 录']/..")
        el[1].click()


    # 退出登录
    def login_out(self,driver):
        el = com_xpath().com_head(driver, buttonType='Portrait')
        el.click()
        sleep(0.5)
        driver.find_element_by_xpath("//li[text()='退出']").click()

    #  创建文件夹 2023-01-29调整，增加一个参数，判断如果文件夹已存在就进入文件夹
    def createFolder(self, driver=None, folder=None, exist=None):
        if not driver:
            driver=driver_new
        sleep(0.5)
        # 2023-01-28调整，由于修改了默认页，需要增加一步，进入我的资料
        driver.find_element_by_xpath("//span[text()='我的资料']/..").click()
        createType = "create"
        el11 = com_xpath().com_listButton(driver, createType)
        ActionChains(driver).move_to_element(el11).perform()
        driver.find_element_by_xpath("//div[text()='文件夹']/..").click()
        sleep(0.5)
        if folder:
            driver.switch_to.active_element.send_keys(folder)
        else:
            driver.switch_to.active_element.send_keys(str(time.time()))
        sleep(0.5)
        driver.switch_to.active_element.send_keys(Keys.ENTER)
        sleep(0.5)

    # 创建文件,传入文件名，文件类型名称（笔记文档等名字）
    def create_file(self, driver=None, file_type=None):
        global driver_new
        if not driver:
            driver = driver_new
        button = 'create'
        el1 = com_xpath().com_listButton(driver, button)
        ActionChains(driver).move_to_element(el1).perform()  # 移动光标到新建
        driver.find_element_by_xpath("//div[text()='"+file_type+"']/..").click()
        sleep(0.5)
        # 下面的等待2023-01-31注释，由于新建文件是新开页，已经无法通过iframe检测到了，当前聚焦的还是原页面
        # WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))  # 等待20秒，每隔0.5秒检测一次是否有iframe
        sleep(0.5)
        # frame = driver.find_element_by_xpath("//iframe")
        # driver.switch_to.frame(frame)
        # sleep(0.5)
        # driver.switch_to.active_element.send_keys("我是一个验证文件")

    # 返回私有资料根目录
    def root_private(self, driver=None):
        global driver_new
        if not driver:
            driver = driver_new
        sleep(0.5)
        driver.find_elements_by_xpath("//i[contains(@class,'anticon')]")[0].click()
        sleep(0.5)

        # driver.find_element_by_xpath("//span[text()='我的资料']/..").click()  # 2023-01-31 注释，目前点击左上角自动到我的资料，无需再次点击
        sleep(0.5)

    # 导航栏模块切换,传入切换的名称
    def switch_navigation(self,driver,name):
        sleep(0.5)
        try:
            driver.find_element_by_xpath("//a[text()='"+name+"']").click()
        except Exception as e:
            print("没有权限开启模块")
        sleep(0.5)

    # 进入文件和文件,目前就点击最近的,类型和位置目前不需要
    def into_folder(self,driver,button_name,type=None,position=None):
        """ 根据type来切换文件夹和文件，目前不需要区分"""
        sleep(0.5)
        el = driver.find_elements_by_xpath("//span[text()='"+button_name+"']/..")
        el[0].click()


# 生成html相关的类
class comHtml:
    def print_html(self, picname, picpath, picid):  # 就是传入名称，路径，picid就是时间
        # 增加对于绝对路径的处理，处理之后本地不能打开查看图片了
        picpath = "\Cyprex-ui" + picpath.split("Cyprex-ui", 2)[1]  # 注释掉之后本地打开html可以了
        print(
            "<a href = \"javascript:void(0)\" onclick = \"document.getElementById(\'" + picid + "\').style.display='block';document.getElementById('fade').style.display='block'\">" + picname + "预览</a>"
            + "<div id=\"" + picid + "\" class=\"white_content\">"
            + "<a href = \"javascript:void(0)\" onclick = \"document.getElementById(\'" + picid + "\').style.display='none';document.getElementById('fade').style.display='none'\" style=\"align-content: center\">点这里关闭</a>"
            + "<img height=\"800\" width=\"1400\" src=\"" + picpath + picid + ".png" + "\">"
            + "</div>"
            + "<div id=\"fade\" class=\"black_overlay\"></div>")

    # 屏幕截图screenshot
    def screen_shot(self, driver, pic_path, print_name):
        datename = str(time.time())
        driver.get_screenshot_as_file(pic_path + datename + ".png")
        comHtml().print_html(print_name, pic_path, datename)


# 团队相关功能，2019/09/29调整，增加点击团队兼容
class team:
    def check_team(self, driver,team_name=None):
        '''检查团队是否存在,不存在就创建，目前没有判断5个团队的情况的'''
        sleep(0.5)
        driver.find_element_by_xpath("//div[contains(@class,'GlobalHeader_logo')]").click()
        sleep(1)
        driver.find_element_by_xpath("//a[text()='协作共享']").click()
        if team_name==None:
            team_name = "验证的团队"
        try:
            WebDriverWait(driver, 2, 0.5).until(ec.presence_of_element_located((By.XPATH, "//span[text()='"+team_name+"']")))
            driver.find_element_by_xpath("//span[text()='"+team_name+"']").click()  # 修改规则为新建之后直接进去
        except Exception as e:
            print("团队不存在准备新建")
            driver.find_element_by_xpath("//span[text()='创建新项目']/..").click()
            driver.find_element_by_xpath("//input[@placeholder='请输入项目名称']").send_keys(team_name)
            # driver.find_element_by_xpath("//span[text()='确 定']/..").click()
            sleep(1)
            driver.find_element_by_xpath("//div[@class='ant-modal-footer']/div/button[2]").click()
            sleep(1)
            print(e)
        sleep(0.5)
        return team_name

    # 创建第二团队，在第一团队基础上
    def check_team2(self, driver):
        '''团队内分享用'''
        sleep(0.5)
        driver.find_element_by_xpath("//div[contains(@class,'GlobalHeader_logo')]").click()
        sleep(1)
        driver.find_element_by_xpath("//a[text()='协作共享']").click()
        team_name = "分享团队"
        try:
            WebDriverWait(driver, 2, 0.5).until(ec.presence_of_element_located((By.XPATH, "//span[text()='分享团队']")))
        except Exception as e:
            print("团队不存在准备新建")
            driver.find_element_by_xpath("//span[text()='创建新项目']/..").click()
            driver.find_element_by_xpath("//input[@placeholder='请输入项目名称']").send_keys(team_name)
            # driver.find_element_by_xpath("//span[text()='确 定']/..").click()
            sleep(1)
            driver.find_element_by_xpath("//div[@class='ant-modal-footer']/div/button[2]").click()
            sleep(1)
            print(e)
        try:
            driver.find_element_by_xpath("//span[text()='分享团队']").click()  #  修改规则为新建之后直接进去
        except Exception as e:
            pass
        sleep(0.5)
        return team_name

    # 删除团队
    def dismiss_team(self,driver,team_name):
        """
        解散团队方法
        :param driver:
        :param team_name:
        :return:
        """
        User().switch_navigation(driver, name="智能编写")
        sleep(1)
        try:
            WebDriverWait(driver, 3, 0.5).until(ec.presence_of_element_located((By.XPATH, "//span[text()='"+team_name+"']")))
            el = driver.find_element_by_xpath("//span[text()='"+team_name+"']")
            ActionChains(driver).move_to_element(el).perform()
            sleep(0.5)
            # el2 = com_xpath().com_listmoreActions(driver,team_name)
            # el2.click()
            com_xpath().com_listmoreActions(driver,team_name)
            sleep(0.5)
            # el3 = com_xpath().com_listmoreButton(driver,"解散项目")
            # el3.click()
            com_xpath().com_listmoreButton(driver, "解散项目")
            sleep(0.5)
            driver.find_element_by_xpath("//span[text()='确 定']/..").click()
            sleep(15)
        except Exception as e:
            print(e)
            print("团队不存在或别的原因")


    # 团队根目录创建协作空间，自动进入协作空间
    def create_cooperation(self,driver,spacename):
        """
        团队根目录创建协作空间
        :param driver:
        :return:
        """
        el = com_xpath().com_listButton(driver, button="createSpace")
        el.click()
        sleep(0.5)
        driver.find_element_by_xpath("//input[@placeholder='请输入分工协作空间名称']").send_keys(spacename)
        sleep(0.5)
        driver.find_element_by_xpath("//span[text()='确 定']/..").click() # 自动进入空间
        sleep(0.5)








# 分享，公共方法,这个方法不带批注关联权限--->>>点击了分享按钮之后调用这个方法
def com_share(team_name, version, print_name, pic_path, driver):  # 分别是团队名字，冲突覆盖方式，截图的图片汉字名字,driver
    sleep(1)
    # 选择团队,分享
    driver.find_element_by_xpath("//span[text()='" + team_name + "']/..").click()
    sleep(0.5)
    driver.find_element_by_xpath("//span[text()='确 定']/..").click()
    # 截图
    datename = str(time.time())
    driver.get_screenshot_as_file(pic_path + datename + ".png")
    comHtml().print_html(print_name, pic_path, datename)
    # 检查弹框是否关闭
    try:
        WebDriverWait(driver, 10, 0.5).until_not(
            ec.presence_of_element_located((By.XPATH, "//span[text()='分享给项目组']")))
        # 兼容版本冲突
        try:
            WebDriverWait(driver, 10, 0.5).until(
                ec.presence_of_element_located((By.XPATH, "//div[text()='版本冲突']")))
            # print("找到了")
            driver.find_element_by_xpath("//span[text()='" + version + "']/..").click()
            sleep(0.5)
        except Exception as e:
            print(e)
            print("没有版本冲突")
    except Exception as e:
        print(e)


# 上传文件,冲突弹框公共方法,传入截图路径，上传路径，html输出名字，冲突处理方法。包含截图输出搭配html
def com_upload(version, print_name, pic_path, uploadUrl, driver):
    driver.find_element_by_xpath("//input[@type='file']").send_keys(uploadUrl)
    sleep(2)
    datename = str(time.time())
    driver.get_screenshot_as_file(pic_path + datename + ".png")
    comHtml().print_html(print_name, pic_path, datename)
    try:
        # self.driver.find_element_by_xpath("//div[text()='版本冲突']")
        WebDriverWait(driver, 3, 0.5).until(ec.presence_of_element_located((By.XPATH, "//div[text()='版本冲突']")))
        driver.find_element_by_xpath("//span[text()='" + version + "']/..").click()
    except Exception as e:
        print(e)
        print("--没有冲突--")
    sleep(30)


def com_upload_min(version, print_name, pic_path, uploadUrl, driver):
    driver.find_element_by_xpath("//input[@type='file']").send_keys(uploadUrl)
    sleep(1)
    datename = str(time.time())
    driver.get_screenshot_as_file(pic_path + datename + ".png")
    comHtml().print_html(print_name, pic_path, datename)
    try:
        # self.driver.find_element_by_xpath("//div[text()='版本冲突']")
        WebDriverWait(driver, 1.5, 0.5).until(ec.presence_of_element_located((By.XPATH, "//div[text()='版本冲突']")))
        driver.find_element_by_xpath("//span[text()='" + version + "']/..").click()
    except Exception as e:
        print(e)
        print("--没有冲突--")
    sleep(5)


#  公共的弹窗类，所有弹窗相关的封装都放这里，20190809优化，控制传参
class com_alert(object):
    #  点击按钮之后的冲突弹框公共方法，传入截图存放路径，html输出名字，冲突处理方法。包含截图输出搭配html
    def com_equal(self, driver, pic_path=None, print_name=None, version=None):
        #  第一步，截图，并且输出到html
        sleep(2)
        if pic_path and print_name:
            datename = str(time.time())

            driver.get_screenshot_as_file(pic_path + datename + ".png")
            comHtml().print_html(print_name, pic_path, datename)
        #  第二步，判断是否有弹框
        try:
            WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, "//div[text()='版本冲突']")))
            # 2019/09/29增加兼容，原格式打开PDF，弹框遮罩问题
            try:
                el1 = driver.find_element_by_xpath("//div[@class='ant-modal-content']")
                el1 = driver.find_element_by_xpath("//section[contains(@class,'GlobalSearchPage_hideContent')]")
                # addAttribute(driver, el1, 'style', 'display:none')
                addAttribute(driver, el1, 'style', 'opacity:0')
            except Exception as e:
                pass
            driver.find_element_by_xpath("//span[text()='" + version + "']/..").click()
        except Exception as e:
            print(e)
            print("--没有冲突--")
        sleep(0.5)

    #  比对弹框,选中并且截图
    def com_alertCompare(self, driver, folder, file, pic_path, print_name):
        sleep(1)
        try:
            WebDriverWait(driver, 5, 0.5).until(
                ec.presence_of_element_located((By.XPATH, "//div[@class='ant-modal-title']")))
            # 目前弹框有问题，增加兼容
            try:
                print('folder：'+folder)
                driver.find_element_by_xpath("//span[text()='" + folder + "']/../../..").click()
            except Exception as e:
                print("弹框中文件名显示有问题，截图")
                print(e)
                # 219/09/25 去掉兼容
                # print("文件夹名： %s" % folder)
                # folder2 = folder.split(".", 2)[0]
                # driver.find_element_by_xpath("//span[contains(text(),'" + folder2 + "')]/../../..").click()
                # print_name1 = "弹窗截图"
                # datename = str(time.time())
                # driver.get_screenshot_as_file(pic_path + datename + ".png")
                # comHtml().print_html(print_name1, pic_path, datename)
            sleep(0.5)
            driver.find_element_by_xpath("//span[text()='" + file + "']/../../..").click()
            sleep(0.5)
            driver.find_element_by_xpath("//span[text()='开始比对']/..").click()
            datename = str(time.time())
            driver.get_screenshot_as_file(pic_path + datename + ".png")
            comHtml().print_html(print_name, pic_path, datename)
            sleep(30)
            try:
                WebDriverWait(driver, 15, 0.5).until(ec.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'ComparisonHeader_comHeaderTitle')]")))
            except Exception as e:
                print(e)
                print("比对超时")
        except Exception as e:
            print(e)
            print("比对弹框未弹出")

    #  团队导入文件弹框
    def com_importalert(self, driver, folder, file, pic_path, print_name):
        sleep(1)
        try:
            WebDriverWait(driver, 5, 0.5).until(
                ec.presence_of_element_located((By.XPATH, "//div[@class='ant-modal-title']")))
            # 目前弹框有问题，增加兼容
            try:
                driver.find_element_by_xpath("//span[text()='" + folder + "']/../../..").click()
            except Exception as e:
                print("弹框中文件名显示有问题，截图")
                print("文件夹名： %s" % folder)
                folder2 = folder.split(".", 2)[0]
                driver.find_element_by_xpath("//span[contains(text(),'" + folder2 + "')]/../../..").click()
                print_name1 = "弹窗截图"
                datename = str(time.time())
                driver.get_screenshot_as_file(pic_path + datename + ".png")
                comHtml().print_html(print_name1, pic_path, datename)
            sleep(1)
            print("准备点击了")
            el1 = driver.find_elements_by_xpath("//span[text()='" + file + "']/../../..")
            el1[-1].click()
            print("点击了")
            sleep(0.5)
            driver.find_element_by_xpath("//span[text()='确 定']/..").click()
            sleep(1)
            datename = str(time.time())
            driver.get_screenshot_as_file(pic_path + datename + ".png")
            comHtml().print_html(print_name, pic_path, datename)
            com_alert().com_equal(driver, pic_path, print_name, version="以新版本覆盖")
            sleep(15)
        except Exception as e:
            print(e)
            print("导入弹框未弹出")

    #  图例加入碎片弹框，传入参数包括按钮类型，确定或者取消
    def com_addFrager(self, driver, name, pic_path, print_name, button):
        sleep(0.5)
        try:
            printName = "未输入弹框截图"
            datename2 = str(time.time())
            driver.get_screenshot_as_file(pic_path + datename2 + ".png")
            comHtml().print_html(printName, pic_path, datename2)
            sleep(0.5)
            driver.find_element_by_xpath("//div[contains(@class,'FileImages_modalImageAction')]/input").send_keys(name)
            driver.switch_to.active_element.send_keys(Keys.ENTER)
            driver.find_element_by_xpath("//span[text()='" + button + "']/..").click()
            datename3 = str(time.time())
            driver.get_screenshot_as_file(pic_path + datename3 + ".png")
            comHtml().print_html(print_name, pic_path, datename3)
            sleep(1)
        except Exception as e:
            print(e)
            print("弹框未弹出")
            printName = "碎片弹框异常截图"
            datename = str(time.time())
            driver.get_screenshot_as_file(pic_path + datename + ".png")
            comHtml().print_html(printName, pic_path, datename)
        pass

    # 移动弹框，传入移动的文件夹层级，三级
    def com_move(self, driver, pic_path, button, folder, folder2=None, folder3=None):
        sleep(0.5)
        try:
            WebDriverWait(driver, 1.5, 0.5).until(ec.presence_of_element_located((
                By.XPATH, "//div[@class='ant-modal-title']")))
            comHtml().screen_shot(driver, pic_path, print_name="移动弹窗截图")
            sleep(0.5)
            driver.find_element_by_xpath(
                "//li[@class='moveToFile ant-tree-treenode-switcher-open']//span[text()='" + folder + "']").click()
            sleep(0.5)
            if folder2:
                el2 = driver.find_elements_by_xpath(
                    "//li[@class='moveToFile ant-tree-treenode-switcher-open']//span[text()='" + folder + "']")
                el2[-1].click()
                sleep(0.5)
                if folder3:
                    el3 = driver.find_elements_by_xpath(
                        "//li[@class='moveToFile ant-tree-treenode-switcher-open']//span[text()='" + folder + "']")
                    el3[-1].click()
                    sleep(0.5)
            driver.find_element_by_xpath("//span[text()='" + button + "']/..").click()
            comHtml().screen_shot(driver, pic_path, print_name="移动确定截图")
            sleep(1)
        except Exception as e:
            print(e)
            comHtml().screen_shot(driver, pic_path, print_name="移动弹窗异常")
            sleep(1)

    # 删除弹窗,传入控制方式
    def com_delete(self,driver,button=None):
        try:
            WebDriverWait(driver,5,0.5).until(ec.presence_of_element_located((By.XPATH,"//div[@class='ant-modal-body']")))
            if button=='确定':
                driver.find_element_by_xpath("//span[text()='确 定']/..").click()
            else:
                driver.find_element_by_xpath("//span[text()='取 消']/..").click()
        except Exception as e:
            print(e)
            print("删除弹框操作错误----")


# 发送邮件,传入参数为邮件主题和html文件url，不带附件.后面发现居然没有发件人和收件人
def send_mail(subject, fileurl):
    # 配置发送邮件参数
    # 发送邮箱服务器
    smtpServer = "smtp.exmail.qq.com"
    # 发送邮箱用户
    user = EmailProperty().SEND_EMAIL_USER
    pwd = EmailProperty().SEND_EMAIL_PWD
    # 发送邮箱
    sender = "qinchuan.he@fir.ai"
    # 接收邮箱
    receiver = "qinchuan.he@fir.ai"
    # 发送邮件主题
    subject = subject
    # 发送邮件内容，这里发送传入html的内容
    fp = open(fileurl, 'rb')
    mail_body = fp.read()
    fp.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpServer)
    smtp.login(user, pwd)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


# 重构发送邮件方法，添加了附件参数2020-11-0增加接收者参数receive（默认为空）
def send_mail(subject, fileurl=None, addfileurl=None, addfilename=None,content=None,receive=None):
    # 配置发送邮件参数
    # 发送邮箱服务器
    smtpServer = "smtp.exmail.qq.com"
    # 发送邮箱用户
    user = EmailProperty().SEND_EMAIL_USER
    pwd = EmailProperty().SEND_EMAIL_PWD
    # 发送邮箱
    sender = EmailProperty().SEND_EMAIL
    # 接收邮箱
    if receive:
        receiver = receive
    else:
        receiver = EmailProperty().RECEVI_EMAIL
    # receiver = "xiaohui.zhou@fir.ai"
    # 发送邮件主题
    subject = subject
    # 发送邮件内容，这里发送传入html的内容
    if fileurl:
        fp = open(fileurl, 'rb')
        mail_body = fp.read()
        fp.close()
        msg = MIMEText(mail_body, 'html', 'utf-8')
    if content:
        msg = MIMEText(content, 'html', 'utf-8')
    # msg['Subject'] = Header(subject, 'utf-8')

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = Header(subject, 'utf-8')
    msgRoot['From'] = EmailProperty().SEND_EMAIL # 发送邮箱信息
    #msgRoot['To'] = ','.join(EmailProperty().RECEVI_EMAIL) # 收件信息，不一定是真的发送邮箱
    msgRoot['To'] = ','.join(receiver) # 改造于2020-12-28
    # 附件,可能多个
    if addfileurl:
        add_file_type = type(addfileurl).__name__
        if add_file_type=="str":
            print('传入文件是str')
            af = open(addfileurl, 'rb').read()
            att = MIMEText(af, 'base64', 'utf-8')
            att['Content-Type'] = 'application/octet-stream'
            att['Content-Disposition'] = 'attachment; filename = ' + addfilename
            msgRoot.attach(att)
        elif add_file_type=="list":
            for i in range(len(addfileurl)):
                print(i)
                af = open(addfileurl[i], 'rb').read()
                att = MIMEText(af, 'base64', 'utf-8')
                att['Content-Type'] = 'application/octet-stream'
                att['Content-Disposition'] = 'attachment; filename = ' + addfilename[i]
                msgRoot.attach(att)
    msgRoot.attach(msg)  # 添加文案描述信息
    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpServer)
    smtp.login(user, pwd)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()


# 上传文件，上传图片到服务器 2024-11-13 虚拟机无法安装对应模块paramiko，暂时注释
# def server_upload(localFile, remoteFile):
#     # 创建ssh对象
#     ssh = paramiko.SSHClient()
#     # 允许连接不在know_hosts文件的主机
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     # 本地文件路径
#     localpath = localFile
#     # 服务器文件路径
#     remotePath = remoteFile
#
#     # 连接服务器
#     transport = paramiko.Transport(("192.168.1.223", 22))
#     transport.connect(username="root", password="fir2018518")
#     ssh = paramiko.SSHClient()
#     ssh._transport = transport
#     # ssh.connect(hostname="192.168.1.223", port=22, username="root", password="fir2018518")
#     # 打开一个channel（频道）并执行命令
#     stdin, stdout, stderr = ssh.exec_command('docker exec -i testpingtai bash;cd /opt;ls')
#     # stdin, stdout, stderr = ssh.exec_command('df -h;ls', timeout=30, get_pty=True)
#     # stdin, stdout, stderr = ssh.exec_command("ls")
#     print(stdout.read().decode('utf-8'))
#     transport.close()


#  封装定位
class com_xpath(object):
    # 本地上传按钮定位封装,传入路径,位置数值(某些地方要用到）
    def com_localupload(self,driver=None,url=None,position=None):
        global driver_new
        if not driver:
            driver=driver_new
        sleep(0.3)
        # driver.find_element_by_xpath("//input[@type='file']").send_keys(url) # 为了合同防伪，改的
        el =driver.find_elements_by_xpath("//input[@type='file']")
        if position:
            el[int(position-1)].send_keys(url)
        else:
            el[0].send_keys(url)
        # sleep(1.5)

    # 封装页面公共头部buttonType是按钮类型
    def com_head(self,driver,buttonType):
        el = driver.find_elements_by_xpath("//span[contains(@class,'GlobalHeader_dropdownButton')]")
        if buttonType=='help':
            return el[0]
        elif buttonType=='date':
            return el[-3]
        elif buttonType=='msg':
            return el[-2]
        elif buttonType=='Portrait':
            return el[-1]

    # 封装内容管理中二级目录,传入，按钮名称，比如回收站
    def com_contentcatalog(self,driver,button):
        sleep(0.5)
        if button=='回收站':
            driver.find_element_by_xpath("//span[text()='回收站']/../..").click()
        else:
            driver.find_element_by_xpath("//a[text()='"+button+"']/../..").click()
        sleep(0.5)

    # 文件夹，文件列表更多操作,传入文件名字（无重名） 目前不用传入文件夹或者文件类型
    def com_listmoreActions(self,driver=None,filename=None):
        global driver_new
        if not driver:
            driver = driver_new
        # el = driver.find_element_by_xpath("//span[text()='"+ filename +"']/../../../../../../../../..//i") #20200311废弃
        if filename:
            # 2023-01-31 调整，增加hover到条目步骤
            e1 = driver.find_element_by_xpath("//span[text()='" + filename + "']")
            ActionChains(driver).move_to_element(e1).perform()
            # 2023-01-31 调整，点击更多展开，不需要返回元素
            # el=driver.find_element_by_xpath("//span[text()='" + filename + "']/../../../../../../../../..//img[@style='cursor: pointer;']")
            driver.find_element_by_xpath("//span[text()='" + filename + "']/../../../../../../../../..//img[@style='cursor: pointer;']").click()

        else:
            # el = driver.find_elements_by_xpath("//img[@style='cursor: pointer;']")  # 不传名字默认第一个
            e1 = driver.find_element_by_xpath("//div[@class='ReactVirtualized__Table__row']")
            ActionChains(driver).move_to_element(e1).perform()
            driver.find_elements_by_xpath("//img[@style='cursor: pointer;']")[0].click()
        # return el[1]  # 2023-01-31调整，不需要返回元素了，直接点击更多


    # 文件夹、文件更多操作按钮,传入按钮名称 ,2023-01-31调整不需要返回元素，直接点击传入的值
    def com_listmoreButton(self,buttonName,driver=None):
        global driver_new
        if not driver:
            driver = driver_new
        el = driver.find_element_by_xpath("//span[text()='"+buttonName+"']/..")
        el.click()
        sleep(0.5)
        # return el  # 2032-02-01 注释

    # 重命名的input输入框,由于输入框是动态的，需要光标协助,传入名字
    def com_listrename(self,driver,name):
        el = driver.find_element_by_xpath("//input[contains(@class,'FileList_listInputFileName')]")
        sleep(0.3)
        ActionChains(driver).move_to_element(el).send_keys(name).perform()
        driver.switch_to.active_element.send_keys(Keys.ENTER)


    # 二次确认弹框，删除确认等
    def com_confirm(self,value,driver=None):
        global driver_new
        if not driver:
            driver = driver_new
        driver.find_element_by_xpath("//span[text()='"+value+"']/..").click()
        sleep(0.5)




    # 封装预览头部按钮的定位，传入driver，button（区分按钮类型）,
    def com_previewButton(self, driver, button):
        '''预览中的定位'''
        el1 = ""  # 返回的参数
        try:
            # 首先确定是否进入预览界面
            WebDriverWait(driver, 15, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
            # mode = 1，代表私有资料，其余都是团队
            # 2019/09/24根据需求调整，本次需求改了预览模式的按钮规则和排列，这一步是打开更多按钮
            driver.find_element_by_xpath("//i[@class='anticon anticon-more']").click()
            # el = driver.find_elements_by_xpath("//div[contains(@class,'FileToolbar_toolButton')]") #  样式改了废弃
            # if button == 'textSearch':  # 搜索按钮
                # el1 = el[0]
            if button == 'innerSearchModel': # 内容搜索模式
                el1 = el1 = driver.find_element_by_xpath("//span[text()='内容搜索']/..")
            elif button == 'modifyModel': #  编辑模式
                el1 = el1 = driver.find_element_by_xpath("//span[text()='编辑文档']/..")
            elif button == 'history':  # 覆盖历史
                el1 = driver.find_element_by_xpath("//div[text()='覆盖历史']/..")
            elif button == 'label':  # 标签
                el1 = driver.find_element_by_xpath("//div[text()='标签']/..")
            # elif button == 'share':  # 分享
                # el1 = el[3]
            # elif button == 'store':  # 收藏
                # el1 = el[3]
            # elif button == 'notes':  # 批注
                # el1 = el[4]
            elif button == 'connect':  # 关联引用
                el1 = driver.find_element_by_xpath("//div[text()='关联引用']/..")
            elif button == 'compare':  # 比对
                el1 = driver.find_element_by_xpath("//div[text()='文件对比']/..")
            # elif button == 'details':  # 共享信息
                # el1 = el[-3]
            # elif button == 'download':  # 下载
                #  el1 = el[-2]
            elif button == 'delete':  # 删除
                el1 = driver.find_element_by_xpath("//div[text()='删除']/..")
            elif button == 'cover':  # PDF覆盖
                el1 = driver.find_element_by_xpath("//div[text()='PDF覆盖']/..")
            else:
                el1 = ""
                print("传入预览按钮类型不对")
            # 2019/09/26增加消除遮罩层设置，某些没有
            try:
                el = driver.find_element_by_xpath("//section[contains(@class,'PreviewContent_viewLayout')]")  # 定位到元素
                addAttribute(driver, el, 'style', 'display:none')  # 隐藏元素
            except Exception as e:
                pass
        except Exception as e:
            print(e)
            print("没有进入预览")
        sleep(0.5)
        return el1

    #  列表预览顶部的按钮，button代表按钮类型
    def com_listButton(self, driver, button):
        el21 = ""
        try:
            WebDriverWait(driver, 2, 0.5).until(
                ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'FileListToolbar_toolButton')]")))
            # 有边框的按钮
            el2 = driver.find_elements_by_xpath("//div[contains(@class,'FileListToolbar_toolButton')]")
            # 无边框的按钮
            el3 = driver.find_elements_by_xpath("//button[contains(@class,'ant-btn FileListToolbar_toolButton')]")
            if button == 'create':
                # 2023-01-28调整，由于样式改变，做出调整
                el21 = el3[1]
            elif button == 'upload':
                el21 = el3[1]
            elif button == 'import1':
                el21 = el3[2]
            elif button=='createSpace':
                el21 = el3[3]
            elif button == 'share':
                el21 = el2[1]
            elif button == 'store':
                el21 = el2[-5]
            elif button == 'move':
                el21 = el2[-4]
            elif button == 'download':
                el21 = el2[-3]
            elif button == 'delete':
                el21 = el2[-2]
            elif button == 'switch':
                el21 = el2[-1]
            else:
                print("传入按钮类型错误")
        except Exception as e:
            print(e)
            print("没有处在资源页面中")
        return el21

    #  文件夹内搜索, 边写边搜，艾玛搜索,传入搜索关键字进行搜索跳转
    def com_internalSearch(self, driver, key):
        sleep(1)
        driver.find_element_by_xpath("//input[contains(@placeholder,'搜文件，也可以通过')]").clear()
        driver.find_element_by_xpath("//input[contains(@placeholder,'搜文件，也可以通过')]").send_keys(key)
        driver.switch_to.active_element.send_keys(Keys.ENTER)
        sleep(3)

    #  文件夹内搜索，选中时间和类型,前提是处于文件夹内搜索界面
    def com_internalChooseType(self, driver, time, type):
        # 选择时间
        el11 = driver.find_elements_by_xpath("//div[@class='ant-select-selection__rendered']")  # 选项框外层
        el12 = driver.find_elements_by_xpath("//div[@class='ant-select-selection-selected-value']")  # 选项框当前值
        checktime = el12[0].text
        if checktime != time:
            el11[0].click()
            driver.find_element_by_xpath("//li[text()='" + time + "']").click()
        checktype = el12[1].text
        if checktype != type:
            el11[1].click()
            driver.find_element_by_xpath("//li[text()='" + type + "']").click()
        try:
            WebDriverWait(driver, 5, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
        except Exception as e:
            print(e)
            print("加载iframe超时")

    #  进入预览界面,有iframe的
    def com_preview(self, driver, fileName):
        print(fileName)
        driver.find_element_by_xpath("//span[text()='" + fileName + "']/..").click()
        print("点击完成")
        try:
            WebDriverWait(driver, 15, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
            print("等待1完成")
        except Exception as e:
            print(e)
            print("没有进入预览或者加载超时或者解析失败")

    # log定位
    def com_log(self, driver):
        User().root_private(driver)
        WebDriverWait(driver, 10, 0.2).until(ec.presence_of_element_located((By.XPATH, "//span[text()='笔记摘录']")))

    # 智能搜索输入框,传入driver和位置,传入值认为是问答搜索
    def smart_search(self,driver,position=None):
        """
        智能搜索输入框
        :param driver:
        :param position:
        :return:
        """
        if position:
            el = driver.find_element_by_xpath("//input[contains(@class,'GlobalSearch_searchInputTwo')]")
        else:
            el = driver.find_element_by_xpath("//input[contains(@class,'GlobalSearch_searchInputOne')]")
        return el

# 封装公共的操作，比如只读预览，内容搜索预览，编辑
class com_operation():
    # 打开预览模式，只读预览,传入，名字、来源（私有可不传）、模式（read_only、search、edit）
    def com_preview(self, driver, name, resource=None, pattern=None):
        driver.find_element_by_xpath("//span[text()='"+name+"']/..").click()
        try:
            WebDriverWait(driver, 15, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
        except Exception as e:
            print(e)
            print("打开预览失败")
        # 打开内容搜索模式
        if(pattern=='search'):
            driver.find_element_by_xpath("//span[text()='内容搜索']/..").click()
            try:
                WebDriverWait(driver, 15, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
            except Exception as e:
                print(e)
                print("打开预览失败")
        # 进入编辑模式
        elif(pattern=='edit'):
            # 团队资源，默认有值就是团队资源
            if(resource):
                driver.find_element_by_xpath("//span[text()='协作编辑']/..").click()
                try:
                    WebDriverWait(driver, 15, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
                except Exception as e:
                    print(e)
                    print("打开预览失败")
            else:
                driver.find_element_by_xpath("//span[text()='编辑文档']/..").click()
                try:
                    WebDriverWait(driver, 15, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
                except Exception as e:
                    print(e)
                    print("打开预览失败")

    # 退出预览,pattern默认只读,历史版本和内容搜索模式需要再次返回，尝试编辑使用
    # 2.0.7版本返回按钮统一调整
    def com_close_preview(self, driver, pattern=None):
        # driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click() # 2.0.7版本废弃
        driver.find_element_by_xpath("//span[contains(@class,'backBtnImg')]").click()
        if pattern:  # 包含两种情况，一直是search，一种是history
            sleep(0.5)
            driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
        sleep(0.5)

# 公共上传参数,公共参数

url1 = os.path.join(com_path(),"19种格式","office","003_模板_TestLink测试用例导入.xls")
url2 = os.path.join(com_path(),"19种格式","office","2017年12月11日-2017年12月15日发行监管部.doc")
url3 = os.path.join(com_path(),"19种格式","office","cyprex1.3测试用例.xlsx")
url4 = os.path.join(com_path(),"19种格式","office","带图片表格文档.docx")
url5 = os.path.join(com_path(),"19种格式","office","小z素材-商务炫酷风格动态模板-003.ppt")


url6 = os.path.join(com_path(),"19种格式","图片","BMP图片.bmp")
url7 = os.path.join(com_path(),"19种格式","图片","timg.jpg")
url8 = os.path.join(com_path(),"19种格式","图片","验证图片.png")

url9 = os.path.join(com_path(),"19种格式","音频","16k.pcm")
url10 = os.path.join(com_path(),"19种格式","音频","m4a.wav")
url11 = os.path.join(com_path(),"19种格式","音频","另一种格式.amr")
url12 = os.path.join(com_path(),"19种格式","音频","群星 - 贾谊《过秦论》.mp3")
url13 = os.path.join(com_path(),"19种格式","音频","电话会议兴业证券.m4a")

url14 = os.path.join(com_path(),"19种格式","其他","146页年度报告.PDF")
url15 = os.path.join(com_path(),"19种格式","其他","测试解压.zip")
url16 = os.path.join(com_path(),"19种格式","其他","厦门亿联网络技术股份有限公司 关于召开 2018 年年度股东大会的通知.html")
url17 = os.path.join(com_path(),"19种格式","其他","天空1.txt")


up_list = [url1,url2,url3,url4,url5,url6,url7,url8,url9,url10,url11,url12,url13,url14,url15,url16,url17]

url21 = os.path.join(com_path(),"19种格式","图例提取文件","PDF后缀验证解析.PDF")
url22 = os.path.join(com_path(),"19种格式","图例提取文件","pdf小写验证解析.pdf")
url23 = os.path.join(com_path(),"19种格式","图例提取文件","docx验证解析.docx")
url24 = os.path.join(com_path(),"19种格式","图例提取文件","doc验证解析.doc")

url25 = os.path.join(com_path(),"19种格式","拆分","拆分模板.doc")

url26 = os.path.join(com_path(),"19种格式","合并","封面.doc")
url27 = os.path.join(com_path(),"19种格式","合并","发行人声明.doc")
url28 = os.path.join(com_path(),"19种格式","合并","本次发行概况.doc")
url29 = os.path.join(com_path(),"19种格式","合并","重大事项提示.doc")

# 比对和审核文件
url31 = os.path.join(com_path(),"19种格式","比对文件","合同1.doc")
url32 = os.path.join(com_path(),"19种格式","比对文件","合同1扫描件（8张合并）.pdf")

up_analysis = [url21,url22,url23,url24]
# 解析文件夹前缀名字,可也通过此方法获取后缀名
folder_analysis = "解析"
def get_urlname(url):
    """ 获取url的name"""
    return os.path.splitext(os.path.split(url)[1])[0]

# 2020-05-07 增加关键字断言方法，关键字驱动使用,有需要可以传入位置参数
def assertls(path,expect,position=None):
    """ 断言方法,传入定位和期望值"""
    global driver_new

    if position:
        el = driver_new.find_elements_by_xpath(path)
        print(el[int(position)].text)
        print(str(expect) in el[int(position)].text)
        assert str(expect) in el[int(position)].text
    else:
        el = driver_new.find_element_by_xpath(path)
        print(el.text)
        print(str(expect) in el.text)
        assert str(expect) in el.text

    # assert el.text==expect # 启用字符串包含关系，in



# 2020-05-08 增加移动方法,关键字驱动使用
class MouseOperation():
    """ 封装鼠标操作方法"""
    def mouse_over(self,driver = None,path=None):
        """ 鼠标悬停到元素上"""
        global driver_new
        if not driver:
            driver = driver_new
        el = driver.find_element_by_xpath(path)
        ActionChains(driver).move_to_element(el).perform()

# 2020-05-08 点击元素,关键字驱动用
def clickElement(driver=None,path=None):
    """ 点击元素"""
    global driver_new
    if not driver:
        driver = driver_new
    driver.find_element_by_xpath(path).click()

# 2020-05-08 浏览器后退，关键字驱动用
def go_back(driver = None):
    """ 浏览器后退"""
    global driver_new
    if not driver:
        driver = driver_new
        driver.back()

# 2020-05-20 失败截图方法 关键字驱动用
def screenShot(driver = None,url = None):
    """ 截图，失败截图"""
    global driver_new
    if not driver:
        driver=driver_new
    if url:
        driver.get_screenshot_as_file(url)

# 2020-05-20 时间戳函数 关键字驱动用,传入需要的时间戳格式
def timeStamp(driver=None,format=None):
    global driver_new
    if not driver:
        driver=driver_new
    if format=='date':
        stamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    elif format=='number':
        stamp= int(time.time())
    else:
        stamp=str(time.time())
    return stamp



#图像处理
class Image_Processing(object):
    """
    图像处理类
    """
    def image_Diffence(self,image_1,image_2,image_error=None):
        """
        diffence方法比较了两张图片全路径，目前传入截图是32位深，需要转成24位深
        第三个地址放置比对失败之后的差异图片
        :param driver:
        :param image1:
        :param image2:
        :return:
        """
        img_1 = Image.open(image_1) # type:PngImageFile
        img_2 = Image.open(image_2) # type:PngImageFile
        diff = ImageChops.difference(img_1.convert("RGB"),img_2.convert("RGB"))
        if diff.getbbox()==None:
            print("两张图片一样")
        else:
            print("两张图片不一样")
            if image_error:
                diff.save(image_error)
            else:
                diff.save(os.path.join(com_path(),"error","diff.png"))



# 封装对于元素的操作js操作
def addAttribute(driver, elementobj, attributeName, value):
    '''
    封装向页面标签添加新属性的方法
    调用JS给页面标签添加新属性，arguments[0]~arguments[2]分别
    会用后面的element，attributeName和value参数进行替换
    添加新属性的JS代码语法为：element.attributeName=value
    比如input.name='test'
    '''
    driver.execute_script("arguments[0].%s=arguments[1]" % attributeName, elementobj, value)

# 封装对于元素高亮的操作
def highlight(driver,element):
    # driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
    #                       element, "background:green ;border:2px solid red;")
    driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
                          element, "border:2px solid red;")










