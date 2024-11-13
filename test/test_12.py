import json
import os

import pytest

import pymysql
from collections import Counter
import requests


def connection_mysql(sql_list):
    ip = '192.168.1.214'
    port = 3306
    username = 'kaifa'
    password = 'kaifazufir2018518'
    conn = pymysql.connect(host=ip,database='test',port=port,user=username,password=password)
    cur = conn.cursor()
    # sql = 'insert into baidu_translate(userId)  values(82713);'
    sql = 'insert into baidu_translate(userId)  values(%s);'
    # cur.execute(sql)
    cur.executemany(sql,sql_list)
    # try:
    #     for i in sql_list:
    #         cur.execute(i)
    # except Exception as e:
    #     print(e)

    conn.commit()
    cur.close()
    conn.close()

# 读取文件 这次是把日志中的内容转成json之后输出-2022-07-19
def insert_text():
    file_path = r'D:\2\5013.txt'
    file = open(file_path,'rb')
    a = file.readlines()
    # print(a)
    sql_list = []
    data_list = []
    for i in a:
        a = str(i,'utf-8')
        msg = a.split('"msg":"')[1]
        msg_s = msg.split(',"post_params":')
        info = msg_s[0] + '}'
        json_info = json.loads(info)
        data = msg_s[1].replace('\\"','"')
        # print(data)
        data_name = data.split('"name":"')[1].split('"')[0]
        print(json_info['userId'], ',', data_name)

        # print(type(json.loads(b)))



def acc():
    a = '{"asctime":"2022-07-15 06:36:44,117","thread":140144628467456,"request_id":"3a4f401e46694806a2905c7294ea3306","lineno":340,"module":"enter_log","level":"INFO","msg":"{"remote_ip":"39.155.10.85","type":"request","method":"POST","path":"/resource/upload/whole/","user":15949434787,"userId":86426,"source":9999,"get_params":{},"post_params":{"Cookie": ["fir_session_id=<null>"], "app_upload": ["1"], "bookmark": ["[]"], "box_highlight": ["[]"], "file_info": ["{\"name\":\"汉语介词及介词短语再演化的模式、动因与功用_张谊生-1.pdf\",\"task_id\":\"c8a6a8c4cd93afcc7b8ad76db1bd5a81_root_root_1657838203000\"}"], "highlight": ["[]"], "ink_note": ["[]"], "page_note": ["[]"], "remark": ["[]"], "strikeline": ["[]"], "underline": ["[]"]}}"}'
    b = '{"asctime":"2022-07-15 06:36:44,117","level":"INFO","msg":"{"remote_ip":"39.155.10.85","path":"resource/upload/whole","get_params":{},"post_params":{"Cookie": ["fir_session_id=<null>"], "app_upload": ["1"],"underline": ["[]"]}}"}'
    # print(type(json.loads(b)))
    # print(type(eval(a)))
    q = a.split('"msg":"')[0]+'"test":"test"}'
    msg = a.split('"msg":"')[1]
    msg_s = msg.split(',"post_params":')
    info = msg_s[0]+'}'
    json_info = json.loads(info)
    print(type(json_info))
    print(type(json.dumps(json_info)))
    data = msg_s[1]
    data_name = data.split('["{"name":"')[1].split('","task_id"')[0]
    # print(json_info['userId'],',', data_name)


def check_json():
    path = r'D:\work\1测试\5部署+配置\客户端\测试环境\20220721\pdf_demo\a.txt'
    path2 = r'D:\work\1测试\5部署+配置\客户端\测试环境\20220721\pdf_demo\a_1.txt'
    file = open(path, 'rb')
    file1 = open(path2, 'rb')
    a = file.readlines()
    e = file1.readlines()
    c = ''
    f = ''
    parser_title = []
    saas_title = []

    for i in a:
        b = str(i,'utf-8')
        c =c + b
    json_1 = json.loads(c)

    for i in e:
        q = str(i,'utf-8')
        # print(q)
        f =f + q
    json_2 = json.loads(f)
    # print(json_2)
    for i in json_2['data']['source_data']:
        qq = i['title'].replace('<i>','')
        qq_2 = qq.replace('</i>','')
        saas_title.append(qq_2)
        print(qq_2)




    for i in json_1['data']['reference']:
        # print(i['title'])
        parser_title.append(i['title'])
    # print(parser_title)
    cc = []
    for i in parser_title:
        if i not in saas_title:
            # print(i)
            cc.append(i)
    # print(len(cc))

# 处理日志数据
def parse_json():
    file_path = r'D:\2\max.txt'
    file = open(file_path, 'rb')
    data = file.readlines()
    # print(type(data))
    userid_list = []
    for i in data:
        # print(i)
        s = str(i,'utf-8')
        # print(s)
        # print(type(s))
        msg = s.split('"msg":"',2)[1]
        # print(type(msg))
        # print(msg)
        link = msg.split(',"source":',2)[0]
        # print(link)
        link_js = link+'}'
        # print(link_js)
        info_js = json.loads(link_js)
        # print(info_js)
        USERID = info_js['userId']
        # print(info_js['userId'])
        userid_list.append(USERID)
        # break
    print(userid_list)
    print(list(set(userid_list)))
    count = Counter(userid_list)
    print(count)
    print(count.get(39647))
    print(count.most_common(1))


def cca():
    d= r'D:\work\1测试\3测试报告\202208\新建文件夹'
    path22 = r'D:\work\1测试\3测试报告\202208\新建文件夹\20220822.txt'
    path23 = r'D:\work\1测试\3测试报告\202208\新建文件夹\20220823.txt'
    path24 = r'D:\work\1测试\3测试报告\202208\新建文件夹\20220824.txt'
    path25 = r'D:\work\1测试\3测试报告\202208\新建文件夹\20220825.txt'
    path26 = r'D:\work\1测试\3测试报告\202208\新建文件夹\20220826.txt'
    path28 = r'D:\work\1测试\3测试报告\202208\新建文件夹\20220828.txt'
    path27 = r'D:\work\1测试\3测试报告\202208\新建文件夹\20220827.txt'
    print(os.listdir(d))
    print(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    file28 = open(path28,'r').readlines()
    file27 = open(path27,'r').readlines()
    file26 = open(path26, 'r').readlines()
    file25 = open(path25, 'r').readlines()
    file24 = open(path24, 'r').readlines()
    file23 = open(path23, 'r').readlines()
    file22 = open(path22, 'r').readlines()
    # print(file28)
    # 3日返回率，3天内有过再次登录行为,高频就是每天都有登录
    in3 = file28+file27+file26
    in3_count = Counter(in3)
    in3_result = 0
    for i in in3_count:
        if in3_count.get(i) > 1:
            in3_result=in3_result+1

    hig3 = set(file28)&set(file27)&set(file26)
    print('{:.2%}'.format(in3_result/91129))  # 3日返回率
    print('{:.2%}'.format(len(hig3)/91129))  # 3日高频返回

    in7 = file28+file27+file26+file25+file24+file23+file22
    hig7 = set(file28)&set(file27)&set(file26)&set(file25)&set(file24)&set(file23)&set(file22)
    in7_count = Counter(in7)
    in7_result = []
    for i in in7_count:
        if in7_count.get(i) > 1:
            in7_result.append(i)

    # print(len(in7_result))
    print('{:.2%}'.format(len(in7_result)/91129))
    print('{:.2%}'.format(len(hig7)/91129))


    # a = [1,2,2,3]
    # b = [1,5,6]
    # c = [2,6,7]
    # c = a+b
    # print(set(a)&set(b)|set(a)&set(c))
    # print(set(c))

# 智能列表添加
def  add_smaretList():
    url = 'https://testapp.fir.ai/api/resource/smart_list/add/'
    cookie = {'fir_session_id':'kitsohg527oovjf1gpimy6ifxtowri6l'}
    datas = {'id':'ELnApb8zkkR7lDwZ','res_id_list':'["Yz3jWPwnJw41LO4X"]'}

    datas = {'id': 'ELnApb8zkkR7lDwZ', 'res_id_list': '["122415","122475","122476","122479","122480","122481","122660","127221","127222","127237","127238","130209","132675","133189","133394","133397","133553","133554","133558","133559","133590","133591","133592","133732","136702","137996","138063","138128","138148"]'}

    res = requests.post(url=url,data=datas,cookies=cookie)
    print(res.text)

def read_txt():
    path = r"D:\2\5013.txt"
    file_s = open(path,'rb')
    # print(file_s.readlines())
    lins = file_s.readlines()
    for i in lins:
        # print(i)
        s = str(i, 'utf-8')
        result = s.split("[")[1].split("]")[0]
        print(result)


def check_json():
    host_name = "192.168.1.214"
    db_name = "cyprex_test"
    db_port = 3306
    db_user = "kaifa"
    db_pwd = "kaifazufir2018518"
    conn = pymysql.connect(host=host_name, database=db_name, port=db_port, user=db_user, password=db_pwd)
    cur = conn.cursor()
    result = []

    sql = "SELECT * FROM `resources_externalshare` where slug = '12c070ed'"
    cur.execute(sql)
    result = cur.fetchall()
    data = result[0].listJson()
    cur.close()
    conn.close()
    print(data)


if __name__ == "__main__":
    # sql_list = insert_text()
    # connection_mysql(sql_list)
    # acc()
    # check_json()
    # parse_json()
    # cca()
    # add_smaretList()
    # read_txt()
    check_json()




