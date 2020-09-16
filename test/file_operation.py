# coding=utf-8

import os
import sys
import shutil
import requests
import json
from concurrent.futures import ThreadPoolExecutor

# 文件操作




# cody 文件
def copyFile():
    # path = r'D:\work\1测试\16测试数据\索引样本'
    path = os.path.dirname(os.path.abspath(__file__))
    firstFileName_s = os.listdir(path)
    for firstFileName in firstFileName_s:
        if os.path.splitext(firstFileName)[1]=='.py':
            continue
        else:
            srcpath = os.path.join(path, firstFileName)
            file_perfix = os.path.splitext(firstFileName)[0]
            file_suffix = os.path.splitext(firstFileName)[1]
            for i in range(1, 1000):
                newFileName = file_perfix + str(i) + file_suffix
                dstpath = os.path.join(path, newFileName)
                shutil.copyfile(srcpath, dstpath)
            break

    print('完成')

# 上传文件，团队批量上传
def uploadFile(file,file_name,team_id,pid=None,folder=None):
    cookie = {'fir_session_id':'j7hsvxe2llyqm10241n1tyory93yytoi'}
    url = 'https://testcyprex.fir.ai/api/resource/upload/whole/'
    # file_s = {'file':open( r'D:\work\1测试\1需求\历史版本\cyprex2.1.3\2.1.3 (2).xlsx','rb')}
    if isinstance(file,list):
        count=0
        for i in  file:
            try:
                if os.path.splitext(i)[1] != '.py'  and os.path.splitext(i)[1] != '.out':
                    file_s = {'file': open(os.path.join(folder,i), 'rb')}
                    file_name =i
                    if pid:
                        data_s = {'file_info':'{"name":"'+file_name+'","task_id":"8252101666"}','pid':pid,'team_id':team_id}
                    else:
                        data_s = {'file_info':'{"name":"'+file_name+'","task_id":"8252101666"}','team_id':team_id}
                    res = requests.post(url=url,data=data_s,files=file_s,cookies=cookie)
                    count+=1
                    print('序号：{}----状态{}'.format(count,json.loads(res.text).get('status')))
            except Exception as e:
                print(e)
                continue
    print('--执行完成--')

def manyThread():
    threads = ThreadPoolExecutor(max_workers=6)
    folder_path = os.path.dirname(os.path.abspath(__file__))
    team_id='9vmqkj8jJJ8rbZNB'
    pid = 'AxrEkReLba852BYa'
    file_name='a'
    files = os.listdir(folder_path)
    file_s = []
    num = int(len(files)/6)
    files_1 = files[0:num]
    files_2 = files[num:2*num]
    files_3 = files[2*num:3 * num]
    files_4 = files[3*num:4 * num]
    files_5 = files[4*num:5 * num]
    files_6 = files[5*num:]
    file_s.append(files_1)
    file_s.append(files_2)
    file_s.append(files_3)
    file_s.append(files_4)
    file_s.append(files_5)
    file_s.append(files_6)
    for i in range(6):
        future = threads.submit(uploadFile, file_s[i], file_name, team_id, pid, folder_path)
        print('启动线程')
    threads.shutdown(wait=True)







if __name__=='__main__':
    # copyFile()
    # uploadFile()
    manyThread()







