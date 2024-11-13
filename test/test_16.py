# 2023-01-28 测试自动化脚本
import json
import time
import os
import requests
from common.comfunction import *
import re
import html
import datetime


def test1():
    mode = 2
    driver = OpenBrowser(mode)
    User().login()



    sleep(5)
    CloseBrowsers()
    print('123')

def aac():
    url = "https://testapp.fir.ai/api/resource/doi/related_papers/?doi=10.1016%2Fj.dss.2020.113401"
    url = "https://testapp.fir.ai/api/resource/doi/related_papers/"
    cookies = {'fir_session_id':'W9Gyr4RxuQnq7g68mMfPAZLKai32bCTV'}
    data_s = {'doi': '10.1016/j.dss.2020.113401'}

    res = requests.get(url=url,cookies=cookies,params=data_s)
    result = json.loads(res.text)
    print(result)
    source_data = result['data']['source_data']
    print(source_data)
    for i in source_data:
        if len(i['doi']) > 7:
            print(data_s)
            # print(i['doi'])
        # print(i['doi'])

def count_grobid():
    # 统计命令5015服务器：cat cyprex.log.2023-07-07 | grep 'sync_grobid_upload_pdf_reference_handle_server get stream time' > 2023-07-07.txt
    path = r'D:\2\a.txt'
    file_name = '2023-09-26.txt'   # 文件名
    path = r'D:\2\{}'.format(file_name)  # 读取文件
    path_2 = r"D:\work\1测试\3测试报告\2023-09\grobid相关统计\{}".format(file_name)  # 写入文件
    count = 0
    file = open(path,'r',encoding='utf-8')
    a = []
    # print(file.readlines())
    file_time = open(path_2, 'w')
    for i in file.readlines():
        try:    # 2023-09-22 增加抛出异常,日志中匹配可能会匹配到错误数据
            js = json.loads(i)
            result_s = js["msg"].split("time:")[1]
            result = result_s.split(",")
            oid_s = result[2].split("resource_id:")[1].split("user_id:")
            oid = oid_s[0]
            user_id = oid_s[1]
            print(result[0], oid, user_id)
            file_time.write(result[0] + user_id + oid + "\n")
            count += 1
        except Exception as e:
            print(e)
            continue

    file_time.close()
    file.close()
    print("处理文件数：{}".format(count))


# 读取用户引用清单，查询数据库匹配文献信息
def readtxt():
    path = r'D:\2\新建文件夹\2.txt'

    file = open(path,'r',encoding='utf-8')
    from test.check_mysql import connection_mysql
    sql_s=[]
    s=1
    for i in file.readlines():
        # print(i)
        sql = "select id,resource_id,user_id, title from (SELECT * FROM resources_resourcedocumentationinfo " \
              "where user_id ='43330') as i where i.title ='{}'".format(i.split('\n',2)[0])
        sql_s.append(sql)
        s=s+1
        # if s==3:
        #     break
    # print(sql_s)
    ss = 'list'
    result,fail = connection_mysql(sql_s,datetype=ss,iscyprex=1)
    # print(result)
    for q in result:
        print(len(q),q)




def repairincite():








    infos = '[{"id":3336681,"source_info":{"a":"3"}}]'

    # infos = '[{"id":1735271,"source_info":{"a":"3"}},{"id":2112454,"source_info":{"a":"3"}}]'

    # infos = '[{"id":1884584,"source_info":{"a":"3"}},{"id":1884585,"source_info":{"a":"3"}}' \
    #         ',{"id":1695400,"source_info":{"a":"3"}}]'

    infos = '[{"id":1855550,"source_info":{"a":"3"}},{"id":1861395,"source_info":{"a":"3"}}' \
            ',{"id":1855552,"source_info":{"a":"3"}},{"id":1855551,"source_info":{"a":"3"}}]'

    block_id = '810b-8ae7-e8fd-ed4c-7edd'






    local_id = 'a435-da99-1181-d464-a10b'
    block_order = '["'+block_id+'"]'
    cookie_s = {'plugins_session_id':'y0kyt07w3j6zcaxnfoo5dhtzai5fv3iu'}
    url = 'https://searchpluginsvc.fir.ai/resource/cyprex/citation/add/'
    date_s = {'citation_infos':infos
        ,'local_id':local_id,'style':'apa','block_id':block_id
        ,'block_order':block_order}

    result = requests.post(url=url,data=date_s,cookies=cookie_s)
    print(result.text)

#读取TXT内容
def  count_user():
    pathj = r'D:\work\1测试\3测试报告\2023-06\重复购买用户数据.txt'
    file = open(pathj,'r')
    id_s=[]
    for i in file.readlines():
        # print(i)
        id = i.split(',',2)[0]
        # print(id)
        id_s.append(id)
    print(id_s)
    print(len(id_s))
    duplicates = set([x for x in id_s if id_s.count(x) > 1])
    print(duplicates)
    print(len(duplicates))

#读取TXT内容
def  check_article():
    path_title = r'D:\work\1测试\3测试报告\2023-06\引用文献题名含有html实体符号全库470万数据中_只有题名.txt'
    file = open(path_title,'r',encoding='utf-8')
    entity_s = []
    symbol = []
    for i in file.readlines():
        # print(i)

        entity = get_html_entity(i,type=2)
        # print(entity)
        if entity == None:
            return
        else:
            if len(entity) > 0:
                for j in entity:
                    entity_s.append(j)
    print("-------------------------")
    # print(entity_s)
    # print(len(entity_s))
    # 对列表去重
    list = set(entity_s)
    print(len(list))
    print(list)



# 处理传入的字符串，找出其中的&内容,使用正则匹配,返回数组
def get_html_entity(text,type=1):
    # 提取题名中的html实体
    if type==1:
        pattern = re.compile(r'&[A-Za-z0-9]+;')
        entities = pattern.findall(text)
        # print(entities)
        # return [html.unescape(entity) for entity in entities]
        return entities
    else:  # 提取题名中的括号和其中内容
        pattern = re.compile(r'&.*?&gt;')
        entities = pattern.findall(text)
        return entities
        # print(entities)






#读取TXT内容，检查bibtex是否有重复
def  check_bibtex():
    path_title = r'D:\work\1测试\3测试报告\2023-06\导出引用清单bibtex.txt'
    path_title = r'D:\work\1测试\3测试报告\2023-06\线上bibtex.txt'
    file = open(path_title,'r',encoding='utf-8')
    entity_s = []
    symbol = '@article'  # 期刊255,68
    symbol = '@book'  # 图书6,3
    symbol = '@phdthesis'  # 学位论文5,2
    symbol = '@inproceedings'  #会议论文7,2
    check_title = []
    s = file.readlines()
    j = -1
    check_name = []

    for i in s:
        # print(i)
        if symbol in i:
            # print(i)
            entity_s.append(i)
        if 'title = ' in s[j+1]:
            check_name.append(s[j].split('{',2)[0])
            check_title.append(i)
            # print(i)
        # print(s[j])
        j = j+1


    print("-------------------------")
    print(entity_s)
    print(len(entity_s))
    bibtex_s = set(entity_s)
    print(bibtex_s)
    print(len(bibtex_s))
    print(check_title)
    print(len(check_title))
    print(check_name)
    print(len(check_name))
    print(set(check_name))

# 访问url获取json数据然后进行筛选
def read_paper():
    file_path = r"D:\work\1测试\3测试报告\2023-06\grobid数据.txt"
    file = open(file_path,'r',encoding='utf-8')
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    for i in lines:
        # print(i)
        url2 = i
        result = requests.get(url=url2).text
        # print(url2)
        # print(result)
        s = "scattering theory for"
        s = "389.82"  # 查询坐标点位
        s = "http://dx.doi.org"  # 查询是否提取出doi
        s = "337.07"  #
        if s in result:
            print("-----------------------------存在")
            print(i)
        # else:
        #     print("-------------------------不存在-----")
        #     print(i)
        # break


# 读取xml文件内容，指定路径进行筛选内容
def check_xml():
    path = r"D:\work\1测试\3测试报告\2023-06\xml文献"
    file_names = os.listdir(path)
    # print(file_names)
    count = []
    for i in file_names:
        file_path = os.path.join(path,i)
        # print(file_path)
        result = open(file_path,'r',encoding='utf-8')
        content = result.readlines()
        # print(content)
        for i in content:
            # print(i)
            s = '10.1002/1097'
            if s in i:
                # print("----------------存在")
                # print(file_path)
                count.append(file_path)
        # break
    print(set(count))

# 获取指定目录下文件路径
def get_path():
    os_path = "D:\上传文件\pdf比对\9doi提取+智能提取\新智能提取--2023-06\作者名"
    os_path = "D:\上传文件\pdf比对\9doi提取+智能提取\新智能提取--2023-06\数字"
    os_path = r"D:\上传文件\pdf比对\7用户文件\英文\pdf50"
    os_path = r"D:\上传文件\pdf比对\7用户文件\83个文件"
    files = os.listdir(os_path)
    for i in files:
        file_path = os.path.join(os_path,i)
        print(file_path)


def abc():
    count = []
    fail = []
    for i in range(8):
        count.append(0)
        fail.append(0)
    print(count)
    print(fail)


if __name__ == '__main__':
    # test1()
    # aac()
    count_grobid()  # 获取grobid服务器执行时间
    # readtxt() # 读取用户引用清单，查询数据库匹配文献信息
    # repairincite()
    # count_user() # 读取TXT内容
    # check_article() # 读取TXT内容
    # check_bibtex()
    # read_paper()
    # check_xml()
    # get_path()
    # abc()




