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
from time import sleep
import time   #生成时间戳用
import os    #上传autoit用
# 发送邮件
import smtplib
from email.mime.text import  MIMEText  # 正文
from email.header import Header  # 头部
from email.mime.multipart import MIMEMultipart # 上传附件用

# 服务器上传
import paramiko







# 启动浏览器
def execBrower(mode):
    opt = Options()
    opt.add_argument('--disable--gpu')
    opt.add_argument('--headless')
    path = "C:\\2services\\driver\\chromedriver.exe"
    if mode == 1:
        driver=webdriver.Chrome(options=opt, executable_path=path)
    else:
        driver = webdriver.Chrome(path)
    driver.set_window_size(1400, 900)  #设置窗口大小
    driver.implicitly_wait(20)
    return driver

# 登录相关
class user:
    url="https://testcyprex.fir.ai/sign-in"
    # url = "https://cyprex.fir.ai/sign-in"
    # url = "http://firai-test.gjzqth.com:4680/"
    user = "19967893456"
    # user = "13248131618"
    # user="19956966528"
    pwd = "Test123456"
    # def __init__(self, url, user, pwd):
    #     self.url = url
    #     self.user = user
    #     self.pwd = pwd
    # 登录
    def login(self, driver):
        driver.get(self.url)
        driver.find_element_by_xpath("//div[text()='账号登录']").click()
        driver.find_element_by_id("username_no").send_keys(self.user)
        driver.find_element_by_id("password").send_keys(self.pwd)
        driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div[1]/div[3]/div[2]/form/div[3]/div/div/span").click()  # 登录，好像伪类中的文字不能识别
        WebDriverWait(driver, 10, 0.2).until(ec.presence_of_element_located((By.XPATH, "//span[text()='艾玛同学']")))

# 生成html相关的类
class comHtml:
    def print_html(self,picname,picpath,picid):    #就是传入名称，路径，picid就是时间
        print("<a href = \"javascript:void(0)\" onclick = \"document.getElementById(\'"+picid+"\').style.display='block';document.getElementById('fade').style.display='block'\">"+picname+"预览</a>"
            +"<div id=\""+picid+"\" class=\"white_content\">"
            +"<a href = \"javascript:void(0)\" onclick = \"document.getElementById(\'"+picid+"\').style.display='none';document.getElementById('fade').style.display='none'\" style=\"align-content: center\">点这里关闭</a>"
            +"<img height=\"800\" width=\"1400\" src=\""+picpath+picid+".png"+"\">"
            +"</div>" 
            +"<div id=\"fade\" class=\"black_overlay\"></div>")


#团队相关功能
class team:
    def check_team(self,driver):
        '''检查团队是否存在,不存在就创建，目前没有判断5个团队的情况的'''
        sleep(1)
        driver.find_element_by_xpath("//a[text()='团队共享']").click()
        team_name = "验证的团队"
        try:
            WebDriverWait(driver,2,0.5).until(ec.presence_of_element_located((By.XPATH,"//span[text()='验证的团队']")))
        except Exception as e:
            print("团队不存在准备新建")
            driver.find_element_by_xpath("//span[text()='创建新团队并命名团队文件夹']/..").click()
            driver.find_element_by_xpath("//input[@placeholder='团队及团队文件夹名称']").send_keys(team_name)
            # driver.find_element_by_xpath("//span[text()='确 定']/..").click()
            sleep(1)
            driver.find_element_by_xpath("//div[@class='ant-modal-footer']/div/button[2]").click()
            sleep(1)
            print(e)
        driver.find_element_by_xpath("//span[text()='验证的团队']").click()
        return team_name

# 分享，公共方法,这个方法不带批注关联权限--->>>点击了分享按钮之后调用这个方法
def com_share(team_name,version, print_name, pic_path, driver): # 分别是团队名字，冲突覆盖方式，截图的图片汉字名字,driver
    sleep(1)
    # 选择团队,分享
    driver.find_element_by_xpath("//span[text()='" + team_name + "']/..").click()
    sleep(0.5)
    driver.find_element_by_xpath("//span[text()='确 定']/..").click()
    # 截图
    datename = str(int(time.time()))
    driver.get_screenshot_as_file(pic_path + datename + ".png")
    comHtml().print_html(print_name, pic_path, datename)
    # 检查弹框是否关闭
    try:
        WebDriverWait(driver, 5, 0.5).until_not(
            ec.presence_of_element_located((By.XPATH, "//span[text()='分享给团队']")))
        # 兼容版本冲突
        try:
            WebDriverWait(driver, 5, 0.5).until(
                ec.presence_of_element_located((By.XPATH, "//div[text()='版本冲突']")))
            # print("找到了")
            driver.find_element_by_xpath("//span[text()='"+version+"']/..").click()
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
    datename = str(int(time.time()))
    driver.get_screenshot_as_file(pic_path + datename + ".png")
    comHtml.print_html(print_name, pic_path, datename)
    try:
        # self.driver.find_element_by_xpath("//div[text()='版本冲突']")
        WebDriverWait(driver, 3, 0.5).until(ec.presence_of_element_located((By.XPATH, "//div[text()='版本冲突']")))
        driver.find_element_by_xpath("//span[text()='"+version+"']/..").click()
    except Exception as e:
        print(e)
        print("--没有冲突--")
    sleep(30)

#  公共的弹窗类，所有弹窗相关的封装都放这里
class com_alert(object):
    #  点击按钮之后的冲突弹框公共方法，传入截图存放路径，html输出名字，冲突处理方法。包含截图输出搭配html
    def com_equal(driver, pic_path, print_name, version):
        #  第一步，截图，并且输出到html
        sleep(2)
        datename = str(int(time.time()))
        driver.get_screenshot_as_file(pic_path + datename + ".png")
        comHtml.print_html(print_name, pic_path, datename)
        #  第二步，判断是否有弹框
        try:
            WebDriverWait(driver, 3, 0.5).until(ec.presence_of_element_located((By.XPATH, "//div[text()='版本冲突']")))
            driver.find_element_by_xpath("//span[text()='" + version + "']/..").click()
        except Exception as e:
            print(e)
            print("--没有冲突--")
        sleep(0.5)


# 发送邮件,传入参数为邮件主题和html文件url，不带附件
def send_mail(subject,fileurl):
    # 配置发送邮件参数
    # 发送邮箱服务器
    smtpServer = "smtp.exmail.qq.com"
    # 发送邮箱用户
    user = "qinchuan.he@fir.ai"
    pwd = "Test123456"
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

# 重构发送邮件方法，添加了附件参数
def send_mail(subject,fileurl, addfileurl,addfilename):
    # 配置发送邮件参数
    # 发送邮箱服务器
    smtpServer = "smtp.exmail.qq.com"
    # 发送邮箱用户
    user = "qinchuan.he@fir.ai"
    pwd = "Test123456"
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
    # 附件
    af = open(addfileurl, 'rb').read()
    att = MIMEText(af, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename = '+addfilename
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = Header(subject, 'utf-8')
    msgRoot.attach(att)
    msgRoot.attach(msg) # 添加文案描述信息
    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpServer)
    smtp.login(user, pwd)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()

# 上传文件，上传图片到服务器
def server_upload(localFile, remoteFile):
    # 创建ssh对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 本地文件路径
    localpath = localFile
    # 服务器文件路径
    remotePath = remoteFile

    # 连接服务器
    transport = paramiko.Transport(("192.168.1.223",22))
    transport.connect(username="root", password="fir2018518")
    ssh = paramiko.SSHClient()
    ssh._transport = transport
    # ssh.connect(hostname="192.168.1.223", port=22, username="root", password="fir2018518")
    # 打开一个channel（频道）并执行命令
    stdin, stdout, stderr = ssh.exec_command('docker exec -i testpingtai bash;cd /opt;ls')
    # stdin, stdout, stderr = ssh.exec_command('df -h;ls', timeout=30, get_pty=True)
    # stdin, stdout, stderr = ssh.exec_command("ls")
    print(stdout.read().decode('utf-8'))
    transport.close()

#  封装定位
class com_xpath(object):
    # 封装预览头部按钮的定位，传入driver，button（区分按钮类型）
    def com_preview(self, driver, button):
        '''预览中的定位'''
        el1 = ""  # 返回的参数
        try:
            # 首先确定是否进入预览界面
            WebDriverWait(driver, 15, 0.5).until(ec.presence_of_element_located((By.XPATH, "//iframe")))
            # mode = 1，代表私有，其余都是团队
            el = driver.find_elements_by_xpath("//div[contains(@class,'FileToolbar_toolButton')]")
            if button =='textSearch':
                el1 = el[0]
            elif button == 'history':
                el1 = el[1]
            elif button == 'label':
                el1 = el[2]
            elif button == 'share':
                el1 = el[3]
            elif button == 'store':
                el1 = el[3]
            elif button == 'notes':
                el1 = el[4]
            elif button == 'connect':
                el1 = el[5]
            elif button == 'compare':
                el1 = el[-3]
            elif button == 'details':
                el1 = el[-3]
            elif button == 'download':
                el1 = el[-2]
            elif button == 'delete':
                el1 = el[-1]
            else:
                el1 = ""
                print("传入预览按钮类型不对")
        except Exception as e:
            print(e)
            print("没有进入预览")
        return el1

    #  列表预览顶部的按钮，button代表按钮类型
    def com_listButton(self, driver, button):
        el21 = ""  #  返回参数
        try:
            WebDriverWait(driver, 3, 0.5).until(ec.presence_of_element_located((By.XPATH, "//div[@class='FileListToolbar_toolButton']")))
            el2 = driver.find_elements_by_xpath("//div[@class='FileListToolbar_toolButton']")
            if button == 'create':
                el21 = el2[0]
            elif button == 'upload':
                el21 = el2[1]
            elif button == 'import1':
                el21 = el2[2]
            elif button == 'share':
                el21 = el2[-5]
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


























