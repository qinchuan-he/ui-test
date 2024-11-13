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
import requests


# 2022-06-27 更新，异步job任务只保留创建索引任务的检查，新增第三方数据入库的检查，2023-07-10更新，异步任务只检查PDF，caj的索引创建

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
    m_charset = 'utf8'
    connect = pymysql.connect(host=m_host,port=m_port,database=m_data,user=m_user,password=m_pwd,charset=m_charset)

    cur = connect.cursor()
    count = []
    fail = []

    # 2023-07-10 增加逻辑，如果传入sql为空，返回结果0,空
    # print(sqls)
    # print(len(sqls))
    if len(sqls) == 0:
        for i in range(8):
            count.append(0)
            # fail.append(0)
        return count, fail


    try:
        if type(sqls) == str:
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




#创建索引，2023-07-10 只统计PDF和caj的
def check_to_content():
    time_s = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    sql_1 = "select count(1) from jobs_extractjob where extract_code='to_content' and `status`='new' and created > '{}' and file_type in ('300','301');".format(time_s)
    sql_2 = "select count(1) from jobs_extractjob where extract_code='to_content' and `status`='running'and created > '{}' and file_type in ('300','301');".format(time_s)
    sql_3 = "select count(1) from jobs_extractjob where extract_code='to_content' and `status`='failed'and created > '{}' and file_type in ('300','301');".format(time_s)
    sql_4 = "select count(1) from jobs_extractjob where extract_code='to_content' and created > '{}' and file_type in ('300','301');".format(time_s)
    sql_5 = "select count(1) from jobs_extractjob where extract_code='to_content' and `status`='succeed' and created > '{}' and file_type in ('300','301');".format(time_s)
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

# 提取纯文本,2020-09-16排除word,2020-11-3修改，new和running的只统计当天的,目前已经废弃2021-03-17
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
    sql_6 = "select count(1) from jobs_extractjob where extract_code='txt_format' and file_type in ('300','301') and `status`in('succeed','failed') and created > '{}';".format(time_s)
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
    sql_6 = "select count(1) from jobs_extractjob where extract_code='txt_format' and file_type in ('300','301') and `status`='succeed' and created > '{}';".format(time_s)
    sql_s = []
    sql_s.append(sql_1)
    sql_s.append(sql_2)
    sql_s.append(sql_3)
    sql_s.append(sql_4)
    sql_s.append(sql_5)
    sql_s.append(sql_6)
    # print(sql_s)
    return sql_s

# 提取文献信息 to_information 2021-03-17
def check_to_information():
    time_s = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    sql_1 = "select count(1) from jobs_extractjob where extract_code='to_information' and file_type <>'400' and `status`='new' and created > '{}';".format(time_s)
    sql_2 = "select count(1) from jobs_extractjob where extract_code='to_information' and file_type <>'400' and `status`='running' and created > '{}';".format(time_s)
    sql_3 = "select count(1) from jobs_extractjob where extract_code='to_information' and file_type <>'400' and `status`='failed' and created > '{}';".format(time_s)
    sql_4 = "select count(1) from jobs_extractjob where extract_code='to_information' and file_type <>'400' and created > '{}';".format(time_s)
    sql_5 = "select count(1) from jobs_extractjob where extract_code='to_information' and file_type <>'400' and `status`='succeed' and created > '{}';".format(time_s)
    sql_s = []
    sql_s.append(sql_1)
    sql_s.append(sql_2)
    sql_s.append(sql_3)
    sql_s.append(sql_4)
    sql_s.append(sql_5)
    # print(sql_s)
    return sql_s

# 检查邀请和删除堆积情况（异步任务）定义超2小时未处理任务为堆积。2022-02-10
def check_asynchronous_task():
    time_s = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    time_d = time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()-7200))
    # 查询大使邀请激励堆积
    sql_1 = "SELECT count(*) FROM `account_inviterecordprev` where ctime BETWEEN '{}' " \
            "and '{}' and `status`='1';".format(time_s, time_d)
    # 查询删除任务堆积
    sql_2 = "SELECT count(*) FROM `resources_resource` WHERE  utime BETWEEN '{}' "\
            "and '{}' and `status` ='0';".format(time_s, time_d)
    sql_s = []
    sql_s.append(sql_1)
    sql_s.append(sql_2)
    return sql_s

# 检查第三方服务doi查询服务，判断依据是第三方信息入库（resources_reference_extend表），判断近2小时的入库数据,终止，后端说单独提供一个接口查
def check_doi_search():
    time_s = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    time_d = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()-7200))
    sql_1 = ''
    pass
# 获取公司ip
def get_ip():
    url = "https://myip.ipip.net/"

    response = requests.request("GET", url)
    ip = response.text
    return ip

# 检查并发送邮件，2023-07-13，只保留pdf和caj的索引创建
def send():
    contes_sqls = check_to_content()
    html_sqls = check_to_html()
    html_sqls = []
    format_sqls = check_text_format()
    format_sqls = []
    image_sqls = check_extract_images()
    image_sqls = []
    table_sqls = check_file_table()
    table_sqls = []
    information_sqls=check_to_information()
    information_sqls = []
    asynchronous_task=check_asynchronous_task()
    contes_result,content_fail = connection_mysql(contes_sqls)
    html_result,html_fail = connection_mysql(html_sqls)
    format_result,format_fail= connection_mysql(format_sqls)
    image_result,image_fail = connection_mysql(image_sqls)
    table_result,table_fail = connection_mysql(table_sqls)
    information_result,information_fail = connection_mysql(information_sqls)
    asynchronous_result,asynchronous_fail = connection_mysql(asynchronous_task, iscyprex=1)

    sum = contes_result[0]+contes_result[1]+html_result[0]+html_result[1]+format_result[0]+format_result[1]\
          +image_result[0]+image_result[1]+table_result[0]+table_result[1]+information_result[0]+information_result[1]
    fail_sum = contes_result[2]+html_result[2]+format_result[2]+image_result[2]+table_result[2]+information_result[2]
    # fail_percentage=(contes_result[2]+html_result[2]+format_result[2])/(contes_result[3]+html_result[3]+format_result[3])
    # 这里可以写一个函数，因为这几个逻辑都一样的，有时间来优化


    if contes_result[3]==0:
        fail_percentage_1=0
    else:
        fail_percentage_1 = contes_result[2]/contes_result[3]
    if html_result[3]==0:
        fail_percentage_2=0
    else:
        fail_percentage_2 = html_result[2]/html_result[3]
    if format_result[3]==0:
        fail_percentage_3=0
    else:
        fail_percentage_3 = format_result[2]/format_result[3]
    if image_result[3]==0:
        fail_percentage_4=0
    else:
        fail_percentage_4 = image_result[2]/image_result[3]
    if table_result[3]==0:
        fail_percentage_5=0
    else:
        fail_percentage_5 = table_result[2]/table_result[3]
    if information_result[3]==0:
        fail_percentage_6=0
    else:
        fail_percentage_6 = information_result[2]/information_result[3]
    fail_percentage_max=max(fail_percentage_1,fail_percentage_2,fail_percentage_3,fail_percentage_4,fail_percentage_5,fail_percentage_6)
    # print(fail_percentage_1,fail_percentage_2,fail_percentage_3,fail_percentage_max)
    if sum > 50:
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
    elif fail_percentage_max > 0.05 or fail_sum > 50:
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
    elif image_result[3] < image_result[5] or table_result[3]<table_result[5]:
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
    time_array = [8,10,12,14,16,18,20,22]
    nowtime = time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time()))
    nowtime_h = int(nowtime.split(' ')[1].split(':')[0])
    nowtime_m = int(nowtime.split(' ')[1].split(':')[1])
    # # 2023-01-03 增加获取公司ip功能
    # ip = get_ip()
    if nowtime_m < 30 and nowtime_h in time_array:
        print('准备发送邮件')
        subject = nowtime+'当天job任务情况'
        content = "<html><header></header><body><table border='1'><tr><td>分类</td><td>创建索引(to_content)</td><td>解析服务(to_html)</td>" \
                  "<td>提取纯文本(txt_format)</td><td>提取文献信息(to_information)</td></tr><tr><td>等待</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr><tr><td>执行中</td>" \
                  "<td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr><tr><td>失败</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr><tr>" \
                  "<td>成功</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "<td>当天任务总数</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>" \
                  "</table></body></html>".format(contes_result[0], html_result[0], format_result[0], information_result[0], contes_result[1]
                                                  , html_result[1], format_result[1], information_result[1], contes_result[2], html_result[2]
                                                  , format_result[2], information_result[2], contes_result[4], html_result[4],
                                                  format_result[4] ,information_result[4], contes_result[3], html_result[3],
                                                  format_result[3],information_result[3])
        send_mail(subject, content=content,receive=EmailProperty().OTHER_EMAIL)
    # 2022-02-10 增加检查超过2小时未处理异步任务
    print(asynchronous_result)
    if asynchronous_result[0] > 10 or asynchronous_result[1] > 50:
        print("异步任务阻塞，准备发送邮件")
        subject = nowtime + '存在超过2小时未处理异步任务'
        content = "<html><header></header><body><table border='1'><tr><td>分类</td><td>超过2小时未被处理任务数</td>" \
                  "</tr><tr><td>大使邀请</td><td>{}</td></tr><tr><td>文件删除</td><td>{}</td></tr>" \
                  "</table></body></html>".format(asynchronous_result[0],asynchronous_result[1])
        send_mail(subject, content=content)

    if content_fail or html_fail or format_fail:
        print("------------------------")
        print(content_fail)
        print(html_fail)
        print(format_fail)
        print("--------------------------")
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




if __name__=="__main__":
    # connection_mysql()
    send()
    # check_notice()
    # cctime()






