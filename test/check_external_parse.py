# coding = utf-8
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0, rootPath)
import paramiko
from common.private import ServerInfo
import time
from common.comfunction import send_mail


"""
任务：接口测试账号：PDF解析+OCR解析根据IP每天自动发调用量+明细
实现：检查221服务器中的日志，输出查询的结果发送邮件
"""


# 统计PDF解析服务使用次数
def check_pdf_parse():
    try:
        ssh_host = ServerInfo().host
        ssh_port = ServerInfo().port
        ssh_user = ServerInfo().user
        ssh_pwd = ServerInfo().pwd

        ssh_client = paramiko.SSHClient()
        key = paramiko.AutoAddPolicy()
        ssh_client.set_missing_host_key_policy(key)
        ssh_client.connect(hostname=ssh_host, port=ssh_port, username=ssh_user, password=ssh_pwd)

        # 获取对应容器id
        container_name = ServerInfo().container_name
        stdin, stdout, stderr = ssh_client.exec_command('docker ps --filter "name={}"'.format(container_name))
        result = stdout.readlines()
        container_id = result[1].split()[0]

        # 获取文件在docker中路径
        inner_container_file_path = ServerInfo().inner_container_file_path
        # cat info.log | grep 2020-08-07| grep 'request_user_info' | awk '{print $1" "$2" "$9" "$10}'
        stdin, stdout, stderr = ssh_client.exec_command(
            'docker cp  {}:{} {}'.format(container_id, inner_container_file_path, ServerInfo().server_folder_path))
        msg = stdout.read().decode('utf-8')
        # 获取文件中内容
        current_day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        stdin, stdout, stderr = ssh_client.exec_command(
            "cat {} | grep {} | grep 'request_user_info' | awk '{{print {}}}'"
            .format(ServerInfo().server_file_path, current_day, '$1" "$2" "$9" "$10'))
        msg = stdout.read().decode('utf-8')
        result_msg = msg.split('\n')
        # print(len(result_msg))
        # print(result_msg)
        return result_msg
    except Exception as e:
        print(e)
        result_msg = []
        return result_msg


# 统计ocr服务使用次数
def check_ocr():
    try:
        ssh_host = ServerInfo().host
        ssh_port = ServerInfo().port
        ssh_user = ServerInfo().user
        ssh_pwd = ServerInfo().pwd
        ssh_client = paramiko.SSHClient()
        key = paramiko.AutoAddPolicy()
        ssh_client.set_missing_host_key_policy(key)
        ssh_client.connect(hostname=ssh_host, port=ssh_port, username=ssh_user, password=ssh_pwd)

        # 获取对应容器id
        container_name = ServerInfo().container_name_2
        stdin, stdout, stderr = ssh_client.exec_command('docker ps --filter "name={}"'.format(container_name))
        result = stdout.readlines()
        container_id = result[1].split()[0]

        # 获取文件在docker中路径
        inner_container_file_path = ServerInfo().inner_container_file_path_2

        stdin, stdout, stderr = ssh_client.exec_command(
            'docker cp  {}:{} {}'.format(container_id, inner_container_file_path, ServerInfo().server_folder_path))
        msg = stdout.read().decode('utf-8')
        # 获取文件中内容
        current_day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        stdin, stdout, stderr = ssh_client.exec_command(
            "cat {} | grep {} | grep 'request_user_info' | awk '{{print {}}}'"
                .format(ServerInfo().server_file_path_2, current_day, '$1" "$3" "$4'))
        msg = stdout.read().decode('utf-8')

        result_msg = msg.split('\n')
        return result_msg
    except Exception as e:
        print(e)
        result_msg = []
        return result_msg


# 发送邮件
def send_msg():
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    title = '{} 日PDF和OCR解析服务调用报告'.format(current_time)
    content_start = '<html><header><h1>PDF解析调用0次,ocr服务调用0次</h1></header><body><table border="1">'
    content_body = '<tr><td width="50px">序号</td><td width="100px">日期</td><td width="100px">时间</td><td width="100px">IP地址</td><td width="500px">请求接口</td></tr>'
    content_end = '</table></body></html>'
    msg = check_pdf_parse()
    word2txt_num = 0
    word2html_num = 0
    pdftxtformat_num = 0
    if msg:
        for i in range(len(msg) - 1):
            if 'word2html' in msg[i]:
                word2html_num += 1
            elif 'pdf_fragment' in msg[i] and 'text_images' in msg[i]:
                pdftxtformat_num += 1
            elif 'word2txt' in msg[i]:
                word2txt_num+=1


        content_start = '''
        <html>
        <header>
        <h1>文件解析服务:pdf解析纯文本调用{}次, word转换html服务调用{}次,word转TXT服务调用{}次</h1>
        <h1> ocr服务调用0次</h1><h3>调用明细如下：</h3>
        </header>
        <body>
        <table border="1">'''.format(
            pdftxtformat_num, word2html_num,word2txt_num)
        for i in range(len(msg) - 1):
            try:
                tr = msg[i].split(" ")
                content_body = content_body + '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(
                    i + 1, tr[0], tr[1], tr[2], tr[3])
            except Exception as e:
                print(i)
                print(e)
    msg_2 = check_ocr()
    if msg_2:
        content_start = '''
        <html>
        <header>
        <h1>文件解析服务:pdf解析纯文本调用{}次, word转换html服务调用{}次,word转TXT服务调用{}次</h1>
        <h1> ocr服务调用{}次</h1><h3>调用明细如下：</h3>
        </header>
        <body>
        <table border="1">'''.format(
            pdftxtformat_num, word2html_num,word2txt_num, len(msg_2) - 1)
        for i in range(len(msg_2) - 1):
            try:
                tr = msg_2[i].split(" ")
                content_body = content_body + '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(
                    i + 1, tr[0], '--', tr[1], tr[2])
            except Exception as e:
                print(i)
                print(e)
    content_all = content_start + content_body + content_end
    send_mail(subject=title, content=content_all)
    print('执行完成')


if __name__ == "__main__":
    # check_pdf_parse()
    send_msg()
