# coding=utf-8

"""
检查数据库剩余任务数量
2020-08-06,连接mysql数据库查询任务情况
new和running的合集超过50条报警，当天失败超过50条或者失败占比>5%报警
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
import time


# 连接mysql
def connection_mysql(sqls):
    m_host = DB.host
    m_port = int(DB.port)
    m_data = DB.db_storage
    m_user = DB.user
    m_pwd = DB.pwd
    m_charset='utf8'
    connect = pymysql.connect(host=m_host,port=m_port,database=m_data,user=m_user,password=m_pwd,charset=m_charset)

    cur = connect.cursor()
    count = []
    fail = []
    try:
        if type(sqls)==str:
            cur.execute(sqls)
            s = cur.fetchall()
            connect.commit()
            count.append(s[0][0])
        else:
            for i in sqls:
                # sql = "select count(1) from jobs_extractjob where `status`='new' or `status`='running'"
                # print(i)
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
    time_s = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    sql_1 = "select count(1) from jobs_extractjob where extract_code='to_content' and `status`='new';"
    sql_2 = "select count(1) from jobs_extractjob where extract_code='to_content' and `status`='running';"
    sql_3 = "select count(1) from jobs_extractjob where extract_code='to_content' and `status`='failed'and created > '{}';".format(time_s)
    sql_4 = "select count(1) from jobs_extractjob where extract_code='to_content' and created > '{}';".format(time_s)
    sql_s = []
    sql_s.append(sql_1)
    sql_s.append(sql_2)
    sql_s.append(sql_3)
    sql_s.append(sql_4)
    return sql_s

# 文件解析
def check_to_html():
    time_s = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    sql_1 = "select count(1) from jobs_extractjob where extract_code='to_html' and `status`='new';"
    sql_2 = "select count(1) from jobs_extractjob where extract_code='to_html' and `status`='running';"
    sql_3 = "select count(1) from jobs_extractjob where extract_code='to_html' and `status`='failed' and created > '{}';".format(time_s)
    sql_4 = "select count(1) from jobs_extractjob where extract_code='to_html'  and created > '{}';".format(time_s)
    sql_s = []
    sql_s.append(sql_1)
    sql_s.append(sql_2)
    sql_s.append(sql_3)
    sql_s.append(sql_4)
    return sql_s

# 提取纯文本,2020-09-16排除word
def check_text_format():
    time_s = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    sql_1 = "select count(1) from jobs_extractjob where extract_code='txt_format' and file_type <>'400' and `status`='new';"
    sql_2 = "select count(1) from jobs_extractjob where extract_code='txt_format' and file_type <>'400' and `status`='running';"
    sql_3 = "select count(1) from jobs_extractjob where extract_code='txt_format' and file_type <>'400' and `status`='failed' and created > '{}';".format(time_s)
    sql_4 = "select count(1) from jobs_extractjob where extract_code='txt_format' and file_type <>'400' and created > '{}';".format(time_s)
    sql_s = []
    sql_s.append(sql_1)
    sql_s.append(sql_2)
    sql_s.append(sql_3)
    sql_s.append(sql_4)
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
    fail_sum = contes_result[2]+html_result[2]+format_result[2]
    # fail_percentage=(contes_result[2]+html_result[2]+format_result[2])/(contes_result[3]+html_result[3]+format_result[3])
    fail_percentage_1 = contes_result[2]/contes_result[3]
    fail_percentage_2 = html_result[2]/html_result[3]
    fail_percentage_3 = format_result[2]/format_result[3]
    fail_percentage_max=max(fail_percentage_1,fail_percentage_2,fail_percentage_3)
    # print(fail_percentage_1,fail_percentage_2,fail_percentage_3,fail_percentage_max)
    if sum>50:
        subject = '任务检查,任务堆积超过50条'
        content = "<html><header></header><body><table border='1'><tr><td>分类</td><td>创建索引(to_content)</td><td>解析服务(to_html)</td>" \
                  "<td>提取纯文本(txt_format)</td></tr><tr><td>等待</td><td>{}</td><td>{}</td><td>{}</td></tr><tr><td>执行中</td>" \
                  "<td>{}</td><td>{}</td><td>{}</td></tr><tr><td>失败</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "<td>当天任务总数</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "</table></body></html>".format(contes_result[0],html_result[0],format_result[0],contes_result[1]
                                                  ,html_result[1],format_result[1],contes_result[2],html_result[2]
                                                  ,format_result[2],contes_result[3],html_result[3],format_result[3])
        send_mail(subject, content=content)
    elif fail_percentage_max>0.05 or fail_sum>50:
        subject = '任务检查,失败任务超出指标'
        content = "<html><header></header><body><table border='1'><tr><td>分类</td><td>创建索引(to_content)</td><td>解析服务(to_html)</td>" \
                  "<td>提取纯文本(txt_format)</td></tr><tr><td>等待</td><td>{}</td><td>{}</td><td>{}</td></tr><tr><td>执行中</td>" \
                  "<td>{}</td><td>{}</td><td>{}</td></tr><tr><td>失败</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "<td>当天任务总数</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "</table></body></html>".format(contes_result[0], html_result[0], format_result[0], contes_result[1]
                                                  , html_result[1], format_result[1], contes_result[2], html_result[2]
                                                  , format_result[2],contes_result[3],html_result[3],format_result[3])
        send_mail(subject, content=content)
    if content_fail or html_fail or format_fail:
        subject = 'sql查询有报错'
        content = "<html><header></header><body><table><tr><td>分类</td><td>创建索引(to_content)</td><td>解析服务(to_html)</td>" \
                  "<td>提取纯文本(txt_format)</td></tr><tr><td>报错信息</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "</table></body></html>".format(content_fail,html_fail,format_fail)
        send_mail(subject, content=content)
    print('执行完成')


# 定时检查接入公告数据，jenkins中每天定时执行，目前每天下午5点
def check_notice():
    date = time.strftime('%y-%m-%d 00:00:00',time.localtime(time.time()))
    notice_sql = "select count(1) from store_publicdatainfo where created > '{}'".format(date)
    # print(notice_sql)
    collect_result, content_fail = connection_mysql(notice_sql)
    # print(collect_result)
    # print(collect_result[0])
    if collect_result[0]==0:
        subject = '公告未获取到'
        # content = "<html><header></header><body>今日公告获取数量为:{}</body></html>".format(collect_result[0])
        content = "<html><header></header><body>今日公告获取数量为:0</body></html>"
        send_mail(subject, content=content)
    print('公告获取检查，执行完成')


if __name__=="__main__":
    # connection_mysql()
    send()
    # check_notice()






