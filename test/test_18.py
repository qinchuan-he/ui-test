import json
import time
from datetime import datetime

import requests
import subprocess
import socket
from common.comfunction import *


# 检查grobid服务是否可用，并且重新拉起服务
def check_grobid():
    urls = 'http://106.75.225.101:8070/api/processFulltextDocument'
    datas = {"consolidateHeader":"1","teiCoordinates":"ref","teiCoordinates":"s","teiCoordinates":"biblStruct"
        ,"teiCoordinates":"persName","teiCoordinates":"figure","teiCoordinates":"formula","teiCoordinates":"head","teiCoordinates":"note"}
    path = r'D:\上传文件\pdf比对\Renewable building-有图例参考相关影响因子.pdf'
    time_out = 100  # 设置超时时间

    print(time.time())
    with open(path,'rb') as file:
        try:
            result = requests.post(url=urls,data=datas,files={"input":file},timeout=time_out)
        except requests.exceptions.Timeout:
            print(time.time())
    print(result.status_code)

# ping 香港服务器的ip，检查网络是否畅通
def check_network():

    ip = '8.212.18.160'
    result = subprocess.run(['ping',ip], capture_output=True, text=True)
    output = result.stdout
    print(type(output))
    print(output)
    if '64 bytes from' in output:
        print('------------------')
    else:
        print("=================")


def check_ip():

    ip = '8.212.18.160'
    # ip = '192.168.1.233'
    port = 443

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    result = s.connect_ex((ip,port))
    if result == 0:
        print('连接畅通')
    else:
        print('连接不上')
        print(result)
    s.close()

# 调用231服务器上新项目，新的PDF解析服务


def get_xmind():
    url = 'https://app.fir.ai/api/resource/xmind/download/'
    date_post = {'oid':'KBEjRn4eAz9Pm9el'}
    cookis_post = {'fir_session_id':'BO8yumVRUNJ5vGXgKiEMnHoqD1h6cWd2'}
    result = requests.post(url=url,data=date_post,cookies=cookis_post)
    print(result.status_code)
    print(result.text)



def tday():
    day1 = datetime
    print(day1)
def day2():

    url_s = UserProperty().url + "/api/TokenAuth/Authenticate"
    print(url_s)


if __name__ == "__main__":
    # check_grobid()
    # check_network()
    # check_ip()
    # test5()
    # get_xmind()
    # test_open()
    # tday()
    day2()