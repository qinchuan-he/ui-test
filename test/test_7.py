#coding=utf-8

import requests
import json
import time
from datetime import datetime
from time import sleep


# 检查线上公告和研报是否有索引,输出返回索引为空的


# 检查公告

cookie = {'fir_session_id':'bqgi8tsr6n6jwm095pixmi5zubc33853'}

def check_notice():
    # for i in range(1,21):
    #     print(i)
    for j in range(1,9):
        url = 'https://cyprex.fir.ai/api/resource/publicSearch/?url=%2Fresource%2FpublicSearch%2F&search_keywords=&' \
              'table_code=004&info_type=02&ordering=score&search_level=1&start_time=&end_time=&page_row=20' \
              '&page='+str(j)+'&author_list=%5B%5D&is_correct=true'
        res = requests.get(url=url,cookies=cookie)
        result = json.loads(res.text).get('data').get('results')[0].get('data_list')
        for i in result:
            if len(i.get('content'))==0:
                print('{},{}'.format(i.get('file_id'),i.get('content')))

# 检查研报
def check_report():
    for j in range(1,5):
        url ='https://cyprex.fir.ai/api/resource/publicSearch/?url=%2Fresource%2FpublicSearch%2F&search_keywords=' \
             '%E5%85%AC%E5%8F%B8&table_code=005&info_type=03&sub_info_type=0302&sub_info_type=0300&search_level=1' \
             '&ordering=score&start_time=&end_time=&page_row=20&page='+str(j)+'&author_list=%5B%5D&is_correct=true'
        res = requests.get(url=url, cookies=cookie)
        result = json.loads(res.text).get('data').get('results')[0].get('data_list')
        for i in result:
            if len(i.get('content')) == 0:
                print('{},{}'.format(i.get('file_id'), i.get('content')))

def check_search():
    cookie = {"fir_session_id":"dsez2cfq0j00lt4g9gof4f7qh6eecfb6"}
    search_key="研究"
    check_list = ["研究"]
    url = "https://testapp.fir.ai/api/resource/search/?search_keywords="+search_key+"&search_type=001" \
          "&start_time=&end_time=&is_correct=true&table_code=001&only_associate=0&pid=-1&ordering=score"

    res = requests.get(url=url,cookies=cookie)
    # 获取搜索页数
    pages = json.loads(res.text).get("data").get("page").get("total_pages")
    # print(pages)
    # 循环请求
    ctime=""
    utime=""
    name_list = [] # 存放所有标题
    content_list = [] # 存放所有摘要
    information_time_list = [] # 发布时间
    for i in range(pages): # 翻页查询
        url_new = "https://testapp.fir.ai/api/resource/search/?search_keywords="+search_key+"&search_type=001" \
              "&start_time=&end_time=&is_correct=true&table_code=001&only_associate=0" \
              "&pid=-1&ordering=score&page="+str(int(i)+1)+"&last=&ctime="+ctime+"&utime="+utime
        res_f = requests.get(url=url_new, cookies=cookie)
        r_json = json.loads(res_f.text) # 转换json
        for i in r_json.get("data").get("data_list"): # 循环返回结果列表
            name = i.get("name")
            norm_content = i.get("norm_content")
            ctime = str(int(i.get("ctime")))
            utime = str(int(i.get("utime")))
            information_time = i.get("information_time")
            name_list.append(name)
            content_list.append(norm_content)
            information_time_list.append(information_time)
    print(name_list)
    print(content_list)
    check_result=[0 for i in range(len(name_list))]
    for j in range(len(name_list)): # 检查标题排序，如果包含关键字标题前一标题不含就有问题

        for k in check_list: # 循环关键字
            if k in name_list[j]:
                check_result[j]=1
                continue
        if j>1:
            if check_result[j]==1 and check_result[j-1]==0:
                print(j)
                print("---搜索排序不对-------------------------------")
                break
    print("1是标题命中，0是正文命中")
    print(check_result)
    print(information_time_list)

def read_file_1():
    path = r'D:\work\1测试\16测试数据\te.out'
    path = r'D:\work\1测试\16测试数据\te_e (2).out'
    file = open(path,'r+', encoding='utf-8')
    time_sum=0
    count_s=0
    time_max=0
    for i in file.readlines():
        # print(i)
        js = json.loads(i)
        # print(js.get('msg').replace('writeSearch cost: ', ''))
        time_cost = float(js.get('msg').replace('writeSearch cost: ',''))
        # print(time_cost)
        # print(type(time_cost))
        time_sum += time_cost
        if time_cost>time_max:
            time_max=time_cost
        count_s+=1
    print(time_sum)
    print(count_s)
    print(time_sum/count_s)
    print(time_max)

def read_file_2():
    path = r'D:\work\1测试\16测试数据\te_e (2).out'
    file = open(path,'r+',encoding='utf-8')
    time_sum = 0
    count_s = 0
    time_max = 0
    for i in file.readlines():
        # print(i)
        # print(i[-8:-3])
        time_cost=float(i[-8:-3])
        # print(time_cost)
        time_sum+=time_cost
        if time_cost>time_max:
            time_max=time_cost
        count_s+=1
    print(time_sum)
    print(count_s)
    print(time_sum/count_s)
    print(time_max)


def read_file_3():
    path = r'D:\work\1测试\16测试数据\te.out'
    path = r'D:\work\1测试\16测试数据\te_e (2).out'
    path = r'D:\2\1.txt'
    file = open(path,'r+', encoding='utf-8')
    time_sum=0
    count_s=0
    time_max=0
    time_list=[]
    for i in file.readlines():
        # print(i)
        js = json.loads(i)
        # print(js.get('msg'))
        # r = js.get('msg').replace('annotation_search cost: ', '')
        # print(r)
        # print(js.get("asctime")[:-4])
        s = datetime.strptime(js.get("asctime")[:-4],'%Y-%m-%d %H:%M:%S')
        s_2 = datetime.strptime('2021-06-12 15:03:00', '%Y-%m-%d %H:%M:%S')
        # print(s)
        if s>s_2:
            time_cost = float(js.get('msg').replace('annotation_search cost: ', ''))
            # print(time_cost)
            # print(type(time_cost))
            # print(time_cost)

            time_sum += time_cost
            if time_cost>time_max:
                time_max=time_cost
            count_s+=1
    print(time_sum)
    print(count_s)
    print(time_sum/count_s)
    print(time_max)

def image2text():
    # url = 'http://120.92.85.191:6006/api/single_img'
    # url = 'http://ocrx.metasotalaw.cn/api/single_img'
    # url = 'http://192.168.1.27:6006/api/single_img'
    # url = 'http://testocr.fir.ai/api/single_img'
    url = 'http://114.84.16.8:6007/api/single_img'
    # url = ocr_url
    file_obj = r'D:\2\qq.png'
    files = {'file': open(file_obj,'rb')}
    time_1=time.time()
    time_sum = 0
    time_avg=0
    # for i in range(1,3):
    response = requests.post(url, files=files)
    # result 就彘??J???~P?°?~D达T佛~^??
    time_2 = time.time()
    result = response.json()
    print(result)
    # print(i)
    print(time_2-time_1)

    #     time_sum+=(time_2-time_1)
    # time_avg=time_sum/904
    # print(time_avg)

def qy():
    path = r'D:\2\cc.txt'
    file = open(path, 'r+', encoding='utf-8')
    fail_list=[223036,223766,223814,223829,223972,223985,223995,224006,224025,224036,224038,224041,224043,224045,224046,224047,224049,224056,224059,224061]
    result_list={}
    for i in file.readlines():
        id = int(i[:6])
        if id in fail_list:
            # print(id)
            # print(i[7:])
            result_list.setdefault(id,i[7:])
        # print(id)
    print(result_list)

def eight():
    position = ()
    result = []
    result_S=[]
    row=[]

    for k in range(1,9): #
        column = []
        for i in range(1,9): # 第一行到第八行
            for j in range(1,9): # 第一列到第八列
                a =0
                tmp = [i,j]
                # print(i)
                # print(tmp)
                tmp_s=[[i-1,j-1],[i+1,j-1],[i-1,j+1],[i+1,j+1],[i-1,j]]
                if not result:
                    column.append(j)
                    result.append([i,6])
                    # print('-')
                    break
                if tmp in result:
                    # print('--')
                    continue
                for s in tmp_s:
                    if s in result:
                        a=1
                        # print('---')
                        continue
                if a==1:
                    # print('----')
                    continue

                if j in column:
                    # print('-----')
                    continue
                column.append(j)

                result.append(tmp)
                # print(column)
                # print(result)
                # print('------------------------')
                break

        print(result)
        if len(result)==8:
            result_S.append(result)
            result = []
        else:
            result=[]
    print(result_S)

if __name__=='__main__':
    # check_notice()
    # check_report()
    # check_search()
    # read_file_3()
    # image2text()
    # qy()eight
    eight()