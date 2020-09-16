# coding=utf-8
import datetime
import random
import time

import requests
from concurrent.futures import ThreadPoolExecutor
import os
import json

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
    path = r'D:\work\3文档\招聘\abc.txt'
    path_2 = r'D:\work\3文档\招聘\d.txt'
    with open(path,'r+',encoding='utf-8') as file:
        s=file.readline()
        with open(path_2,'a+',encoding='utf-8') as file_2:
            for i in range(1,int(len(s)/10)):
                file_2.write(s[i*10:i*10+random.randint(0,20)])
                file_2.write('\n')

    print('操作完毕')



if __name__=='__main__':
    # one()
    # two(88488)
    # three()
    four()
    # getcut()
    # send_login()
    # getPrivateFile()
    # getTeamList()


