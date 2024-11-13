# coding=utf-8
import datetime
import random
import time

import requests
from concurrent.futures import ThreadPoolExecutor
import os
import json
import re

# 私有搜索
def getcut():
    cookie = {'fir_session_id':'nk07oxnoo9q4m6pvlq86jx8kwm0cz2ef'}
    search_keywords='1 2 3 4 5 6 7 8 9'
    search_type='002'   # 001,002分别是私有和共享
    url = 'https://testcyprex.fir.ai/api/resource/search/?search_keywords='+search_keywords+'&search_type='+search_type+ \
          '&clickSearch=false&start_time=&end_time=&page_row=20&page=1&keywords_pos=0&info_type=&ordering=score&author_list=%5B%5D&is_correct=true'
    res = requests.get(url=url,cookies=cookie)
    result = json.loads(res.text)
    num = result.get('data').get('page').get('total_pages')
    word_segs = result.get('data').get('word_segs')
    # print(result)
    print('本次分词：{},页数：{}'.format(word_segs,num))
    for i in range(num):
        url = 'https://testcyprex.fir.ai/api/resource/search/?search_keywords='+search_keywords+ \
          '&search_type='+search_type+'&clickSearch=false&start_time=&end_time=&page_row=20&page='+str(i+1)+'&keywords_pos=0&info_type=' \
          '&ordering=score&author_list=%5B%5D&is_correct=true'
        res_1 = requests.get(url=url, cookies=cookie)
        result_1 = json.loads(res_1.text)
        data = result_1.get('data').get('data_list')
        for j in data:
            norm_content=j.get('norm_content')
            name = j.get('name')
            # print(type(norm_content))
            count=0
            for k in word_segs:
                if k in norm_content:
                    count+=1
                if k in name:
                    count+=1
            if count==0:
                print('--没有命中--{}-{}'.format(name,j.get('file_id')))



def send_login():
    url = 'https://testcyprexplug.fir.ai/api/account/user/login/'
    data={'mobile':'10025253635','password':'Test123456'}
    res = requests.post(url=url,data=data)
    print(res.text)

# 得到私有根目录下文件
def getPrivateFile():
    cookie = {'fir_session_id': '8nbf1f7ugta9sa1ntiuvgvb3aq22va7a'}
    url = 'https://testcyprex.fir.ai/api/resource/personal/list/?ordering=-utime&include=info&pageRow=50'
    res = requests.get(url=url,cookies = cookie)
    result = json.loads(res.text).get('data').get('list')
    tag_url = 'https://testcyprex.fir.ai/api/resource/tag/form/'
    tag_files = []
    for i in result:
        if i.get('id'):
            tag_files.append(i.get('id'))
            data = {'srcId':i.get('id'),'name':'贵州茅台的标签'}
            res_2 = requests.post(url=tag_url,data=data,cookies=cookie)
            print(res_2.text)
    print(tag_files)
    print(len(tag_files))

def getTeamList():
    cookie = {'fir_session_id':'n6jads9gz2drawbk3by7jbylzc1nr64m'}
    url = 'https://testcyprex.fir.ai/api/group/team/list/?ordering=-is_admin'
    url_invite = 'https://testcyprex.fir.ai/api/group/team/invite/url/'
    res = requests.get(url=url,cookies=cookie)
    teamList = []
    for i in json.loads(res.text).get('data').get('teamList'):
        data_invite={'teamId':i.get('id'),'reset':'1'}
        try:
            res_invite = requests.post(url=url_invite,data=data_invite,cookies=cookie)
            teamList.append(json.loads(res_invite.text).get('data').get('inviteUrl'))
        except Exception as e:
            continue
    print(teamList)



def one():
    s1 = 1598928105
    s2 = 1598899605
    s3 = datetime.datetime(2020, 9, 1, 10, 41, 11, 889703)
    s4 = datetime.datetime(2020, 9, 1, 2, 46, 9, 166411)
    print((s4-s3).seconds)
    # print(time.mktime(s3.timetuple()))
    # print(time.mktime(s4.timetuple()))
    # print(time.mktime(s4.timetuple())-time.mktime(s3.timetuple()))
    # print(time.time())
    s5 = datetime.datetime.now()
    s6 = s5+datetime.timedelta(hours=8)
    s7 = '2020-08-21 02:53:54.869610'
    # print(s5)
    # print(s6)

    s8 = datetime.datetime.strptime(s7,'%Y-%m-%d %H:%M:%S.%f')
    s9=s8+datetime.timedelta(hours=8)
    print(s8)
    print(s9)
    print(0-277)

def two(s:int):
    if s>=0:
        a = str(s)
        b=a[::-1]
        if a==b:
            # print('回文数')
            return True
        else:
            # print('不是回文数')
            return False
    else:
        # print('不是回文数')
        return False


def three():
    cookie = {'fir_session_id':'c0th7f4d3nw5486nnhef828m6qu1aivh'}
    url = 'https://cyprex.fir.ai/api/resource/data/fetch/extra/?view_type=search&pageType=previewSecondary&id=qVQzGPMoAMRY3w5y'
    res = requests.get(url=url,cookies=cookie)
    path = r'D:\work\3文档\招聘\abc.txt'
    with open(path,'w+',encoding='utf-8') as file:
        file.write(res.text)
    print('完毕')

def four():
    url = 'http://192.168.1.211:8030/user_data_index_233/user_data_index_233/91c18fce-7fa3-4cca-b24d-dace6ad5c771'
    res = requests.get(url=url)
    result=str(json.loads(res.text).get('_source').get('content'))
    s = result.replace(' ','')
    print(len(s))

    print('操作完毕')


def five():
    mob = '10025666973'
    company='!@#@$#%^'
    source='1001' # 官网-企业
    # source='1003' # 官网-个人
    url = 'https://testcyprexsvc.fir.ai/account/userInfoCollect/'
    if source=='1001':
        data = {'name': mob, 'phone': mob, 'company': company, 'source': source}
    else:
        data = {'name': mob, 'phone': mob, 'source': source}
    res = requests.post(url=url,data=data)
    print(res.text)

def six():
    url = 'http://192.168.1.225:8080/plugins/servlet/embedded-crowd/directories/troubleshoot/'
    data_s = {'username':'admin','password':'fir2018518','test':'测试设置','atl_token':'c6beade1dc846869f1ab2e4916fb37dcb76e69fe','directoryId':'10000',}
    res = requests.post(url=url,data=data_s)
    print(res.text)


def check_serch_repeat():
    compare = '1208318237'
    compare=[]

    cookie = {'fir_session_id':'vzc15ehmalssgxe8wv980ld28algrrbn'}
    url1='https://testcyprex.fir.ai/api/resource/publicSearch/?url=%2Fresource%2FpublicSearch%2F&search_keywords=%E5%9B%BD%E6%B3%B0%E5%90%9B%E5%AE%89%20%E5%90%88%E7%BA%B5%E7%A7%91%E6%8A%80%20%E8%88%AA%E5%8F%91%E5%8A%A8%E5%8A%9B&table_code=004&info_type=02&ordering=last_open_time&search_level=1&start_time=&end_time=&page_row=20&page=1&author_list=%5B%5D&is_correct=true'
    res1 = requests.get(url=url1,cookies=cookie)
    res1_json=json.loads(res1.text)
    for k in res1_json.get('data').get('results')[0].get('data_list'):
        compare.append(k.get('file_id'))
    print(compare)

    url = 'https://testcyprex.fir.ai/api/resource/publicSearch/?url=%2Fresource%2FpublicSearch%2F&search_keywords=%E5%90%88%E7%BA%B5%E7%A7%91%E6%8A%80%20%E5%9B%BD%E6%B3%B0%E5%90%9B%E5%AE%89&table_code=004&info_type=02&search_pattern=01&ordering=last_open_time&search_level=1&start_time=&end_time=&page_row=20&page=1&author_list=%5B%5D&is_correct=true&exclude_ids=1208534207&exclude_ids=1208317877&exclude_ids=1208534209&exclude_ids=1208534208&exclude_ids=1208318237'
    res = requests.get(url=url,cookies=cookie)
    result = json.loads(res.text)
    # print(result.get('data').get('results')[0].get('data_list')[0].get('file_id'))
    num = result.get('data').get('results')[0].get('page').get('total_pages')

    for i in range(1,num+1):
        url2 = 'https://testcyprex.fir.ai/api/resource/publicSearch/?url=%2Fresource%2FpublicSearch%2F&search_keywords=%E5%90%88%E7%BA%B5%E7%A7%91%E6%8A%80%20%E5%9B%BD%E6%B3%B0%E5%90%9B%E5%AE%89&table_code=004&info_type=02&search_pattern=01&ordering=last_open_time&search_level=1&start_time=&end_time=&page_row=20' \
               '&page='+str(i)+'&author_list=%5B%5D&is_correct=true&exclude_ids=1208534207&exclude_ids=1208317877&exclude_ids=1208534209&exclude_ids=1208534208&exclude_ids=1208318237'
        res2 = requests.get(url=url2,cookies=cookie)
        result2=json.loads(res2.text)
        data_list=result2.get('data').get('results')[0].get('data_list')
        for j in data_list:
            # print(j.get('file_id'))
            if j.get('file_id')==compare:
                print('存在相同的:{}页，file_id：{}'.format(i,compare))
            # if j.get('file_id')in compare:
            #     print('存在相同的:{}页，file_id：{}'.format(i,compare))
        if i >15:
            break

def test_date():
    now = time.time()
    now_1=now+183*24*60*60
    print(now)
    print(time.strftime('%Y-%m-%d',time.localtime(now_1)))

# 添加笔记接口
def test_note():
    cookie = {'fir_session_id':'jfa8xjj6gfhd2hnsspql7g6p3nhkv1z8'}
    url = 'https://testcyprex.fir.ai/api/resource/form/'
    url = 'https://testcyprex.fir.ai/api/resource/fragment/reference/'
    data_s = {'resource_list':'[{"type":"info","content":"小舟从此逝，沧海寄余生","createType":400,"contentType":901'
                              ',"isDataCollect":1,"origId":"n9rGO8WLQabRNa3k","name":"点点.html"}]'}
    data_s = {'resource_id':'NqGWd1yaDjV1ZkgL','action':'import','orign_id':'n9rGO8WLQabRNa3k','draft_title':'验证图例文件.pdf','orign_content':'江海寄余生','author':'czq'}
    for i in range(9):
        res = requests.post(url=url,data=data_s,cookies=cookie)
        print(res.text)


def test_add_flow():
    cookie = {'fir_session_id': '50zz5xnhuer5p96ckhpbzpmdr4f0i1em'}
    url = 'https://testapp.fir.ai/api/send/flow/'
    data_s = {'user_id': '1415'}
    res = requests.post(url=url, data=data_s, cookies=cookie)
    print(res.text)



def acc():
    s = 'https://testimages.fir.ai/show/?id=beb59c8c-726e-464b-a16a-a88d707ce159?_=1636014968737'
    ss = re.search('\?(.*)\?', s)
    print(ss)
    print(ss.groups())


def search_ip():
    url='http://ip.t086.com/?ip=210.36.46.171'
    res = requests.get(url)
    content = res.text
    print(content.split('title>')[1])

    file_path = r'D:\ip查询\ip.txt'
    text = open(file_path,'r')
    for ip in text.readlines():

        url = 'http://ip.t086.com/?ip={}'.format(ip)
        res = requests.get(url)
        content = res.text
        print(content.split('title>')[1])

def testccc():
    # time_s = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    # print(time_s)
    print("7"+"1")
    print(7+1)
    print(10/3)
    print(round(10/3, 2))
    print(10**(1/3))
    print(9**(1/2))
    a = 'aa'
    print(a)
    print("a")
    print("you are " + "so nice")





if __name__=='__main__':
    # one()
    # two(88488)
    # three()
    # four()
    # five()
    # six()
    # getcut()
    # send_login()
    # getPrivateFile()
    # getTeamList()
    # check_serch_repeat()
    # test_date()
    # test_note()
    # test_add_flow()
    # acc()
    #search_ip()
    testccc()