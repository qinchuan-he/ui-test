# coding = utf-8
import requests
import time
import threading
import os
import pymysql
from common.private import DB
import re

def request():
    print('hahha')


class mythread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        request()
        print(self.id)

def start_thread():

    for i in range(3):
        a = mythread(i)
        a.start()
        a.join()
    # a1 = mythread()
    # a2 = mythread()
    # a3 = mythread()
    #
    #
    # a1.start()
    # a2.start()
    # a3.start()
    #
    # a1.join()
    # a2.join()
    # a3.join()


def quest():
    cookie = {'fir_session_id':'62q5rernrq2on6qrcvmxb5kkrwj1cwml'}
    url = 'https://testcyprex.fir.ai/api/company/resource/cat/create/'
    data = {}


# def  openfile():
#     file = open(os.path.join(os.path.dirname(__file__),'b.json'),encoding='utf-8')
#     t = json.load(file)
#     print(t)
#     for i in t:
#         print(i)
#         for j in i.get('value'):
#             print(j)
#             print(j.get('value'))


def three():
    url = r'D:\work\1测试\3测试报告\日报\前端日志\cyprex_web\cyprex_web.log.2020-07-18'
    folder = r'D:\work\1测试\3测试报告\日报\前端日志\cyprex_web'
    files = os.dir(folder)

    for s in files:
        file_url = os.path.join(folder,s)
        # print(file_url)
        b = []
        file = open(file_url, 'r+', encoding='utf-8')
        for i in file.readlines():
            # print(i)
            a = []
            asctime = re.findall('"asctime":"(.*?)"',i)
            # if asctime[0]=='2020-07-18 10:48:01,488':
            type = re.findall('"type":"(.*?)"',i)
            message = re.findall('"message":"(.*?)"', i)
            detail = re.findall('"detail":{(.*?)}', i)
            detail_req = re.findall('"request":"(.*?)"',i)
            detail_res = re.findall('"response":{(.*?)}',i)
            current_url = re.findall('"currentURL":"(.*?)"',i)
            user = re.findall("'name': '(.*?)',", i)
            browser_name = re.findall('"userAgent":"(.*?)"', i)
            # print(asctime[0])
            a.append(str(asctime[0]).replace(',','.'))
            # a+(str(asctime[0]).replace(',','.'))
            if type:
                try:
                    # print(type[1])
                    a.append(type[1])
                    # a+(str(type[1]))
                except:
                    a.append("")
            else:
                a.append("")
            if message:
                # print(message[0])
                a.append(message[0])
                # a+(str(message[0]))
            else:
                a.append("")
            if detail:
                # print(detail[0])
                a.append(detail[0])
                # a+(str(detail[0]))
            else:
                a.append("")
            if detail_req:
                # print(detail_req[0])
                a.append(detail_req[0])
                # a+(str(detail_req[0]))
            else:
                a.append("")
            if detail_res:
                # print(detail_res[0])
                a.append(detail_res[0])
                # a+(str(detail_res[0]))
            else:
                a.append("")
            if current_url:
                # print(current_url[0])
                a.append(current_url[0])
                # a+(str(current_url[0]))
            else:
                a.append("")
            if user:
                # print(user[0])
                a.append(user[0])
                # a+(str(user[0]))
            else:
                a.append("")
            if browser_name:
                # print(browser_name[0])
                a.append(browser_name[0])
                # a+(str(browser_name[0]))
            else:
                a.append("")
            c = tuple(a)
            d = []
            d.append(c)
            # print(d)
            b.append(d)
        print(b)
        my_sql(b)


def my_sql(paraments):
    host1 = DB.host
    port1 = DB.port
    user1 = DB.user
    pwd1 = DB.password
    db_name = DB.db_name
    connection = pymysql.connect(host=host1,port=int(port1),user=user1,password=pwd1,database=db_name,charset='utf8')
    cur = connection.cursor()
    # if not paraments:
    #     paraments=[('1','1','1','1','1','1','1','1','2020-07-18 08:22:10.752')]
    for i in paraments:
        try:
            sql = 'insert into front_log(asctime,type,message,detail,detail_req,detail_res,current_url,user,browser_name)' \
                  ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            cur.executemany(sql,i)
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(e)


def cc():
    """ 获取cookie方法"""
    argument = {'type': 'account', 'username_no': '10034345659', 'passwd': 'Test123456', 'validCode': '', 'inviteCode': '',
                'userId': ''
        , 'teamId': '', 'source': '3001', 'session_duration': '31536000', 'auto_login': '1'}
    login = requests.post(url = 'https://testapp.fir.ai/api/account/user/signin/', data=argument)
    print(login.text)
    print(login.cookies)

def create_file():
    url = r'D:\上传文件\4排序\脚本创建'
    file_name = ''
    print('--')


if __name__ == '__main__':
    # start_thread()
    # openfile()
    # three()
    create_file()
    # cc()
    # my_sql()