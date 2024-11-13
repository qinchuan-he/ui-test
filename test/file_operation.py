# coding=utf-8

import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)
import shutil
import requests
import json
import pymysql
from concurrent.futures import ThreadPoolExecutor
from common.private import UserProperty,DB,InterBaseUrl
from common.decode import cyprex_decode
import time
from time import sleep
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

# 检查上传文件是否生成对应job任务（word+pdf）,传入文件，加长等待时间是因为，发现实际线上比较慢
def check_parsejobs(file,fir_session_id=None):
    # 需要检查的任务
    #word_jobs = ['to_html','to_pdf','to_content','bookmarks','thumbnail','extract_pagenum','extract_images']
    word_jobs = ['to_content']
    pdf_jobs = ['to_html','to_content','to_html','txt_format','thumbnail','extract_images','file_tables']
    # 1.准备上传，
    if fir_session_id:
        cookie = {'fir_session_id':fir_session_id}
    else:
        cookie = {'fir_session_id':'nbony33gvvd8onrmalf5ae5lulohq8jo'}
    url = InterBaseUrl().Base_url+'/resource/upload/whole/'  # 上传接口
    url_2 = InterBaseUrl().Base_url+'/resource/new/parse/'  # 手动触发解析接口
    file_s={'file':open(file,'rb')}
    data_s={'file_info': '{"name":"'+os.path.split(file)[1]+'","task_id":'+str(time.time())+'}'}
    res = requests.post(url=url,data=data_s,files=file_s,cookies=cookie)
    # print(res.text)
    # 获取上传成功返回id
    id_encryption=json.loads(res.text).get('data').get('meta_info').get('id')
    # 2020-12-08 增加，手动点击解析任务
    data_2 = {'oid':id_encryption}
    res_2 = requests.post(url=url_2,data=data_2,cookies=cookie)
    print(res_2.text)
    id = cyprex_decode(id_encryption)
    print(id)
    sleep(12) # 上传成功之后等待一定时间生成任务
    # 通过id获取到file_id
    host = DB.host
    db_c = DB.db_cyprex
    db_s = DB.db_storage
    port=int(DB.port)
    user = DB.user
    pwd=DB.pwd
    char_set='utf8'
    connection_1 = pymysql.connect(host=host,port=port,database=db_c,user=user,password=pwd,charset=char_set)
    connection_2 = pymysql.connect(host=host,port=port,database=db_s,user=user,password=pwd,charset=char_set)
    cur1 = connection_1.cursor()
    cur2 = connection_2.cursor()
    sql_1 = 'select fileId from resources_resourcedatads where resource_id={}'.format(id)
    job_list = []
    file_id=''
    try:
        cur1.execute(sql_1)
        connection_1.commit()
        file_id=cur1.fetchone()[0] # 获取查询结果第一个中的第一个结果（只有这唯一一个结果）
        cur1.close()
        print(file_id)
        sleep(28)  # 等待job任务生成
        #  通过file_id 查询是否生成任务
        if file_id:
            sql_2 = "select extract_code from jobs_extractjob where file_id='{}'".format(file_id)
            cur2.execute(sql_2)
            connection_2.commit()
            jobs=cur2.fetchall()
            cur2.close()
            print(jobs)
            for i in jobs:
                # print(i)
                job_list.append(i[0]) # 元组转换成数组
        else:
            print('未获取到file_id')

    except Exception as e:
        # connection_1.rollback()  # 查询不需要回滚
        # connection_2.rollback()
        print(e)
    # finally:
    # print(job_list)
    connection_1.close()
    connection_2.close()
    suffix = os.path.splitext(file)[1]
    result_msg = ''
    if suffix.lower() in ['.docx','.doc']:
        for i in word_jobs:
            if i not in job_list:
                print('上传word文件没有生成 {} 任务'.format(i))
                result_msg = result_msg + i +'，'
        if len(result_msg)>0:
            # result_msg=result_msg[:-1:]
            result_msg =   '上传word文件没有生成：' + result_msg[:-1] + '任务。file_id：'+file_id+'<br>'

    elif suffix.lower() =='.pdf':
        for i in pdf_jobs:
            if i not in job_list:
                print('上传pdf文件没有生成 {} 任务'.format(i))
                result_msg = result_msg + i +'，'
        if len(result_msg)>0:
            # result_msg = result_msg[:-1:]
            result_msg =  '上传pdf文件没有生成：' + result_msg[:-1] + '任务。file_id：'+file_id+'<br>'
    else:
        print('上传格式不对')
    # 检查完成之后删除文件
    url_2 = InterBaseUrl().Base_url+'/resource/merge/delete/'
    data_s2 = {'src_list': '[{"id":"'+id_encryption+'","type":"info"}]'}
    res2 = requests.post(url=url_2,data=data_s2,cookies=cookie)
    print(res2.text)
    if len(result_msg)==0:
        print('任务都生成了')
    return result_msg




# 线程池
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
        print('启动线程池')
    threads.shutdown(wait=True)







if __name__=='__main__':
    # copyFile()
    # uploadFile()
    # manyThread()
    file = os.path.join(r'D:\上传文件\自动化验证文档\回归的word文档.docx')
    file = os.path.join(r'D:\上传文件\自动化验证文档\2018-0403_origin.pdf')
    check_parsejobs(file)






