#coding=utf-8

import paramiko
import datetime
import pymysql

import os,sys
# 解决Linux中找不到引用问题
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)

from common.private import DB
from common.comfunction import send_mail

# 检查第三方服务调用情况，登录线上服务器5017，查看日志。连接数据库查询

def check_documentinfo():
    check_date = [1,2,3,4,5]
    host_name = DB.host
    host_port = 5017
    username=DB.user

    db_name = DB.db_cyprex
    db_port = int(DB.port)
    db_user = DB.user
    db_pwd = DB.pwd

    private_file = r'D:\2\本机密钥\id_rsa1_2048'
    # private_file = r'/opt/tomcat/webapps/ui-test/common/id_rsa1_2048'
    day = datetime.datetime.now().date()
    date = day.isoweekday()

    if date in check_date: # 判断是检查日，就执行后续检查
        private_key = paramiko.RSAKey.from_private_key_file(private_file)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        document_count = 0 # 标题查询
        document_count_error = 0
        note_ocr = 0 # 局部ocr
        note_ocr_error = 0
        translate_count = 0 #翻译
        translate_count_error = 0
        doi_count = 0 #doi查询
        doi_error_count=0
        ocr_count = 0 #全文ocr
        ocr_error_count = 0
        client.connect(hostname=host_name,port=host_port,username=username,pkey=private_key)
        #循环星期，2021-08-10增加上周六和周日的统计
        for i in range(1, +3):
            date_d = datetime.timedelta(days=-(i-1))
            days=day+date_d
            # 统计语句
            log_url = 'cd /data/srcpd/cyprex/cyprex/log/cyprex'
            # 统计文献获取，命令执行结果除以2
            document_count_shell = 'cat cyprex.log.{} | grep "documentation/info/remote/sync/" |  wc -l'.format(days)
            document_count_error_shell = 'cat cyprex.log.{} | grep "documentation/info/remote/sync/" |   grep \'"data":""\' | wc -l'.format(
                days)
            # 统计局部ocr使用次数，命令执行
            note_ocr_shell = 'cat cyprex.log.{} | grep "/resource/pdfrect/ocr/" |  grep "data" | wc -l'.format(days)
            note_ocr_error_shell = 'cat cyprex.log.{} | grep "/resource/pdfrect/ocr/" |  grep \'"data":""\' | wc -l'.format(days)
            # 统计翻译功能使用次数，命令执行结果除以2
            translate_count_shell = 'cat cyprex.log.{} | grep "/trans/" | wc -l'.format(days)
            translate_count_error_shell = 'cat cyprex.log.{} | grep "/trans/" |  grep \'"data":""\' | wc -l'.format(days)

            stdin, stdout, stderr = client.exec_command('{};{};{};{};{};{};{}'.format(log_url,document_count_shell
                                                                                      ,document_count_error_shell,note_ocr_shell
                                                                                      ,note_ocr_error_shell,translate_count_shell
                                                                                      ,translate_count_error_shell))
            count_s = stdout.readlines()
            document_count+=int(int(count_s[0])/2)
            document_count_error+=int(count_s[1])
            note_ocr += int(count_s[2])
            note_ocr_error += int(count_s[3])
            translate_count += int(int(count_s[4])/2)
            translate_count_error += int(count_s[5])
            #如果循环到周一，使用周一时间去数据库查（查询大于周一时间就行）,2021-08-10
            if days.isoweekday()==6:
            # 连接数据库，查询doi和全文ocr,这里只查手动的
                connect = pymysql.connect(host=host_name,database=db_name,port=db_port,user=db_user,password=db_pwd)
                cur = connect.cursor()
                sql_doi = "select count(*) from (SELECT resource_id,count(resource_id) FROM `resources_extraattr` " \
                          "where utime>'{}' and `key` in ('file_documentation_doi','file_documentation_doi_is_hit') " \
                          "GROUP BY resource_id) as doi".format(days)
                sql_doi_fail = "select count(*) from (SELECT resource_id,count(resource_id) FROM `resources_extraattr` " \
                               "where utime>'{}' and `key` in ('file_documentation_doi','file_documentation_doi_is_hit') " \
                               "and `value`='0' GROUP BY resource_id) as doi".format(days)
                sql_ocr = "select count(*) from (SELECT resource_id,count(resource_id) FROM `resources_extraattr` where utime>'{}' " \
                          "and `key` in ('is_ocr') GROUP BY resource_id) as ocr".format(days)
                sql_ocr_fail = "select count(*) from (SELECT resource_id,count(resource_id) FROM `resources_extraattr` " \
                               "where utime>'{}' and `key` in ('is_ocr') and `value`='0' GROUP BY resource_id) as ocr".format(days)
                # 查询上传文件自动获取的doi查询情况（该表只保存获取成功的）
                sql_doi_log = "SELECT count(*) FROM resources_doilog where ctime > '{}'".format(days)
                cur.execute(sql_doi)
                doi_count= int(cur.fetchall()[0][0])
                cur.execute(sql_doi_fail)
                doi_error_count = int(cur.fetchall()[0][0])
                cur.execute(sql_ocr)
                ocr_count = int(cur.fetchall()[0][0])
                cur.execute(sql_ocr_fail)
                ocr_error_count = int(cur.fetchall()[0][0])
                # 统计doi次数，手动触发和自动触发相加
                cur.execute(sql_doi_log)
                doi_count+=int(cur.fetchall()[0][0])

                #准备发送邮件
                subject = "周例行检查--第三方服务调用情况"
                content = '<html><head></head><body><h3>周外部服务调用情况</h3>文献获取：{}次（成功{},失败：{}）<br>' \
                          'DOI获取次数：{}次（成功{},失败：{}）<br>' \
                          'ocr全文识别：{}次（成功{},失败：{}）<br>' \
                          'ocr局部识别：{}次（成功{},失败：{}）<br>' \
                          '翻译：{}次（成功{},失败：{}）<br></body></html>'.format(document_count,document_count-document_count_error,document_count_error
                                                                        ,doi_count,doi_count-doi_error_count,doi_error_count
                                                                        ,ocr_count,ocr_count-ocr_error_count,ocr_error_count
                                                                        ,note_ocr,note_ocr-note_ocr_error,note_ocr_error
                                                                        ,translate_count,translate_count-translate_count_error,translate_count_error)
                cur.close()
                connect.close()
                send_mail(subject,content=content)


def cc():
    a = [1,2,'0\n']
    b = round(81.915,2)
    print(b)


if __name__=='__main__':
    # check_documentinfo()
    cc()


