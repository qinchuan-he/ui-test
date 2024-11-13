
from test.check_day import EveryDayMethod
import time
from datetime import *
from common.private import DB
import pymysql


# 用于统计单日注册用户，进5日登录情况  2023-10-20 根据实际情况调整开始时间base_str和循环次数range(25)，还有统计id where id > '18733096' and id < '19720923'
def count_user():

    base_str='2023-10-07'
    base_date = datetime.strptime(base_str, "%Y-%m-%d")

    count_all = []  # 堆放所有数据的集合


    for i in range(25):

        star_date = base_date + timedelta(days=i)
        star2_date = base_date + timedelta(days=(i+1))
        star3_date = base_date + timedelta(days=(i + 2))
        star4_date = base_date + timedelta(days=(i + 3))
        star5_date = base_date + timedelta(days=(i + 4))
        star6_date = base_date + timedelta(days=(i + 5))
        # print(star5_date+timedelta(days=1))

        count_single = [] # 记录每天的数据

        print("开始统计：{}".format(star_date))
        # 统计注册人数，并且获取到user_id
        sql_1 = ("SELECT id FROM `account_user` WHERE  id > '140000' and `status`='1' "
                 "and ctime BETWEEN '{}' and '{}';").format(star_date,star2_date)
        sql_list = []
        sql_list.append(sql_1)
        list_user = conn_mysql(sql_list)
        # 获取对应天数的使用用户数
        user_day1 = ""
        user_day2 = ""
        user_day3 = ""
        user_day4 = ""
        # 获取第一天用户，并且加工成一个长字符串
        count_single.append(len(list_user))
        print("注册人数： {}".format(len(list_user)))
        for i in list_user:
            # print(i[0])  # 用户id
            user_day1 = user_day1+str(i[0])+"','" # 拼接出的结果末尾会多出一个','，最后sql中为''不影响
        # 如果只统计第一天注册人数，从这里开始可以隐藏
        # ==========================================================================================================================
        # -----------------------------------------------------------------------------------------------------------
        # 查询连续二天使用用户
        sql_2 = ("SELECT user_id FROM `main_logentry` where id > '18733096' and id < '19720923' and user_id in ('{}') "
                 "and ctime BETWEEN  '{}' and  '{}' GROUP BY user_id").format(user_day1,star2_date,star3_date)
        sql_list = []
        sql_list.append(sql_2)
        list_user2 = conn_mysql(sql_list)
        count_single.append(len(list_user2))
        print("连续2日使用人数： {}".format(len(list_user2)))
        for i in list_user2:
            # print(i[0])  # 用户id
            user_day2 = user_day2+str(i[0])+"','" # 拼接出的结果末尾会多出一个','，最后sql中为''不影响
        # -----------------------------------------------------------------------------------------------------------
        # 查询连续三天使用用户
        sql_3 = ("SELECT user_id FROM `main_logentry` where id > '18733096' and id < '19720923' and user_id in ('{}') "
                 "and ctime BETWEEN  '{}' and  '{}' GROUP BY user_id").format(user_day2,star3_date,star4_date)
        sql_list = []
        sql_list.append(sql_3)
        list_user3 = conn_mysql(sql_list)
        count_single.append(len(list_user3))
        print("连续3日使用人数： {}".format(len(list_user3)))
        for i in list_user3:
            # print(i[0])  # 用户id
            user_day3 = user_day3+str(i[0])+"','" # 拼接出的结果末尾会多出一个','，最后sql中为''不影响
        # -----------------------------------------------------------------------------------------------------------
        # 查询连续四天使用用户
        sql_4 = ("SELECT user_id FROM `main_logentry` where id > '18733096' and id < '19720923' and user_id in ('{}') "
                 "and ctime BETWEEN  '{}' and  '{}' GROUP BY user_id").format(user_day3,star4_date,star5_date)
        sql_list = []
        sql_list.append(sql_4)
        list_user4 = conn_mysql(sql_list)
        count_single.append(len(list_user4))
        print("连续4日使用人数： {}".format(len(list_user4)))
        for i in list_user4:
            # print(i[0])  # 用户id
            user_day4 = user_day4+str(i[0])+"','" # 拼接出的结果末尾会多出一个','，最后sql中为''不影响
        # -----------------------------------------------------------------------------------------------------------
        # 查询连续五天使用用户
        sql_5 = ("SELECT user_id FROM `main_logentry` where id > '18733096' and id < '19720923' and user_id in ('{}') "
                 "and ctime BETWEEN  '{}' and  '{}' GROUP BY user_id").format(user_day4,star5_date,star6_date)
        sql_list = []
        sql_list.append(sql_5)
        list_user5 = conn_mysql(sql_list)
        count_single.append(len(list_user5))
        print("连续4日使用人数： {}".format(len(list_user5)))
        # ==========================================================================================================================
        count_all.append(count_single) # 汇总数据


    print(count_all)


        # 统计注册第二日持续登录

        # 统计第三日持续登录

        # 统计第四日持续登录

        # 统计第五日持续登录

def conn_mysql(sql_list):
    host_name = DB.host
    db_name = DB.db_cyprex
    db_port = int(DB.port)
    db_user = DB.user
    db_pwd = DB.pwd
    conn = pymysql.connect(host=host_name, database=db_name, port=db_port, user=db_user, password=db_pwd)
    cur = conn.cursor()
    result = []
    try:
        for i in sql_list:
            cur.execute(i)
            # result.append(int(cur.fetchall()[0][0]))
            # result.append(cur.fetchall())
            result=list(cur.fetchall())
    except Exception as e:
        print(e)
    cur.close()
    conn.close()
    return result






if __name__=="__main__":
    count_user()

