# coding=utf-8


import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)
print('----------')
# import openpyxl
from time import sleep

url = r'D:\work\1测试\11数据&检查\2021-02-24\100个中文PDF的fileid.xlsx'
url = r'D:\work\1测试\11数据&检查\2021-02-24\100pdf.txt'
path1_src = '/data/project/datastorage/datastorage/datastorage-go/data_hub/pdf/'
path1_srcaj = '/data/project/datastorage/datastorage/datastorage-go/data_hub/'
# url = r'/opt/qy/100pdf.txt'
url_50=r'D:\work\1测试\11数据&检查\2021-02-24\50pdf.txt'
url_50=r'/opt/qy/50pdf.txt'
url_caj=r'D:\work\1测试\11数据&检查\2021-02-24\50caj.txt'
url_caj=r'/opt/qy/50caj.txt'

# 100个中文pdf
def get_pdf100():
    file = open(url, 'r+')
    s = file.readlines()
    for i in s:
        p = i.split('何秦川')

        path1 = os.path.join(path1_src, p[0], 'orginal.pdf')
        path_dest = os.path.join('/opt/qy/pdf1/', p[1])
        print(p[0])
        print(path1)
        print(path_dest)
        ss = 'cp {} {}'.format(path1, path_dest)
        try:
            print(ss)
            os.system(ss)
        except Exception as e:
            print(e)
#50个英文文档
def get_pdf50():
    file = open(url_50, 'r+')
    s = file.readlines()
    for i in s:
        p = i.split('何秦川')

        path1 = os.path.join(path1_src, p[0], 'orginal.pdf')
        path_dest = os.path.join('/opt/qy/pdf50/', p[1])
        print(p[0])
        print(path1)
        print(path_dest)
        ss = 'cp {} {}'.format(path1, path_dest)
        try:
            print(ss)
            os.system(ss)
        except Exception as e:
            print(e)

# 50个caj文件
def get_caj50():
    file = open(url_caj, 'r+')
    s = file.readlines()
    for i in s:
        p = i.split('何秦川')

        path1 = os.path.join(path1_srcaj, p[0], 'orginal.pdf')
        path_dest = os.path.join('/opt/qy/caj50/', p[1])
        print(p[0])
        print(path1)
        print(path_dest)
        ss = 'cp {} {}'.format(path1, path_dest)
        try:
            print(ss)
            os.system(ss)
        except Exception as e:
            print(e)

if __name__=='__main__':
    # get_pdf100()
    # get_pdf50()
    get_caj50()













