# coding=utf-8

# 检查上传word+PDF是否生成对应job任务
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)
from test.file_operation import check_parsejobs
from common.private import UserProperty,InterBaseUrl
from common.comfunction import send_mail
import requests
import json


def login():
    name = UserProperty().user_check1
    url = InterBaseUrl().Base_url+'/account/user/signin/'
    print('url:'+url)
    data_s ={'type':'account','username_no':name,'passwd':UserProperty().pwd,'validCode':'','inviteCode':'','userId':'','teamId':''}
    res = requests.post(url=url,data=data_s)
    print(res.text)
    fir_session_id = res.headers.get('Set-Cookie').split(';')[0].split('fir_session_id=')[1]
    return fir_session_id


if __name__=='__main__':
    fir_session_id = login()
    # rootpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    word_file = os.path.join(rootPath,'自动化验证文档','回归的word文档.docx')
    pdf_file = os.path.join(rootPath,'自动化验证文档','验证图例文件.pdf')
    print(word_file)
    print(pdf_file)
    count_msg=''
    for i in [word_file,pdf_file]:
        msg = check_parsejobs(i,fir_session_id)
        count_msg = count_msg + msg
    if len(count_msg)>0: # 存在没有生成任务的，准备发送邮件
        subject = '上传文件job任务检查'
        content = '<html><head></head><body>'+count_msg+'</body></html>'
        send_mail(subject,content=content)

























