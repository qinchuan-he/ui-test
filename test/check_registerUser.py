

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)
from test.check_mysql import connection_mysql,check_User
from common.comfunction import send_mail
from common.private import EmailProperty
import time

def check_newUser():

    sql = check_User() # 获取sql语句
    resule,fail = connection_mysql(sql,'list',1)
    content_head = '<html><head></head><body><table border="1">'
    content_foot = '</table></body></html>'
    if len(fail)>1:
        # print(fail)
        context = '<tr><td>'+fail+'</td></tr>'
    else:
        context = '<tr><td>序号</td><td>姓名</td><td>手机</td><td>套餐</td><td>EDU邮箱激活时间</td><td>注册来源类型</td>' \
                  '<td>创建时间</td><td>最后登录时间</td><td>账号状态</td><td>是否加入改进计划</td><td>登录次数</td><td>空间容量</td></tr>'
        convert = []
        for i in resule[0]:
            transit = []
            # print(i)
            if i[1][0:3:1]=='100':  # 排除100开头的手机号
                continue
            transit.append(i[0]) # 姓名
            transit.append(i[1]) # 手机号
            if i[2]=='1001':
                transit.append('个人免费版')
            else:
                # transit.append('企业用户')
                transit.append('新用户')
            if i[3]:
                transit.append(i[3])
            else:
                transit.append('-')
            if i[4]==1001:
                transit.append('见远团队页')
            elif i[4]==1002:
                transit.append('官网-登录入口')
            elif i[4] == 1003:
                transit.append('边写边搜页PC')
            elif i[4] == 1006:
                transit.append('边写边搜页MOB')
            elif i[4] == 2001:
                transit.append('Office')
            elif i[4] == 2001:
                transit.append('见远Saas')
            else:
                transit.append('其他未知渠道')
            transit.append(i[6].strftime("%Y-%m-%d %H:%M:%S")) # 创建日期
            if i[7] is not None:
                transit.append(i[7].strftime("%Y-%m-%d %H:%M:%S")) # 最后登录日期
            else:
                transit.append('-')  # 最后登录日期
            if i[-4]==1:
                transit.append('有效')
            else:
                transit.append('无效')
            if i[-3]==0:
                transit.append('否')
            else:
                transit.append('是')
            transit.append(i[-2]) # 登录次数
            transit.append('{}M/500M'.format(int(int(i[-1])/1024/1024)))


            convert.append(transit)
        # print(convert)
        # print(len(convert))
        print('统计完成数据：{}条，准备发送邮件'.format(len(convert)))
        num = 1
        for j in convert:
            context = context+'<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>' \
                              '</tr>'.format(num,j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8],j[-2],j[-1])
            num+=1
    subject = '昨日注册人数'
    content=content_head+context+content_foot
    send_mail(subject,content=content,receive=EmailProperty().RECEVI_EMAIL_MARKET)
    print('邮件发送完成')

if __name__=='__main__':
    check_newUser()







