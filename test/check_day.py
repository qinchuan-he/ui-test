#coding=utf-8

import os,sys
# 解决Linux中找不到引用问题
import time

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)

from common.private import DB,ServerInfo,EmailProperty
from common.comfunction import send_mail
import datetime
import pymysql
import paramiko

# 每天执行检查相关功能(统计前一天数据)，输出结果有标记

class EveryDayMethod:
    """ 方法类"""
    # 初始化
    def __init__(self):

        # 2023-05-30 增加id条件，隔段时间需要更新
        self.resource_id = 4368707   # resources_resource 表id，2023-12-11更新
        self.extraattr_id = 3240564  # resources_extraattr 表id
        self.annotation_id = 6449003  # resources_annotation 表id
        self.logentry_id = 21300796  # main_logentry 表id
        self.chatgpt_id = 144917  # resources_chat_record 表id


        same_day = datetime.datetime.now()
        d = datetime.timedelta(days=-1)
        # d1 = datetime.timedelta(days=-1)
        self.start_day = (same_day+d).strftime("%Y-%m-%d")  # 开始检查日期
        self.end_day = same_day.strftime("%Y-%m-%d")   # 截止检查日期
        # self.end_day = (same_day+d1).strftime("%Y-%m-%d")
        print('-------------统计日期------------------',self.start_day)
# 设置统计变量
        self.document_count = 0  # 标题查询，以前的文献查询
        self.document_count_error = 0
        self.note_ocr = 0  # 局部ocr
        self.note_ocr_error = 0
        self.translate_count = 0  # 翻译
        self.translate_count_error = 0
        self.doi_count = 0  # doi查询
        self.doi_error_count = 0
        self.doi_success_count = 0
        self.ocr_count = 0  # 全文ocr
        self.ocr_error_count = 0
        self.pdf_count = 0  # PDF数量
        self.caj_count = 0  # caj数量
        self.webpage_count = 0  # 网页快照统计PDF+html
        self.doi_up_count = 0  # doi上传

        self.doi_pdf_count = 0  # doi查询--pdf
        self.doi_pdf_success_count = 0
        self.doi_caj_count = 0  # doi查询--caj
        self.doi_caj_success_count = 0
        self.doi_html_count = 0  # doi查询--html
        self.doi_html_success_count = 0

        self.annotation_count = 0  # 笔记数量
        self.excerpt_count = 0  # 摘录数量

        self.analysis_count = 0  #文献分析使用次数

        self.chatgpt_count_all = 0 # chatgpt调用次数,成功
        self.chatgpt_count_success = 0 # chatgpt调用次数,成功
        self.chatgpt_count_fail = 0  # chatgpt调用次数,失败


        self.plugin_office_use = 0  # 统计office插件使用用户数
        self.plugin_wps_use = 0  # 统计wps插件使用用户数
        self.plugin_citation_add = 0  # 统计引用次数


# 连接数据库，并执行sql，传入数组，sql一条条执行，返回数组
    def conn_mysql(self,sql_list):
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
                result.append(int(cur.fetchall()[0][0]))
        except Exception as e:
            print(e)
        cur.close()
        conn.close()
        return result

# 该linux方法主要用于统计数量，不做其他处理，2021-09-15增加连接第三台服务器
# 连接linux服务器,并执行传入的命令（删除命令需要严格定义）,传入数组，用;拼接成str一起转过去执行,返回结果是数组.目前两台服务器
    def conn_linux(self,shell_list):
        host_name = DB.host
        host_port = ServerInfo.port_1
        host_portb = ServerInfo.port_2
        host_portc = ServerInfo.port_3
        username = DB.user
        private_file = ServerInfo.private_file
        private_key = paramiko.RSAKey.from_private_key_file(private_file)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        result_a = []  # 第一台服务器
        result_b = []  # 第二台服务器
        result_c = []  # 第三台服务器
        result = []
        shell_content = ""
        # 拼装Linux命令
        for i in range(len(shell_list)):
            if i == 0:
                shell_content = shell_list[i]
            else:
                shell_content = shell_content+';'+shell_list[i]
        # 连接第一台服务器
        try:
            client.connect(hostname=host_name, port=host_port, username=username, pkey=private_key)
            # stdin,stdout,stderr = client.exec_command('{};{}'.format(shell_context[0],shell_context[1]))
            stdin, stdout, stderr = client.exec_command(shell_content)
            result_a = stdout.readlines()
        except Exception as e:
            print(e)

        # 连接另一台服务
        try:
            client.connect(hostname=host_name, port=host_portb, username=username, pkey=private_key)
            # stdin,stdout,stderr = client.exec_command('{};{}'.format(shell_context[0],shell_context[1]))
            stdin, stdout, stderr = client.exec_command(shell_content)
            result_b = stdout.readlines()
        except Exception as e:
            print(e)

        # 连接第三台服务器，2021-09-15
        try:
            client.connect(hostname=host_name,port=host_portc,username=username,pkey=private_key)
            stdin,stdout,stderr = client.exec_command(shell_content)
            result_c = stdout.readlines()
        except Exception as e:
            print(e)

        client.close()
        # 查询结果合并
        result_len_temp = len(result_a) if len(result_a) > len(result_b) else len(result_b)
        result_len = result_len_temp if result_len_temp > len(result_c) else len(result_c)
        for i in range(result_len):
            # 排除发生异常情况下导致查询结果不一致情况
            res_a = result_a[i] if len(result_a) >= (i+1) else 0
            res_b = result_b[i] if len(result_b) >= (i+1) else 0
            res_c = result_c[i] if len(result_c) >= (i+1) else 0
            result.append(int(res_a)+int(res_b)+int(res_c))  # 转换成int数组，且排除换行符号

        return result


# 每日PDF统计，2023-05-30优化，增加id条件(增加查询速度)
    def everyday_pdf_count(self):


        # 日新增PDF个数（上传+收录+解压），只统计有效的
        sql_count = "select count(*) from resources_resource where id > {} and ctime BETWEEN '{}' and '{}' and contentType = 300 and " \
                  "`status`='1'".format(self.resource_id,self.start_day,self.end_day)
        # 日PDFdoi查询总数
        sql_doi = "SELECT count(*) FROM `resources_extraattr` where id > {} and utime BETWEEN '{}' and '{}'  and `key` in ('file_documentation_doi' ,'file_documentation_doi_auto') " \
                  "and resource_id in(select id from resources_resource where id > {} and contentType = 300 " \
                  "and `status`=1)".format(self.extraattr_id,self.start_day,self.end_day,self.resource_id)
        # 日PDFdoi查询成功数量
        sql_doi_success = "SELECT count(*) FROM `resources_extraattr` where id > {} and utime BETWEEN '{}' and '{}' and " \
                          "`key` in ('file_documentation_doi_is_hit','file_documentation_doi_auto_is_hit') and resource_id in(select id from " \
                          "resources_resource where id > {} and contentType = 300 and `status`=1) and " \
                          "`value`='1'".format(self.extraattr_id,self.start_day,self.end_day,self.resource_id)
        # 统计语句，进入服务器对应路径
        log_url = 'cd /data/srcpd/cyprex/cyprex/log/cyprex'
        # 标题查询全部，结果除以2,2021-09-22调整，只查request请求
        document_count_shell = 'cat cyprex.log.{} | grep "documentation/info/remote/sync/" | grep ' \
                               '\'"type":"request"\' |  wc -l'\
            .format(self.start_day)
        # 标题查询失败
        document_count_error_shell = 'cat cyprex.log.{} | grep "documentation/info/remote/sync/" |   ' \
                                     'grep \'"data":""\' | wc -l'.format(self.start_day)

        # 执行sql
        sql_all = [sql_count,sql_doi,sql_doi_success]
        result_sql = self.conn_mysql(sql_all)
        self.pdf_count += result_sql[0]
        self.doi_pdf_count += result_sql[1]
        self.doi_pdf_success_count += result_sql[2]
        # 执行linux
        shell_all = [log_url,document_count_shell,document_count_error_shell]
        result_shell = self.conn_linux(shell_all)
        self.document_count = int(result_shell[0])
        self.document_count_error = int(result_shell[1])
        # print(self.pdf_count,self.doi_pdf_count,self.doi_pdf_success_count,self.document_count,self.document_count_error)
        # print(sql_doi)



# 统计caj，由于标题查询无法区分文件类型，这里不再另外查询,2023-05-30优化，增加id条件(增加查询速度)
    def everyday_caj_count(self):
        # 日新增caj个数，只统计有效的
        sql_count = "select count(*) from resources_resource where id > {} and ctime BETWEEN '{}' and '{}' and contentType = 301 and " \
                  "`status`='1'".format(self.resource_id,self.start_day,self.end_day)
        # 日caj doi查询总数
        sql_doi = "SELECT count(*) FROM `resources_extraattr` where id > {} and utime BETWEEN '{}' and '{}' and `key` in ('file_documentation_doi' ,'file_documentation_doi_auto') " \
                  "and resource_id in(select id from resources_resource where id > {} and contentType = 301 " \
                  "and `status`=1)".format(self.extraattr_id,self.start_day,self.end_day,self.resource_id)
        # 日caj doi查询成功数量
        sql_doi_success = "SELECT count(*) FROM `resources_extraattr` where id > {} and utime BETWEEN '{}' and '{}' and " \
                          "`key` in ('file_documentation_doi_is_hit','file_documentation_doi_auto_is_hit') and resource_id in(select id from " \
                          "resources_resource where id > {} and contentType = 301 and `status`=1) and " \
                          "`value`='1'".format(self.extraattr_id,self.start_day,self.end_day,self.resource_id)
        # 执行sql
        sql_all = [sql_count, sql_doi, sql_doi_success]
        result_sql = self.conn_mysql(sql_all)
        self.caj_count += result_sql[0]
        self.doi_caj_count += result_sql[1]
        self.doi_caj_success_count += result_sql[2]

# 统计网页快照次数（仅html）,，2023-05-30优化，增加id条件(增加查询速度) 2023-11-08，注释，系统已取消网页快照功能
    def everyday_webpage_count(self):
        # 统计语句，进入服务器对应路径
        log_url = 'cd /data/srcpd/cyprex/cyprex/log/cyprex'
        # 网页快照html+pdf,统计结果除以2，,2021-09-22调整，只查request请求
        webpage_count_shell = "cat cyprex.log.{} | grep '/web/snapshot/' | grep '\"type\":\"request\"' " \
                              "| wc -l".format(self.start_day)
        # 日html doi查询总数
        sql_doi = "SELECT count(*) FROM `resources_extraattr` where id > {} and utime BETWEEN '{}' and '{}' and `key` " \
                  "in ('file_documentation_doi' ,'file_documentation_doi_auto') " \
                  "and resource_id in(select id from resources_resource where id > {} and contentType = 901 " \
                  "and `status`=1)".format(self.extraattr_id,self.start_day,self.end_day,self.resource_id)
        # 日html doi查询成功数量
        sql_doi_success = "SELECT count(*) FROM `resources_extraattr` where id > {} and utime BETWEEN '{}' and '{}' and " \
                          "`key` in ('file_documentation_doi_is_hit','file_documentation_doi_auto_is_hit') " \
                          "and resource_id in(select id from " \
                          "resources_resource where id > {} and contentType = 901 and `status`=1) and " \
                          "`value`='1'".format(self.extraattr_id,self.start_day,self.end_day,self.resource_id)
        sql_all = [sql_doi, sql_doi_success]
        result_sql = self.conn_mysql(sql_all)
        self.doi_html_count += result_sql[0]
        self.doi_html_success_count += result_sql[1]
        # 执行linux
        shell_all = [log_url, webpage_count_shell]
        result_shell = self.conn_linux(shell_all)
        self.webpage_count = int(result_shell[0])

# 统计doi上传数量（包含bibtex和endnote）,2023-05-30优化，增加id条件(增加查询速度)
    def everyday_doi_upload(self):
        # 统计语句，进入服务器对应路径
        log_url = 'cd /data/srcpd/cyprex/cyprex/log/cyprex'
        # 统计doi上传数量，统计接口调用次数（仅请求，不管响应）
        doi_count_shell = 'cat cyprex.log.{} | grep \'/resource/upload/bibtex/\' ' \
                          '| grep \'"type":"request"\' | wc -l'.format(self.start_day)
        # 执行linux
        shell_all = [log_url, doi_count_shell]
        result_shell = self.conn_linux(shell_all)
        self.doi_up_count = int(result_shell[0])


# 统计笔记数量，2023-05-30优化，增加id条件(增加查询速度)
    def everyday_annotation_count(self):
        # 日增笔记数量,以前的批注（页面删除会直接删除数据），2021-10-08增加类型判断（数据库结构改了）
        sql_annotation = "SELECT count(*) FROM `resources_annotation` where id > {} and ctime BETWEEN '{}' and '{}' " \
                         "and is_excerpt='0'".format(self.annotation_id,self.start_day,self.end_day)
        sql_all = [sql_annotation]
        result_sql = self.conn_mysql(sql_all)
        self.annotation_count = result_sql[0]

# 统计摘录数量，2023-05-30优化，增加id条件(增加查询速度)
    def everyday_excerpt_count(self):
        # 日增摘录数量，2021-10-08调整，不去查询resource表中901了，数据库结构变了
        sql_excerpt = "SELECT count(*) FROM `resources_annotation` where id > {} and ctime BETWEEN '{}' and '{}' " \
                         "and is_excerpt='1'".format(self.annotation_id,self.start_day,self.end_day)
        sql_all = [sql_excerpt]
        result_sql = self.conn_mysql(sql_all)
        self.excerpt_count = result_sql[0]

# 统计文献分析使用次数
    def document_analysis_count(self):
        # 统计语句，进入服务器对应路径
        log_url = 'cd /data/srcpd/cyprex/cyprex/log/cyprex'
        # 统计文献分析接口调用次数
        analysis_count_shall = 'cat cyprex.log.{} | grep  \'resource/doi/extended_info\' | ' \
                         'grep \'"type":"request"\' | wc -l'.format(self.start_day)
        shell_all = [log_url,analysis_count_shall]
        result_shell = self.conn_linux(shell_all)
        self.analysis_count = int(result_shell[0])

# 统计chatGPT查询次数,2023-06-06
    def chatgpt_count(self):
        # sql,查询当天全部
        sql_count = "SELECT count(*) FROM `resources_chat_record` where id > {} and " \
                  "ctime BETWEEN '{}' and '{}' ".format(self.chatgpt_id,self.start_day,self.end_day)
        # 查询当天成功
        sql_success = "SELECT count(*) FROM `resources_chat_record` where id> {} and " \
                      "ctime BETWEEN '{}' and '{}' and chat_status = '2' ".format(self.chatgpt_id,self.start_day,self.end_day)

        # 执行sql
        sql_all = [sql_count,sql_success]
        result_sql = self.conn_mysql(sql_all)
        self.chatgpt_count_all = result_sql[0]
        self.chatgpt_count_success = result_sql[1]
        self.chatgpt_count_fail = self.chatgpt_count_all - self.chatgpt_count_success


# 统计翻译数量,目前无法统计各个渠道，只能统计到总的2021-11月调整之后，客户端的第三方翻译统计不到
    def everyday_translate_count(self):
        # 统计语句，进入服务器对应路径
        log_url = 'cd /data/srcpd/cyprex/cyprex/log/cyprex'
        # 统计翻译功能使用次数，命令执行结果除以2,2021-09-22调整，只查request请求
        translate_count_shell = 'cat cyprex.log.{} | grep "/trans/" | grep \'"type":"request"\' ' \
                                '| wc -l'.format(self.start_day)
        translate_count_error_shell = 'cat cyprex.log.{} | grep "/trans/" |  grep \'"data":""\' | wc -l'.format(self.start_day)
        shell_all = [log_url, translate_count_shell, translate_count_error_shell]
        result_shell = self.conn_linux(shell_all)
        self.translate_count = int(result_shell[0])
        self.translate_count_error = int(result_shell[1])

# 统计ocr数量---2023-05-24补充，ocr服务已终止
    def everyday_ocr_count(self):
        # 统计语句，进入服务器对应路径
        log_url = 'cd /data/srcpd/cyprex/cyprex/log/cyprex'
        # 统计局部ocr使用次数，命令执行
        note_ocr_shell = 'cat cyprex.log.{} | grep "/resource/pdfrect/ocr/" |  grep "data" | wc -l'.format(self.start_day)
        note_ocr_error_shell = 'cat cyprex.log.{} | grep "/resource/pdfrect/ocr/" |  grep \'"data":""\' | wc -l'.format(
            self.start_day)
        # 数据库中全文ocr
        sql_ocr = "select count(*) from (SELECT resource_id,count(resource_id) FROM `resources_extraattr` where utime BETWEEN '{}' and '{}' " \
                  "and `key` in ('is_ocr') GROUP BY resource_id) as ocr".format(self.start_day,self.end_day)
        sql_ocr_fail = "select count(*) from (SELECT resource_id,count(resource_id) FROM `resources_extraattr` " \
                       "where utime BETWEEN '{}' and '{}' and `key` in ('is_ocr') and `value`='0' GROUP BY resource_id) as ocr".format(self.start_day,self.end_day)
        shell_all = [log_url, note_ocr_shell, note_ocr_error_shell]
        result_shell = self.conn_linux(shell_all)
        self.note_ocr = int(result_shell[0])
        self.note_ocr_error = int(result_shell[1])
        sql_all = [sql_ocr, sql_ocr_fail]
        result_sql = self.conn_mysql(sql_all)
        self.ocr_count += result_sql[0]
        self.ocr_error_count = result_sql[1]

# 插件端使用人次统计+触发引用生成次数（add）,citation无法区分端
    def everyday_pluginuse_count(self):
        #sql
        sql_office = "select count(*) from (SELECT count(user_id) FROM `main_logentry` where id > {} and ctime BETWEEN '{}' " \
                     "and '{}'  and source_type='2001' GROUP BY user_id) as count_user_id".format(self.logentry_id,self.start_day, self.end_day)
        sql_wps = "select count(*) from (SELECT count(user_id) FROM `main_logentry` where id > {} and ctime BETWEEN '{}' and '{}'  " \
                  "and source_type='2002' GROUP BY user_id) as count_user_id".format(self.logentry_id,self.start_day,  self.end_day)
        # 统计语句，进入服务器对应路径
        log_url = 'cd /data/srcpd/cyprex/cyprex/log/cyprex'
        # 服务器查询，结果除以2（接口请求和响应都打印）,2021-09-22调整，只查request请求
        citation_add_shell = "cat cyprex.log.{} | grep '/citation/add' | grep '\"type\":\"request\"' | wc -l".format(self.start_day)

        # 执行sql
        sql_all = [sql_office, sql_wps]
        result_sql = self.conn_mysql(sql_all)
        self.plugin_office_use = result_sql[0]
        self.plugin_wps_use = result_sql[1]

        # linux服务器
        shell_all = [log_url, citation_add_shell]
        result_shell = self.conn_linux(shell_all)
        self.plugin_citation_add = int(result_shell[0])


# 统计，汇总结果
    def run_check(self):
        print("开始检查时间"+time.strftime("%Y-%m-%d_%H:%M:%S"))
        self.everyday_pdf_count()  # 统计PDF日增量和doi+标题查询
        self.everyday_caj_count()  # 统计caj日增量和doi+标题查询（标题无法区分）
        # self.everyday_webpage_count()  # 统计网页快照日增量和doi+标题查询（标题无法区分），2023-11-08注销
        self.everyday_annotation_count()  # 日增笔记
        self.everyday_excerpt_count()  # 日增摘录
        # self.everyday_translate_count()  # 翻译统计次数和成功次数 # 2022-08-08 百度翻译api改版，停止了api翻译服务，这里不统计了
        # self.everyday_ocr_count()  # ocr统计次数+成功次数（全文+局部）
        self.everyday_pluginuse_count()  # 插件统计使用人数+引用次数
        self.everyday_doi_upload()  # 2021-09-27新增统计doi上传
        self.document_analysis_count() # 2023-06-06 添加统计文献分析
        self.chatgpt_count()  # 2023-06-06 添加统计chatgpt查询次数


        print('-----------pdf------------')
        print(self.pdf_count,self.doi_pdf_count,self.doi_pdf_success_count,self.document_count,(self.document_count-self.document_count_error))
        print('-----------caj------------')
        print(self.caj_count,self.doi_caj_count,self.doi_caj_success_count)
        print('-------------网页快照---------------')
        # print(self.webpage_count,self.doi_html_count,self.doi_html_success_count)
        print('---------------摘录笔记---------------------')
        print(self.excerpt_count,self.annotation_count)
        print('--------------------翻译---------------------------')
        print(self.translate_count,(self.translate_count-self.translate_count_error))
        print('--------------------ocr---------------------')
        print((self.ocr_count+self.note_ocr),(self.ocr_count+self.note_ocr-self.note_ocr_error-self.ocr_error_count))
        print('------------------插件端--------------------------')
        print(self.plugin_office_use,self.plugin_wps_use,self.plugin_citation_add)
        print('------------------doi上传--------------------------')
        print(self.doi_up_count)
        print('------------------文献分析--------------------------')
        print(self.analysis_count)

        # 准备发送邮件
        email_title = str(self.start_day)+"数据统计"
        email_content = '<html>'\
                    '<head><title>check report</title></head>'\
                    '<body>'\
                    '<h3>数据统计结果集合：{}</h3>'\
                    '<table border="1px">'\
                    '<tr><td>新增PDF个数</td><td>获取DOI次数</td><td>DOI查询成功次数</td><td>标题查询次数</td><td>标题查询成功次数</td></tr>'\
                    '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'\
                    '</table><br>'\
                    '<table border="1px">'\
                    '<tr><td>新增caj个数</td><td>获取DOI次数</td><td>DOI查询成功次数</td></tr>'\
                    '<tr><td>{}</td><td>{}</td><td>{}</td></tr>'\
                    '</table><br>'\
                    '<table border="1px">'\
                    '</table><br>'\
                    '<table border="1px">'\
                    '<tr><td>新增摘录个数</td><td>新增笔记个数</td></tr>'\
                    '<tr><td>{}</td><td>{}</td></tr>'\
                    '</table><br>'\
                    '<table border="1px">'\
                    '<tr><td>office端登录人数</td><td>wps端登录人数</td><td>引用次数</td></tr>'\
                    '<tr><td>{}</td><td>{}</td><td>{}</td></tr>'\
                    '</table><br>' \
                    '<table border="1px">' \
                    '<tr><td>doi上传次数</td><td>文献分析次数</td></tr>' \
                    '<tr><td>{}</td><td>{}</td></tr>' \
                    '</table><br>' \
                    '<table border="1px">' \
                    '<tr><td>AI助手调用次数</td><td>AI助手成功次数</td></tr>' \
                    '<tr><td>{}</td><td>{}</td></tr>' \
                    '</table><br>' \
                    '</body>'\
                    '</html>'.format(self.start_day,self.pdf_count,self.doi_pdf_count,self.doi_pdf_success_count,self.document_count
                                     ,(self.document_count-self.document_count_error),self.caj_count,self.doi_caj_count
                                       ,self.doi_caj_success_count

                                     ,self.excerpt_count
                                       ,self.annotation_count,
                                       self.plugin_office_use,self.plugin_wps_use,self.plugin_citation_add
                                     ,self.doi_up_count,self.analysis_count,self.chatgpt_count_all,self.chatgpt_count_success)
        send_mail(subject=email_title,content=email_content,receive=EmailProperty().RECEVI_EMAIL2)
        print('执行完成')
        print("结束检查时间" + time.strftime("%Y-%m-%d_%H:%M:%S"))





if __name__ == "__main__":
    EveryDayMethod().run_check()
    # EveryDayMethod().chatgpt_count()






