#coding=utf-8

import io

from PIL.PngImagePlugin import PngImageFile
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
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from common.comfunction import com_path,send_mail,OpenBrowser,User
from common.private import EmailProperty
from common.comparameter import symbol
from PIL import Image
from PIL import ImageChops


def compare_images(path_one, path_two, diff_save_location):
    """
    比较图片，如果有不同则生成展示不同的图片

    @参数一: path_one: 第一张图片的路径
    @参数二: path_two: 第二张图片的路径
    @参数三: diff_save_location: 不同图的保存路径
    """
    image_one = Image.open(path_one)  # type:PngImageFile
    print("%s----%s-----%s"%(image_one.size,image_one.format,image_one.mode))
    print(image_one)
    # image_one.show()
    # image_one.resize((400,400))
    # image_one.show()
    print(len(image_one.split()))
    image_one = image_one.convert("RGB")
    print(image_one)
    image_two = Image.open(path_two) # type:PngImageFile
    print(image_two)
    # image_two.resize((400,400))
    # image_two.show()

    # image_two.convert()
    print(len(image_two.split()))
    image_two = image_two.convert("RGB")
    print(image_two)
    try:
        diff = ImageChops.difference(image_one, image_two)
        print("diff: %s" % diff)
        # diff.getpixel((100,100))
        diff.show()
        # diff.save(diff_save_location)
        print(diff.getbbox())
        if diff.getbbox() is None:
            # 图片间没有任何不同则直接退出
            print("【+】We are the same!")
        else:
            diff.save(diff_save_location)
        diff.close()
    except ValueError as e:
        text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
                "The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, "
                "right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted "
                "image must match the size of the region.使用2纬的box避免上述问题")
        print("【{0}】{1}".format(e, text))

def qy_1():
    a = []
    perfix = '续费月度会员'
    suffix = '测试搜索逻辑'
    for i in symbol.china_symbol:
        print(perfix+i+suffix)


def cca(cur=0):
    for i in range(2):
        # print('====',i)
        for j in range(cur):
            # print('i---j',i,j)
            if j==1:
                break
        else:
            print('--------------')
            cca(cur+1)

def recursion(n):
    print("level %d" % n)
    if n<4:
        recursion(n+1)
    print("level %d" % n)

def sum(n):
    sum1=n*(n+1)
    if n>1:
        sum1 = n * (n - 1)
        sum(n-1)

    # print(sum1)
    return sum1

def queen(A, cur=0):
    # print(A)
    print(cur)
    if cur == len(A):
        # print(A)
        return 0
    for _ in range(2):  # 遍历当前行的所有位置0,1
        queen(A, cur+1)  # 计算下一行的位置


if __name__ == '__main__':
    queen([None] * 3)
    # recursion(1)
    # print(sum(3))
    # qy_1()
    # root = "C:\\Users\\fir\\Pictures\\QQ浏览器截图\\"
    # picture1 = root+"QQ浏览器截图20200113110005.png"
    # picture2 = root+"QQ浏览器截图20200113105958.png"
    # compare_images(picture1,
    #                picture2,
    #                'C:\\Users\\fir\\Pictures\\QQ浏览器截图\\我们不一样.png')





# mode = 2
# driver = OpenBrowser(mode)
# try:
#     User().login(driver)
#     User().createFolder(driver)
#     print("执行完毕")
# except Exception as e:
#     print(e)
# driver.quit()


# p1="test.png"
# s1 = os.path.join(com_path(),"截图","合并失败截图.png")
# send_mail("合并检查邮件", EmailProperty().EMAIL_COMBINE, s1,p1)







# sender = "qinchuan.he@fir.ai"
# recivie = ["m13248131618@163.com","849446261@qq.com"]
# msg = MIMEText("我发送的邮件","plain","utf-8")
# print(sender)
# msg['From'] = sender
# print(','.join(recivie))
# msg['To'] = ','.join(recivie)
# msg['Subject'] ="验证的邮件"
# # Header("","utf-8")
# print(" msg--------:%s" % msg)
# smtp  = smtplib.SMTP("smtp.exmail.qq.com")
# # smtp.connect("smtp.exmail.qq.com")
# smtp.login("qinchuan.he@fir.ai","Test12345678")
# smtp.sendmail("qinchuan.he@fir.ai",["m13248131618@163.com","849446261@qq.com"],msg.as_string())
# smtp.quit()











# send_mail("合并检查邮件", EmailProperty().EMAIL_COMBINE, s,p)








# @pytest.mark.parametrize(
#     "a, b, c",
#     [(1,2,1),
#      (2,2,4),
#      (0,9,1)]
#     # ids=["case1", "case2", "case3"]
# )
# def test_pow(a,b,c,test_url):
#     assert math.pow(a, b) == c
#     # print(test_url)

# @pytest.mark.flaky(reruns=5, reruns_delay=1) # 设置失败执行5次，0延迟
# def test_baidu():
#     sleep(3)
#     assert 2 + 2 ==4

# def test_bi():
#     sleep(2)
#     print("hahha")
# def test_acf():
#     sleep(2)
#     print("acfun")
# if __name__ == "__main__":
#     # pytest.main(['-s'])
#     # pytest.main(['-sv',  'test_3.py', '--html=C:\\work\\1测试\\10自动化\\报告\\3.html'])
#     # pytest.main(['-sv', 'test_3.py', '--tests-per-worker', 'auto', '--html=C:\\work\\1测试\\10自动化\\报告\\3.html'])
#     # pytest.main(['-sv', 'test_3.py', '--junit-xml=../test_report/log1.xml'])
#     pytest.main(['-sv', 'test_3.py', '--html=../test_report/log.html'])


