# coding=utf-8


import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)

import requests
from bs4 import BeautifulSoup
from common.private import EmailProperty,UserProperty
from common.comfunction import send_mail



# 检查任务执行情况
def check_server_fail():
    session = requests.Session()
    url_1 = UserProperty().url_1
    url_2 = UserProperty().url_2
    url_3 = UserProperty().url_3
    url_4 = UserProperty().url_4

    try:
        res_1 = session.get(url_1,timeout=(30,30))
        # print("Cookies after first request:", session.cookies)
        token_2 = session.cookies.get('XSRF-TOKEN')
        data_s = {"returnUrl":"","TenancyName":"","UsernameOrEmailAddress":UserProperty().user,"Password":UserProperty().pwd2,"__RequestVerificationToken":token_2}

        res_2 = session.post(url=url_2,data=data_s,timeout=(30,30))
        # print("Cookies after first request:", session.cookies)

        res_3 = session.get(url=url_3,timeout=(30,30))
        # print(res_3.text)

        # 解析返回结果
        html_s = BeautifulSoup(res_3.text,'lxml')


        # 由于span标签存在重复这里查找a标签,只有一个不用find_all
        element_s = html_s.find('a', href="/hangfire/jobs/failed")
        # print(element_s)
        if element_s:
            element_span = element_s.find('span').find('span',class_ = 'metric metric-danger highlighted')
            fail_count = element_span.text.strip() # 获取文本并去除空格
            # print(element_span)
            # print(fail_count)
            # print(type(fail_count))
            if int(fail_count)>0:
                print('----错误数量超标请求详情页----')
                res_4 = session.get(url=url_4,timeout=(30,30))
                html_failed = res_4.content
                # print(html_failed)
                # 发送邮件
                print("开始发送邮件")
                email_title = "任务检查"
                email_content = html_failed
                send_mail(subject=email_title, content=email_content, receive=EmailProperty().RECEVI_EMAIL)
                print("发送邮件成功")
            else:
                print("本次检查无异常")

        # 继续找下去
    except Exception as e:
        print("本次检查报错了")
        print(e)
        print("开始发送邮件")
        email_title = "任务检查"
        email_content = ('<html> <head><title>check report</title></head> <body> <h3>检查url：'+url_1+'</h3> '
                         '<div>错误信息：{}</div></body> </html>').format(e)
        send_mail(subject=email_title, content=email_content, receive=EmailProperty().RECEVI_EMAIL)
        print("发送邮件成功")








if __name__=="__main__":
    check_server_fail()



