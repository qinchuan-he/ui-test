# coding=utf-8
import threading

import requests
from concurrent.futures import ThreadPoolExecutor
import os
import json


# 项目中批量上传
def one(file,file_name,team_id,pid=None,folder=None):
    cookie = {'fir_session_id':'8nbf1f7ugta9sa1ntiuvgvb3aq22va7a'}
    url = 'https://testcyprex.fir.ai/api/resource/upload/whole/'
    # file_s = {'file':open( r'D:\work\1测试\1需求\历史版本\cyprex2.1.3\2.1.3 (2).xlsx','rb')}
    print(threading.current_thread().name)
    if isinstance(file,list):
        for i in  file:
            file_s = {'file': open(os.path.join(folder,i), 'rb')}
            file_name =i
            if pid:
                data_s = {'file_info':'{"name":"'+file_name+'","task_id":"8252101666"}','pid':pid,'team_id':team_id}
            else:
                data_s = {'file_info':'{"name":"'+file_name+'","task_id":"8252101666"}','team_id':team_id}
            res = requests.post(url=url,data=data_s,files=file_s,cookies=cookie)

            print(json.loads(res.text).get('status'))
    print('--执行完成--')


def run_request():
    threads = ThreadPoolExecutor(max_workers=6,thread_name_prefix="test_")
    pid_s=['nW4wNRDxnXRMlqXJ','mplArPENnZ8B5J6W','OM3GBRVwDV1dYAm2','OJ04rPoBjX1957MK','94QyWRlnLWPpwXve','jVN9lPqA44PoA2vO']
    folder=r'D:\上传文件\pdf比对\1专业数据\数据组--公告企微'
    file_s=os.listdir(folder)
    file_name = 'test'
    team_id = 'QOM3GBRVOE1dYAm2'
    for i in range(6):
        print(pid_s[i])
        # future = threads.submit(one(file_s,file_name,team_id,pid_s[i],folder), i)
        future = threads.submit(one, file_s, file_name, team_id, pid_s[i], folder)
        print('*****************')
        # future.add_done_callback(one(file_s,file_name,team_id,pid_s[i],folder))
        # print('-----------')
    threads.shutdown(wait=True)


def three():
    folder = r'D:\上传文件\pdf比对\1专业数据\数据组--公告企微'
    file_s = os.listdir(folder)
    print(file_s)
    print(type(file_s))
    if isinstance(file_s,list):
        print('----')
    s = '_ST皇台：关于重大资产重组的进展公告.pdf'
    print(os.path.splitext(s)[0])

if __name__=='__main__':
    # three()
    run_request()




