

import requests
from common.comInterfaceUrl import InterfaceUrl
from common.private import InterBaseUrl
from common.comfunction import url22
import time
import json
from time import sleep
from common.comfunction import OpenBrowser,User
import openpyxl
import os
import re
# r = requests.post('https://testcyprexsvc.fir.ai/account/user/judge/register/',data={'key':'mobile','value':'13245698565'})
# 性能测试造数据用，目前主要调用金山接口
def analysis():
    """ 数据组pdf公告解析接口"""
    url = 'http://192.168.1.219:8016/data/api/algorithm/algorithm'
    argument = {'algo_type':'pdf2html','pdf_type':'notice'}
    argument = {'algo_type':'pdf2html','pdf_type':'report'}
    folder_path = 'D:\\上传文件\\pdf比对\\数据组--样本文件\\研报'
    # file_bash_pash = 'D:\\上传文件\\pdf比对\\数据组--样本文件\\'
    lst = []
    for i in os.listdir(os.path.join(folder_path)):
        # file_path = file_bash_pash+i
        file_path = os.path.join(folder_path,i)
        print(file_path)
        file = {'file': open(file_path, 'rb')}
        res = requests.post(url,data=argument,files=file)
        res_text=res.text
        print(res_text)
        try:
            res_j = json.loads(res_text).get('data')
            lst.append(res_j)
        except Exception as e:
            print('这个解析失败了')

    print('-------------------------------')
    print(lst)

def test(s):
    ss =re.search("'(.*?)'",str(s)).group()
    print(ss[1:-1])

def king_upload():
    """ 金山文档，上传"""
    cookie = {'wpsua':'V1BTVUEvMS4wICh3ZWIta2RvY3M6Q2hyb21lXzc5LjAuMzk0NS44ODsgTWljcm9zb2Z0IFdpbmRvd3M6V2luZG93cyAxMC4'
                      'wOyBnWlUxejFZTlN3U18yOVBkNDlKYU13PT06ZFc1cmJtOTNJQ0IxYm10dWIzYz0pIHVua25vdy91bmtub3c',
              # 'singleSignStart':'1586421081471',
              'wps_sid':'QIbM8ay_x4Le0k43HdT5s06afc782d00233ec4c4',
              'csrf':'m2Bbsdxa6T5WinWZWQWrkx72XmmRDWJp',
              'visitorid':'243296296',
              'Default':'DESC-mtime',
              'singleSignTime':'80132414'
              }


    # 前置接口
    url_0 = 'https://www.kdocs.cn/3rd/drive/api/v3/groups/670954879/files/permission/assert?fileid=65086883704&assert_perm=modify&parentid=-1'
    res = requests.get(url_0,cookies = cookie)
    print(res.text)

    # 第一个接口 /api/files/upload/request
    king_bash_url='https://www.kdocs.cn'
    k_url_1 = king_bash_url+'/3rd/drive/api/files/upload/request'

    argument={'groupid':'670954879','parentid':'65086883704','size':'547','name':'jmeter与jdk的配置.txt',
              'store':'ks3','method':'POST','encrypt':'true'
              }
    res_1 = requests.get(k_url_1,params=argument,cookies=cookie)
    res_data = res_1.text
    print(res_data)
    res_data_json = json.loads(res_data)

    # 第二个接口 https://wpsfile.ksyun.com/ 这里上传文件了
    k_url_2 = 'https://wpsfile.ksyun.com/'
    file = {'file':open('D:\\1软件\\jmeter\\jmeter-4.0及相关文档\\Jemter\\文件资料\\463040.txt','rb')}
    argument_2 ={'key':res_data_json.get('key'),'Policy':res_data_json.get('Policy'),'submit':res_data_json.get('submit')
        ,'KSSAccessKeyId':res_data_json.get('KSSAccessKeyId'),'x-kss-newfilename-in-body':res_data_json.get('x-kss-newfilename-in-body')
        ,'x-kss-server-side-encryption':res_data_json.get('x-kss-server-side-encryption'),'Signature':res_data_json.get('Signature')}
    res_2 = requests.post(k_url_2,data=argument_2,cookies = cookie,files=file)
    res_data_2 = res_2.text
    print(res_data_2)
    res_data_json_2 = json.loads(res_data_2)
    # 第三个接口  上传文件第三个接口
    headers={'content-type':'application/json'}
    k_url_3 = 'https://www.kdocs.cn/3rd/drive/api/v5/files/file'
    argument_3 = {'groupid':670954879,'parentid':'65086883704','parent_path':[],'name':'463040.txt','isUpNewVer':'false'
        ,'etag':'25a55f1d56bba824f0687360307c045d','store':'ks3','size':40,'sha1':res_data_json_2.get('newfilename'),'csrfmiddlewaretoken':'Kkx632wRHpHMBQsKrY7KKp2CPX2nxbAy'}
    print(argument_3)
    argument_4 = {"groupid":670954879,"parentid":"65086883704","parent_path":[],"name":"463040.txt","isUpNewVer":"false","etag":"25a55f1d56bba824f0687360307c045d","store":"ks3","size":40,"sha1":"3340bab03b68cc279663d7d946b2b318498993cf","csrfmiddlewaretoken":"Kkx632wRHpHMBQsKrY7KKp2CPX2nxbAy"}
    argument_4 = json.loads(str(argument_4).replace("'",'"'))
    print(argument_4)
    res_3 = requests.post(k_url_3,data=None,json =argument_4, cookies = cookie,headers=headers)
    print(res_3.text)

def king_create():
    """ 创建文件 根据文件夹调整参数pid"""
    cookie = {'wpsua':'V1BTVUEvMS4wICh3ZWIta2RvY3M6Q2hyb21lXzc5LjAuMzk0NS44ODsgTWljcm9zb2Z0IFdpbmRvd3M6V2luZG93cyAxMC4'
                      'wOyBnWlUxejFZTlN3U18yOVBkNDlKYU13PT06ZFc1cmJtOTNJQ0IxYm10dWIzYz0pIHVua25vdy91bmtub3c=',
              # 'singleSignStart':'1586421081471',
              'wps_sid':'V02SgNrwE-QIbM8ay_x4Le0k43HdT5s06afc782d00233ec4c4',
              'csrf':'m2Bbsdxa6T5WinWZWQWrkx72XmmRDWJp',
              'visitorid':'243296296',
              'Default':'DESC-mtime',
              # 'singleSignTime':'80132414'
              }
    url = 'https://www.kdocs.cn/api/office/files2?from=docs&source=docsWeb'
    argument = {"type":"wps","tid":0,"gid":"670954879","pid":"0"}
    headers = {'content-type':'application/json'}
    res = requests.post(url,data=None,json=argument,cookies=cookie,headers = headers)
    print(res.text)

def king_create_folder():
    """ 创建文件夹,为了造数据，目前某些参数写死"""
    url = 'https://www.kdocs.cn/3rd/drive/api/v5/files/folder'
    cookie = {'wpsua':'V1BTVUEvMS4wICh3ZWIta2RvY3M6Q2hyb21lXzc5LjAuMzk0NS44ODsgTWljcm9zb2Z0IFdpbmRvd3M6V2luZG93cyAxMC4'
                      'wOyBnWlUxejFZTlN3U18yOVBkNDlKYU13PT06ZFc1cmJtOTNJQ0IxYm10dWIzYz0pIHVua25vdy91bmtub3c=',
              # 'singleSignStart':'1586421081471',
              'wps_sid':'V02SgNrwE-QIbM8ay_x4Le0k43HdT5s06afc782d00233ec4c4',
              'csrf':'m2Bbsdxa6T5WinWZWQWrkx72XmmRDWJp',
              'visitorid':'243296296',
              'Default':'DESC-mtime',
              # 'singleSignTime':'80132414'
              }
    argument = {'groupid':'670954879','parentid':0,'name':'hello'+str(time.time()),'parsed':'true','owner':'true','csrfmiddlewaretoken':'m2Bbsdxa6T5WinWZWQWrkx72XmmRDWJp'}
    res = requests.post(url,data=None,json=json.loads(str(argument).replace("'",'"')),cookies = cookie)
    print(res.text)


import hashlib
def md5Encode(args):
    m = hashlib.md5(args.encode(encoding="utf-8"))
    return m.hexdigest()


def sha1Encode(args):
    m = hashlib.sha1(args.encode(encoding="utf-8"))
    return m.hexdigest()


if  __name__=='__main__':
    analysis()   # 数据组公告接口
    # test("<a href='http://124.77.120.212:9650/apis/download/?data_id=66fd27c2-7a64-11ea-9d68-0242ac110008'>结果地址</a>")
    # king_upload()
    # print(md5Encode('b8cdca3870d35e40776ca7387c8a7ed0'))
    # for i in range(90):
    #     king_create()
    # print('循环完毕')
    # for i in range(18):
    #     king_create_folder()





