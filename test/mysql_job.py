# coding=utf-8


import pymysql
from common.private import DB
import time
import datetime


# 创建索引,用户私有数据（往job表插数据）,传入user_id
def create_indexs(user_id):
    host = DB.host_test
    port = int(DB.port_test)
    db_name1 = DB.db_test_cyprex
    db_name2 = DB.db_test_storage
    user = DB.user_test
    pwd = DB.pwd_test
    char_set='utf8'
    connect = pymysql.connect(host=host,port=port,database=db_name1,user=user,password=pwd,charset=char_set)
    connect2 = pymysql.connect(host=host,port=port,database=db_name2,user=user,password=pwd,charset=char_set)
    cur = connect.cursor()
    cur2 = connect2.cursor()
    try:
        sql = "select rd.fileId,rc.contentType from resources_resource rc,resources_resource_users ru,resources_resourcedatads" \
              " rd where rc.id=ru.resource_id and rc.id=rd.resource_id and ru.user_id={} and rc.status=1;".format(user_id)
        cur.execute(sql)
        connect.commit()
        s = cur.fetchall()
        # print(s)
        sql3 = ''
        for file_id,content_type in s:
            # print(file_id,content_type)

            sql2 = "insert into jobs_extractjob(created,update_time,file_id,extract_code,extract_name,`status`,`code`,msg,file_type,opt_type" \
                   ",retry,job_serial,callback_status) values ('2020-08-21 10:19:44.463359','2020-08-21 10:19:44.463359'" \
                   ",'{}','to_content','to_content','new','','','{}','insert',0,'{}','new');".format(file_id,content_type,file_id)
            # print(sql2)
            cur2.execute(sql2)
        connect2.commit()
        print('--执行完毕--')
    except Exception as e:
        print(e)
        connect.rollback()
        connect2.rollback()
    connect.close()
    connect2.close()

# 创建索引,用户团队数据（往job表插数据）
def create_team_indexs():
    host = DB.host_test
    port = int(DB.port_test)
    db_name1 = DB.db_test_cyprex
    db_name2 = DB.db_test_storage
    user = DB.user_test
    pwd = DB.pwd_test
    char_set='utf8'
    connect = pymysql.connect(host=host,port=port,database=db_name1,user=user,password=pwd,charset=char_set)
    connect2 = pymysql.connect(host=host,port=port,database=db_name2,user=user,password=pwd,charset=char_set)
    cur = connect.cursor()
    cur2 = connect2.cursor()
    try:
        sql = "select rd.fileId,rc.contentType from resources_resource rc,resources_resourcedatads rd,resources_resource_groups rg" \
              ",group_userteammapping gu where rc.id=rd.resource_id and rg.resource_id=rc.id and rg.team_id=gu.team_id and user_id=32 and rc.status=1;"
        cur.execute(sql)
        connect.commit()
        s = cur.fetchall()
        # print(s)
        sql3 = ''
        for file_id,content_type in s:
            # print(file_id,content_type)
            sql2 = "insert into jobs_extractjob(created,update_time,file_id,extract_code,extract_name,`status`,`code`,msg,file_type,opt_type" \
                   ",retry,job_serial,callback_status) values ('2020-08-21 10:19:44.463359','2020-08-21 10:19:44.463359'" \
                   ",'{}','to_content','to_content','new','','','{}','insert',0,'{}','new');".format(file_id,content_type,file_id)
            # print(sql2)
            cur2.execute(sql2)
        connect2.commit()
        print('--执行完毕--')
    except Exception as e:
        print(e)
        connect.rollback()
        connect2.rollback()


# 根据用户id查询出，用户团队文件，根据文件file_id查询出任务执行时间.会连接两个数据库
def checkUseTime():
    host = DB.host_test
    port = int(DB.port_test)
    db_name1 = DB.db_test_cyprex
    db_name2 = DB.db_test_storage
    user = DB.user_test
    pwd = DB.pwd_test
    char_set = 'utf8'
    connect = pymysql.connect(host=host, port=port, database=db_name1, user=user, password=pwd, charset=char_set)
    connect2 = pymysql.connect(host=host, port=port, database=db_name2, user=user, password=pwd, charset=char_set)
    cur = connect.cursor()
    cur2 = connect2.cursor()
    try:
        # 查询出用户有共享数据的word和pdf
        sql_1 = "select rd.fileId,rc.contentType from resources_resource rc,resources_resourcedatads rd,resources_resource_groups rg" \
                ",group_userteammapping gu where rc.id=rd.resource_id and rg.resource_id=rc.id and rg.team_id=gu.team_id and user_id=681 " \
                "and rc.status=1 and rc.contentType in ('300','400')"
        # 插入到job表里面
        sql_2 = "insert into jobs_extractjob(created,update_time,file_id,extract_code,extract_name,`status`,`code`,msg,file_type,opt_type" \
                   ",retry,job_serial,callback_status) values (%s,%s" \
                   ",%s,'to_content','to_content','new','','',%s,'insert',0,%s,'new');"
        # 插入之前删除，对应的索引记录
        sql_3 = "delete from jobs_extractjob where file_id=%s and extract_code='to_content';"
        # args_delete=[('e0d0d9c9-92e0-4587-8883-841561cb57ea')]
        # args_insert = [(datetime.datetime.now(),datetime.datetime.now(),'e0d0d9c9-92e0-4587-8883-841561cb57ea','400','e0d0d9c9-92e0-4587-8883-841561cb57ea')]
        # 2和3执行之后，检查的


        cur.execute(sql_1)
        connect.commit()
        args_delete=[]
        args_insert=[]
        args_select = []
        for file_id,content_type in cur.fetchall():
            # print(file_id)
            tup=(file_id,)
            tup2 = (datetime.datetime.now(),datetime.datetime.now(),file_id,str(content_type),file_id)
            args_delete.append(tup)
            args_insert.append(tup2)
            args_select.append(file_id)

        sql_4 = "select count(1) from jobs_extractjob where extract_code='to_content' and `status`='new'  and file_id in {};".format(tuple(args_select)) # 查询任务执行情况
        sql_5 = "select created,update_time,file_id from jobs_extractjob where extract_code='to_content' and `status`='succeed'  and file_id in {};".format(
            tuple(args_select)) # 调整时区，查询出时间和id
        sql_6 = "update jobs_extractjob set update_time=%s where  file_id =%s and extract_code='to_content' " # 调整时区，更新时间
        sql_7 ="select min(created),max(update_time),count(1) from jobs_extractjob where extract_code='to_content' and `status`='succeed' and file_id in {};".format(tuple(args_select)) # 查询出成功数据中最早的开始时间和最晚的完成时间，就是一段时间的执行总量，可以区分word和PDF

        # cur2.executemany(sql_3, args_delete) # 删除老的索引任务
        # connect2.commit()
        # cur2.executemany(sql_2,args_insert) # 创建新的索引任务
        # connect2.commit()
        # print(args_delete)
        # print(args_insert)
        # cur2.execute(sql_4) # 查询执行结果
        # connect2.commit()
        # cur2.execute(sql_5) # 查询出创建时间和更新时间（由于服务器时区不对，导致差八小时，现在补上，只针对成功的）
        #
        # args_update = []
        # for i in cur2.fetchall():
        #     args_tmp = []
        #     args_tmp.append(i[1]+datetime.timedelta(hours=8))
        #     args_tmp.append(i[2])
        #     args_update.append(tuple(args_tmp))
        # cur2.executemany(sql_6,tuple(args_update)) # 给数据库的更新时间+8小时（调整时区）
        # connect2.commit()
        cur2.execute(sql_7) # 查询一段时间成功的总量
        result = cur2.fetchall()
        num = result[0][2]
        consuming = (result[0][1]-result[0][0]).seconds # 耗时，秒
        print(num)
        print(consuming)
        unitConsuming = int(consuming)/int(num)
        print(unitConsuming)


        print(result)

        print('--执行完--')

    except Exception as e:
        print(e)
        connect2.rollback()

# 统计登录用户数
def get_usercount():
    host = DB.host
    port = int(DB.port)
    db_name1 = DB.db_cyprex
    user = DB.user
    pwd = DB.pwd
    char_set = 'utf8'
    connect = pymysql.connect(host=host, port=port, database=db_name1, user=user, password=pwd, charset=char_set)
    cur =connect.cursor()


    day_now = datetime.date.today()
    for i in range(40):
        days = datetime.timedelta(days=-i)
        day = day_now+days
        sql_1 = "select count(*) from (SELECT user_id FROM `main_logentry` where ctime like '{}%' GROUP BY user_id) as u".format(day)
        cur.execute(sql_1)
        result = cur.fetchall()[0][0]
        print(day,',',result)

    connect.commit()
    # print(result)







if __name__=='__main__':
    # create_indexs()
    # create_team_indexs()
    # checkUseTime()
    get_usercount()














