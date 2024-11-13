# coding=utf-8

"""
从5016服务器下载文件
2020-08-11
"""

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)
import paramiko




def download_file():
    path = r'D:\2'
    url = '/data/project/datastorage/datastorage/datastorage-go/data_hub/pdf/28d9e092-2fc2-417a-9077-50644cfb4da1'
    open('','rb')




if __name__=='__main__':
    download_file()





