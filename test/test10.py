# coding=utf-8
import requests
import os
import json

def a_s():

    url = 'https://testcyprexplugsvc.fir.ai/resource/material/upload/'
    path = r'D:\work\1测试\回归\思维导图2\新建文件夹'
    # path = r'D:\work\1测试\回归\思维导图2\pdf'
    file_s = os.listdir(path)
    print(file_s)
    for i in file_s:
        data_s = {'file':i,'src_type':'C002'}
        files = {'file':open(os.path.join(path,i),'rb')}
        res = requests.post(url=url,data=data_s,files =files )
        print(res.text)




def a(s):

    url = 'https://testcyprexplugsvc.fir.ai/thirdParty/parse/'
    for i in s:
        data_s = {'neid':i,'opt_type':'01'}
        res = requests.post(url=url,data=data_s)
        print(res.text)

# 请求文件夹内容
def folder_list():
    cookie = {'fir_session_id':'c3yi0wiavv3fjne7c87ljgkh3pjultii'}
    url = 'https://testcyprex.fir.ai/api/resource/personal/list/?ordering=-utime&include=infoCat&include=info&pageRow=50&pId=Jed46RJmkW8Oyx2B'
    res = requests.get(url=url,cookies=cookie)
    file_list = json.loads(res.text).get('data').get('list')
    result = []
    for i in file_list:
        if  i is not None:
            result.append(i.get('id'))
    print(result)
    return result



if __name__=='__main__':
    # s = ['ZVGgb13kvzq1yrmN','vmqkj8jBn7B8rbZN','WkaXG1Qk0pq8NdEw','LnApb8zy7MaP7lDw','NqGWd1yadAl1ZkgL','VZKvJRNqAxd8oMGO','LZAeqPOqWNkRmOMJ','DrqxJ1x4Nej1Ql27']
    # s_2= ['Yz3jWPwnxYj1LO4X', 'BYvDV1AVLkEPbalW', 'ZnbexRpG4dk8VqwJ', '6zQlJPLMzb083n2O', 'en4E78GkQYw8zjNB', 'AxrEkReGDdAP52BY', 'AqN0l82W0MpRZKQo']
    # a(s)
    # a(s_2)
    # a_s()
    # s_3=['n9rGO8WLDjYRNa3k']
    s_4 = folder_list()
    a(s_4)



























