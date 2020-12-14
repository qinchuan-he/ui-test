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


# 连接mysql,cyprex数据库和datastorage数据库,传入iscyprex说明是cyprex数据库,type是数据类型，不传返回第一个行的第一个值
def connection_mysql(sqls,datetype=None,iscyprex=None):
    m_host = DB.host
    m_port = int(DB.port)
    if iscyprex:
        m_data = DB.db_cyprex
    else:
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
            if datetype=='list':
                count.append(s)
            else:
                count.append(s[0][0])
        else:
            for i in sqls:
                # sql = "select count(1) from jobs_extractjob where `status`='new' or `status`='running'"
                # print(i)
                cur.execute(i)
                s=cur.fetchall()
                connect.commit()
                if datetype == 'list':
                    count.append(s)
                else:
                    count.append(s[0][0])
    except Exception as e:
        connect.rollback()
        count.append(0)
        fail.append(e)
    return count,fail




#创建索引
def check_to_content():
    time_s = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    sql_1 = "select count(1) from jobs_extractjob where extract_code='to_content' and `status`='new' and created > '{}';".format(time_s)
    sql_2 = "select count(1) from jobs_extractjob where extract_code='to_content' and `status`='running'and created > '{}';".format(time_s)
    sql_3 = "select count(1) from jobs_extractjob where extract_code='to_content' and `status`='failed'and created > '{}';".format(time_s)
    sql_4 = "select count(1) from jobs_extractjob where extract_code='to_content' and created > '{}';".format(time_s)
    sql_5 = "select count(1) from jobs_extractjob where extract_code='to_content' and `status`='succeed' and created > '{}';".format(time_s)
    sql_s = []
    sql_s.append(sql_1)
    sql_s.append(sql_2)
    sql_s.append(sql_3)
    sql_s.append(sql_4)
    sql_s.append(sql_5)
    return sql_s

# 文件解析
def check_to_html():
    time_s = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    sql_1 = "select count(1) from jobs_extractjob where extract_code='to_html' and `status`='new' and created > '{}';".format(time_s)
    sql_2 = "select count(1) from jobs_extractjob where extract_code='to_html' and `status`='running' and created > '{}';".format(time_s)
    sql_3 = "select count(1) from jobs_extractjob where extract_code='to_html' and `status`='failed' and created > '{}';".format(time_s)
    sql_4 = "select count(1) from jobs_extractjob where extract_code='to_html'  and created > '{}';".format(time_s)
    sql_5 = "select count(1) from jobs_extractjob where extract_code='to_html' and `status`='succeed' and created > '{}';".format(time_s)
    sql_s = []
    sql_s.append(sql_1)
    sql_s.append(sql_2)
    sql_s.append(sql_3)
    sql_s.append(sql_4)
    sql_s.append(sql_5)
    return sql_s

# 提取纯文本,2020-09-16排除word,2020-11-3修改，new和running的只统计当天的
def check_text_format():
    time_s = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    sql_1 = "select count(1) from jobs_extractjob where extract_code='txt_format' and file_type <>'400' and `status`='new' and created > '{}';".format(time_s)
    sql_2 = "select count(1) from jobs_extractjob where extract_code='txt_format' and file_type <>'400' and `status`='running' and created > '{}';".format(time_s)
    sql_3 = "select count(1) from jobs_extractjob where extract_code='txt_format' and file_type <>'400' and `status`='failed' and created > '{}';".format(time_s)
    sql_4 = "select count(1) from jobs_extractjob where extract_code='txt_format' and file_type <>'400' and created > '{}';".format(time_s)
    sql_5 = "select count(1) from jobs_extractjob where extract_code='txt_format' and `status`='succeed' and created > '{}';".format(time_s)
    sql_s = []
    sql_s.append(sql_1)
    sql_s.append(sql_2)
    sql_s.append(sql_3)
    sql_s.append(sql_4)
    sql_s.append(sql_5)
    return sql_s

# 提取图例 extract_images 2020-12-08
def check_extract_images():
    time_s = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    sql_1 = "select count(1) from jobs_extractjob where extract_code='extract_images' and file_type <>'400' and `status`='new' and created > '{}';".format(time_s)
    sql_2 = "select count(1) from jobs_extractjob where extract_code='extract_images' and file_type <>'400' and `status`='running' and created > '{}';".format(time_s)
    sql_3 = "select count(1) from jobs_extractjob where extract_code='extract_images' and file_type <>'400' and `status`='failed' and created > '{}';".format(time_s)
    sql_4 = "select count(1) from jobs_extractjob where extract_code='extract_images' and file_type <>'400' and created > '{}';".format(time_s)
    sql_5 = "select count(1) from jobs_extractjob where extract_code='extract_images' and file_type <>'400' and `status`='succeed' and created > '{}';".format(time_s)
    sql_6 = "select count(1) from jobs_extractjob where extract_code='txt_format' and file_type ='300' and `status`in('succeed','failed') and created > '{}';".format(time_s)
    sql_s = []
    sql_s.append(sql_1)
    sql_s.append(sql_2)
    sql_s.append(sql_3)
    sql_s.append(sql_4)
    sql_s.append(sql_5)
    sql_s.append(sql_6)
    # print(sql_s)
    return sql_s

# 提取表格 file_tables 2020-12-08
def check_file_table():
    time_s = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    sql_1 = "select count(1) from jobs_extractjob where extract_code='file_tables' and file_type <>'400' and `status`='new' and created > '{}';".format(time_s)
    sql_2 = "select count(1) from jobs_extractjob where extract_code='file_tables' and file_type <>'400' and `status`='running' and created > '{}';".format(time_s)
    sql_3 = "select count(1) from jobs_extractjob where extract_code='file_tables' and file_type <>'400' and `status`='failed' and created > '{}';".format(time_s)
    sql_4 = "select count(1) from jobs_extractjob where extract_code='file_tables' and file_type <>'400' and created > '{}';".format(time_s)
    sql_5 = "select count(1) from jobs_extractjob where extract_code='file_tables' and file_type <>'400' and `status`='succeed' and created > '{}';".format(time_s)
    sql_6 = "select count(1) from jobs_extractjob where extract_code='txt_format' and file_type ='300' and `status`='succeed' and created > '{}';".format(time_s)
    sql_s = []
    sql_s.append(sql_1)
    sql_s.append(sql_2)
    sql_s.append(sql_3)
    sql_s.append(sql_4)
    sql_s.append(sql_5)
    sql_s.append(sql_6)
    # print(sql_s)
    return sql_s

# 检查并发送邮件
def send():
    contes_sqls = check_to_content()
    html_sqls = check_to_html()
    format_sqls = check_text_format()
    image_sqls = check_extract_images()
    table_sqls = check_file_table()
    contes_result,content_fail = connection_mysql(contes_sqls)
    html_result,html_fail = connection_mysql(html_sqls)
    format_result,format_fail= connection_mysql(format_sqls)
    image_result,image_fail = connection_mysql(image_sqls)
    table_result,table_fail = connection_mysql(table_sqls)


    sum = contes_result[0]+contes_result[1]+html_result[0]+html_result[1]+format_result[0]+format_result[1]\
          +image_result[0]+image_result[1]+table_result[0]+table_result[1]
    fail_sum = contes_result[2]+html_result[2]+format_result[2]+image_result[2]+table_result[2]
    # fail_percentage=(contes_result[2]+html_result[2]+format_result[2])/(contes_result[3]+html_result[3]+format_result[3])
    fail_percentage_1 = contes_result[2]/contes_result[3]
    fail_percentage_2 = html_result[2]/html_result[3]
    fail_percentage_3 = format_result[2]/format_result[3]
    fail_percentage_4 = image_result[2]/image_result[3]
    fail_percentage_5 = table_result[2]/table_result[3]
    fail_percentage_max=max(fail_percentage_1,fail_percentage_2,fail_percentage_3,fail_percentage_4,fail_percentage_5)
    # print(fail_percentage_1,fail_percentage_2,fail_percentage_3,fail_percentage_max)
    if sum>50:
        subject = '任务检查,任务堆积超过50条'
        content = "<html><header></header><body><table border='1'><tr><td>分类</td><td>创建索引(to_content)</td><td>解析服务(to_html)</td>" \
                  "<td>提取纯文本(txt_format)</td><td>图例(extract_images)</td><td>表格(file_tables)</td></tr><tr><td>等待" \
                  "</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr><tr><td>执行中</td>" \
                  "<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr><tr><td>失败</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "<td>当天任务总数</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "</table></body></html>".format(contes_result[0], html_result[0], format_result[0], image_result[0], table_result[0], contes_result[1]
                                                  , html_result[1], format_result[1], image_result[1], table_result[1], contes_result[2], html_result[2]
                                                  , format_result[2], image_result[2], table_result[2], contes_result[3],html_result[3],format_result[3]
                                                  , image_result[3], table_result[3])
        send_mail(subject, content=content)
    elif fail_percentage_max>0.05 or fail_sum>50:
        subject = '任务检查,失败任务超出指标'
        content = "<html><header></header><body><table border='1'><tr><td>分类</td><td>创建索引(to_content)</td><td>解析服务(to_html)</td>" \
                  "<td>提取纯文本(txt_format)</td><td>图例(extract_images)</td><td>表格(file_tables)</td></tr><tr><td>等待" \
                  "</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr><tr><td>执行中</td>" \
                  "<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr><tr><td>失败</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "<td>当天任务总数</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "</table></body></html>".format(contes_result[0], html_result[0], format_result[0], image_result[0], table_result[0], contes_result[1]
                                                  , html_result[1], format_result[1], image_result[1], table_result[1], contes_result[2], html_result[2]
                                                  , format_result[2], image_result[2], table_result[2], contes_result[3],html_result[3],format_result[3]
                                                  , image_result[3], table_result[3])
        send_mail(subject, content=content)
    elif image_result[3]<image_result[5] or table_result[3]<table_result[5]:
        subject = '任务检查,图例表格任务异常'
        content = "<html><header></header><body><table border='1'><tr><td>分类</td><td>创建索引(to_content)</td><td>解析服务(to_html)</td>" \
                  "<td>提取纯文本(txt_format)</td><td>图例(extract_images)</td><td>表格(file_tables)</td></tr><tr><td>等待" \
                  "</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr><tr><td>执行中</td>" \
                  "<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr><tr><td>失败</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "<td>当天任务总数</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "</table></body></html>".format(contes_result[0], html_result[0], format_result[0], image_result[0],
                                                  table_result[0], contes_result[1]
                                                  , html_result[1], format_result[1], image_result[1], table_result[1],
                                                  contes_result[2], html_result[2]
                                                  , format_result[2], image_result[2], table_result[2],
                                                  contes_result[3], html_result[3], format_result[3]
                                                  , image_result[3], table_result[3])
        send_mail(subject, content=content)
    # 2020-11-03 增加每隔两小时发送一份邮件，统计当天的任务情况
    time_array= [8,10,12,14,16,18,20,22]
    nowtime = time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time()))
    nowtime_h = int(nowtime.split(' ')[1].split(':')[0])
    nowtime_m = int(nowtime.split(' ')[1].split(':')[1])
    if nowtime_m < 30 and nowtime_h in time_array:
        print('准备发送邮件')
        subject = nowtime+'当天job任务情况'
        content = "<html><header></header><body><table border='1'><tr><td>分类</td><td>创建索引(to_content)</td><td>解析服务(to_html)</td>" \
                  "<td>提取纯文本(txt_format)</td></tr><tr><td>等待</td><td>{}</td><td>{}</td><td>{}</td></tr><tr><td>执行中</td>" \
                  "<td>{}</td><td>{}</td><td>{}</td></tr><tr><td>失败</td><td>{}</td><td>{}</td><td>{}</td></tr><tr>" \
                  "<td>成功</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "<td>当天任务总数</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "</table></body></html>".format(contes_result[0], html_result[0], format_result[0], contes_result[1]
                                                  , html_result[1], format_result[1], contes_result[2], html_result[2]
                                                  , format_result[2],  contes_result[4], html_result[4],
                                                  format_result[4] ,contes_result[3], html_result[3],
                                                  format_result[3])
        send_mail(subject, content=content,receive=EmailProperty().OTHER_EMAIL)

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

# 检查上一天的注册用户信息
def check_User():
    # sql_1 = 'select `name`, mobile, menu_code, edu_active_time, source_type, company, ctime, ltime, exp_time' \
    #       ', `status`,is_join_improve from account_user where date(ctime) = date_sub(curdate(),interval 2 day); '
    sql_1 = "select u.`name`, u.mobile, u.menu_code, u.edu_active_time, u.source_type, u.company, u.ctime, u.ltime" \
            ", u.exp_time, u.`status`,u.is_join_improve ,count(lg.userId),attr.`value` from account_user u " \
            "LEFT JOIN account_loginlog lg on  u.id=lg.userId LEFT JOIN account_userattrs attr on u.id=attr.user_id " \
            "where  date(u.ctime) = date_sub(curdate(),interval 1 day) and attr.`key`='usedCapcity' GROUP BY u.id"
    sql_s = []
    sql_s.append(sql_1)
    # print(sql_s)
    return sql_s


def cctime():
    now_h = time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time()))
    now_m = time.strftime('%M', time.localtime(time.time()))
    print(now_h)
    print(now_h.split(' ')[1].split(':')[0])
    print(now_h.split(' ')[1].split(':')[1])
    print(now_m)
    if int(now_m)>30:
        print('------')



if __name__=="__main__":
    # connection_mysql()
    send()
    # check_notice()
    # cctime()






