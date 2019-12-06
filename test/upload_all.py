# coding=utf-8

#2019-12-02
#上传验证
# 新建一个文件夹，进入文件夹之后上传，截图
import time
from time import sleep

from common.comfunction import execBrower
from common.comfunction import User
from common.comfunction import com_xpath
from common.comfunction import com_path

def upload_all(driver,image_path=None,image_prefix=None):
    """ 上传所有文件"""
    # 返回私有根目录
    User().root_private(driver)
    # 新建文件夹
    up_folder = str(time.time())
    User().createFolder(driver,folder=up_folder)
    # 进入文件夹
    driver.find_element_by_xpath("//span[text()='"+up_folder+"']/..").click()
    sleep(0.5)

    # 准备上传
    url1=str(com_path)+"19种格式\\"+"office\\"+"003_模板_TestLink测试用例导入.xls"
    url2 = str(com_path) + "19种格式\\" + "office\\" + "2017年12月11日-2017年12月15日发行监管部.doc"
    url3 = str(com_path) + "19种格式\\" + "office\\" + "cyprex1.3测试用例.xlsx"
    url4 = str(com_path) + "19种格式\\" + "office\\" + "带图片表格文档.docx"
    url5 = str(com_path) + "19种格式\\" + "office\\" + "小z素材-商务炫酷风格动态模板-003.ppt"

    url6 = str(com_path) + "19种格式\\" + "图片\\" + "BMP图片.bmp"
    url7 = str(com_path) + "19种格式\\" + "图片\\" + "timg.jpg"
    url8 = str(com_path) + "19种格式\\" + "图片\\" + "验证图片.png"

    url9 = str(com_path) + "19种格式\\" + "音频\\" + "16k.pcm"
    url10 = str(com_path) + "19种格式\\" + "音频\\" + "筷子兄弟《小苹果》.wav"
    url11 = str(com_path) + "19种格式\\" + "音频\\" + "另一种格式.amr"
    url12 = str(com_path) + "19种格式\\" + "音频\\" + "群星 - 贾谊《过秦论》.mp3"
    url16 = str(com_path) + "19种格式\\" + "音频\\" + "世纪大道199号.m4a"

    url14 = str(com_path) + "19种格式\\" + "其他\\" + "146页年度报告.PDF"
    url15 = str(com_path) + "19种格式\\" + "其他\\" + "测试解压.zip"
    url16 = str(com_path) + "19种格式\\" + "其他\\" + "厦门亿联网络技术股份有限公司 关于召开 2018 年年度股东大会的通知.html"
    url17 = str(com_path) + "19种格式\\" + "其他\\" + "天空1.txt"




    com_xpath().com_localupload(driver,url1)