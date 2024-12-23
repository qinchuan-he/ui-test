# coding=utf-8


from datetime import datetime

import requests
import json
import os,sys
import time


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)

from common.private import EmailProperty,UserProperty
from common.comfunction import send_mail




# 检查47服务器状态和林斯特龙统计界面是否可用访问，能登录成功+请求到区域管理数据就是服务器+服务没问题
def check_url():
    # 检查时间点
    date_s = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    # 如果请求过程发生异常，比如超时等，算异常需要发送邮件
    try:
        # 先期登录
        url_s = UserProperty().url + "/api/TokenAuth/Authenticate"
        json_s = {"userNameOrEmailAddress": UserProperty().user2, "password": UserProperty().pwd, "clientType": "PC"}
        # 直接传递tenant租户id，不用调用租户接口
        headers_s = {"Content-Type": "application/json", "tenant": UserProperty().tenant_id_lin}
        print(url_s)
        print(json_s)
        # 登录获取token
        res = requests.post(url=url_s,json=json_s,headers=headers_s,timeout=(30,30))
        # print(type(res.text))
        # print(res.text)
        # 设置token
        result_s = json.loads(res.text)
        token = result_s['result']['accessToken']
        # print(token)
        token_s = "Bearer "+token
        # print(token_s)
        # 请求区域管理数据
        url_Clean = UserProperty().url + "/api/services/app/CleanAreaDailyManager/GetCleanAreaCharts"
        headers_clean = {"Content-Type": "application/json","tenant":UserProperty().tenant_id_lin,"authorization":token_s }
        res_claen = requests.get(url=url_Clean,headers=headers_clean,timeout=(30,30))
        # print(res_claen.text)
        status_s = json.loads(res_claen.text)['success']
        print(status_s)
        # print(type(status_s))
        if status_s:
            print("成功请求到区域管理数据")
        else:
            print("未请求到数据，发送邮件")
            email_title = "数据检查"
            email_content = '<html> <head><title>check report</title></head> <body> <h3>林斯特龙服务端检查{}</h3> <div>访问林斯特龙服务出现问题</div></body> </html>'.format(date_s)
            send_mail(subject=email_title, content=email_content, receive=EmailProperty().RECEVI_EMAIL2)

    except Exception as e:
        print("发生异常，发送邮件")
        print(e)
        email_title = "数据检查"
        email_content = '<html> <head><title>check report</title></head> <body> <h3>林斯特龙服务端检查：{}</h3> <div>访问林斯特龙服务出现问题</div><div>url：https://x.51xi.com</div></body> </html>'.format(
            date_s)
        send_mail(subject=email_title, content=email_content, receive=EmailProperty().RECEVI_EMAIL2)



if __name__=="__main__":
    check_url()



