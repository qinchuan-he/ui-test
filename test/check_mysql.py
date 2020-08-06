# coding=utf-8

"""
检查数据库剩余任务数量
2020-08-06,连接mysql数据库查询任务情况
"""

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)
import pymysql
from common.private import *
from common.comfunction import send_mail
from time import sleep


# 连接mysql
def connection_mysql(sqls):
    m_host = DB.host_pd
    m_port = int(DB.port_pd)
    m_data = DB.db_pd_storage
    m_user = DB.user_pd
    m_pwd = DB.pwd_pd
    m_charset='utf8'
    connect = pymysql.connect(host=m_host,port=m_port,database=m_data,user=m_user,password=m_pwd,charset=m_charset)

    cur = connect.cursor()
    count = []
    fail = []
    try:
        for i in sqls:
            # sql = "select count(1) from jobs_extractjob where `status`='new' or `status`='running'"
            cur.execute(i)
            s=cur.fetchall()
            connect.commit()
            count.append(s[0][0])
    except Exception as e:
        connect.rollback()
        count.append(0)
        fail.append(e)
    return count,fail




#创建索引
def check_to_content():
    sql_1 = "select count(1) from jobs_extractjob where extract_code='to_content' and `status`='new';"
    sql_2 = "select count(1) from jobs_extractjob where extract_code='to_content' and `status`='running';"
    sql_3 = "select count(1) from jobs_extractjob where extract_code='to_content' and `status`='failed';"
    sql_s = []
    sql_s.append(sql_1)
    sql_s.append(sql_2)
    sql_s.append(sql_3)
    return sql_s

# 文件解析
def check_to_html():
    sql_1 = "select count(1) from jobs_extractjob where extract_code='to_html' and `status`='new';"
    sql_2 = "select count(1) from jobs_extractjob where extract_code='to_html' and `status`='running';"
    sql_3 = "select count(1) from jobs_extractjob where extract_code='to_html' and `status`='failed';"
    sql_s = []
    sql_s.append(sql_1)
    sql_s.append(sql_2)
    sql_s.append(sql_3)
    return sql_s

# 提取纯文本
def check_text_format():
    sql_1 = "select count(1) from jobs_extractjob where extract_code='txt_format' and `status`='new';"
    sql_2 = "select count(1) from jobs_extractjob where extract_code='txt_format' and `status`='running';"
    sql_3 = "select count(1) from jobs_extractjob where extract_code='txt_format' and `status`='failed';"
    sql_s = []
    sql_s.append(sql_1)
    sql_s.append(sql_2)
    sql_s.append(sql_3)
    return sql_s

# 检查并发送邮件
def send():
    contes_sqls = check_to_content()
    html_sqls = check_to_html()
    format_sqls = check_text_format()
    contes_result,content_fail = connection_mysql(contes_sqls)
    html_result,html_fail = connection_mysql(html_sqls)
    format_result,format_fail= connection_mysql(format_sqls)
    sum = contes_result[0]+contes_result[1]+html_result[0]+html_result[1]+format_result[0]+format_result[1]
    if int(sum)>50:
        subject = '任务检查,任务堆积超过50条'
        content = "<html><header></header><body><table border='1'><tr><td>分类</td><td>创建索引</td><td>解析服务</td>" \
                  "<td>提取纯文本</td></tr><tr><td>等待</td><td>{}</td><td>{}</td><td>{}</td></tr><tr><td>执行中</td>" \
                  "<td>{}</td><td>{}</td><td>{}</td></tr><tr><td>失败</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "</table></body></html>".format(contes_result[0],html_result[0],format_result[0],contes_result[1]
                                                  ,html_result[1],format_result[1],contes_result[2],html_result[2]
                                                  ,format_result[2])
        send_mail(subject, content=content)
    if content_fail or html_fail or format_fail:
        subject = 'sql查询有报错'
        content = "<html><header></header><body><table><tr><td>分类</td><td>创建索引</td><td>解析服务</td>" \
                  "<td>提取纯文本</td></tr><tr><td>报错信息</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "</table></body></html>".format(content_fail,html_fail,format_fail)
        send_mail(subject, content=content)


if __name__=="__main__":
    # connection_mysql()
    send()







