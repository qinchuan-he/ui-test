# encoding=utf-8

import pymysql
from common.private import DB
import time






# 统计pv uv

# 连接数据库，执行sql,传入数组
def connect_mysql(sqls):
    m_host = DB.host
    m_port = int(DB.port)
    m_data = DB.db_cyprex
    m_user = DB.user
    m_pwd = DB.pwd
    m_charset = 'utf8'
    connect = pymysql.connect(host=m_host, port=m_port, database=m_data, user=m_user, password=m_pwd, charset=m_charset)
    cur = connect.cursor()
    result_l=[]
    # sql = "SELECT count(1) FROM `datastatistics_logs`  where ctime BETWEEN '2021-02-18' and '2021-02-19'"
    for sql in sqls:
        cur.execute(sql)
        result=cur.fetchall()
        # print(result)
        connect.commit()
        # print('--------------')
        # print(result)
        result_l.append(result)
    return result_l

# 存放时间范围
def date_list():

    time_l = []
    time_s = time.strftime('%Y-%m-%d', time.localtime(time.time() - 3600 * 24 * 35))
    for i in range(36):
        time_s = time.strftime('%Y-%m-%d', time.localtime(time.time() - 3600 * 24 * 35 + i * 3600 * 24))
        time_l.append(time_s)
    # print(time_l)
    return time_l

# sql语句,查询时间段的PV，返回数组
def PV():
    sql = "SELECT count(1) FROM `datastatistics_logs`  where ctime BETWEEN '2021-02-18' and '2021-02-19'"
    # print(time.time())
    s = date_list()
    sql_s = []
    for i in range(len(s)-1):
        # print(s[i],s[i+1])
        sql = "SELECT count(1) FROM `datastatistics_logs`  where ctime BETWEEN '{}' and '{}'".format(s[i],s[i+1])
        sql_s.append(sql)
    # print(sql_s)
    return sql_s

# UV时间段内UV的sql
def UV():
    s = date_list()
    sql_s = []
    for i in range(len(s) - 1):
        # print(s[i],s[i+1])
        sql = "select count(*) from (SELECT realip FROM `datastatistics_logs`  where ctime " \
              "BETWEEN '{}' and '{}' GROUP BY realip) ip".format(s[i], s[i + 1])
        sql_s.append(sql)
    # print(sql_s)
    return sql_s

# 一段时间内的每日新增用户
def add_user():
    s = date_list()
    sql_s = []
    for i in range(len(s)-1):
        sql = "select count(*) FROM account_user where `status`=1 and service_type='1' " \
              "and mobile not like '100%' and ctime BETWEEN '{}' and '{}'".format(s[i],s[i+1])
        sql_s.append(sql)
    return sql_s

# 一段时间内每天付款的用户
def add_vip():
    s = date_list()
    sql_s = []
    for i in  range(len(s)-1):
        sql = "select count(*) from account_user where `status`=1 and " \
              "service_type='1' and mobile not like '100%' and id in " \
              "(select DISTINCT user_id from pay_order where `STATUS`='1' " \
              "and payment_time BETWEEN '{}' and '{}')".format(s[i],s[i+1])
        sql_s.append(sql)
    return sql_s

# 一段时间内每天购买的标准会员
def add_standard_vip():
    s = date_list()
    sql_s = []
    for i in range(len(s)-1):
        sql = "select count(*) from account_user where `status`=1 and " \
              "service_type='1' and mobile not like '100%' and id in (select " \
              "DISTINCT user_id from pay_order where `STATUS`='1' " \
              "and payment_time BETWEEN '{}' and '{}' and total_amount='69')".format(s[i],s[i+1])
        sql_s.append(sql)
    return sql_s

# 一段时间内购买高级会员
def add_senior_vip():
    s = date_list()
    sql_s = []
    for i in range(len(s)-1):
        sql = "select count(*) from account_user where `status`=1 and service_type='1' and mobile not " \
              "like '100%' and id in (select DISTINCT user_id from pay_order " \
              "where `STATUS`='1' and payment_time BETWEEN '{}' and '{}' and total_amount in ('139','70','100'))".format(s[i],s[i+1])
        sql_s.append(sql)
    return sql_s

# 一段时间内购买专业会员
def add_profess_vip():
    s = date_list()
    sql_s = []
    for i in range(len(s)-1):
        sql = "select count(*) from account_user where `status`=1 and service_type='1' and mobile not like '100%' " \
              "and id in (select DISTINCT user_id from pay_order where `STATUS`='1' and payment_time " \
              "BETWEEN '{}' and '{}' and total_amount in ('198','129','59','159'))".format(s[i],s[i+1])
        sql_s.append(sql)
    return sql_s

def  exec_sql():
    pv_sqls=PV()
    uv_sqls=UV()
    add_user_sql = add_user()
    add_vip_sql = add_vip()
    add_standard_vip_sql = add_standard_vip()
    add_senior_vip_sql = add_senior_vip()
    add_profess_vip_sql = add_profess_vip()
    # pv_result = connect_mysql(pv_sqls)
    # uv_result = connect_mysql(uv_sqls)
    # add_user_result = connect_mysql(add_user_sql)
    # add_vip_result = connect_mysql(add_vip_sql)
    # add_standard_vip_result = connect_mysql(add_standard_vip_sql)
    # add_senior_vip_result = connect_mysql(add_senior_vip_sql)
    add_profess_vip_result = connect_mysql(add_profess_vip_sql)
    print(add_profess_vip_result)

if __name__=='__main__':
    # connect_mysql()
    exec_sql()
    # add_vip()




