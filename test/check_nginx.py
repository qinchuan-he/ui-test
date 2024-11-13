#coding=utf-8

import os,sys
# 解决Linux中找不到引用问题
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)

import paramiko
from common.private import DB,ServerInfo,EmailProperty
from common.comfunction import send_mail

# 检查5017中nginx的错误日志，如果有报错就发邮件提示

# 连接服务器
def conn_linux(shell_list):
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
    # 连接第一台服务器5017
    shell_content = "" # 查询语句
    # 拼装Linux命令
    for i in range(len(shell_list)):
        if i == 0:
            shell_content = shell_list[i]
        else:
            shell_content = shell_content + ';' + shell_list[i]
    try:
        client.connect(hostname=host_name, port=host_port, username=username, pkey=private_key)
        stdin, stdout, stderr = client.exec_command(shell_content)
        result_a = stdout.readlines()

    except Exception as e:
        print(e)
    client.close()
    return result_a

# 查询nginx错误日志
def check_error():
    # 统计语句，进入服务器对应路径
    log_url = 'cd /fir/log'
    # 排除错误，访问无权限，接口超时
    shell = "cat nginx_error.log | grep -v 'access forbidden by rule' | grep -v 'upstream timed out' " \
            "| grep -v 'Permission denied'"
    shell_all = [log_url,shell]
    res = conn_linux(shell_all)
    res_count = len(res)
    email_count = res_count if res_count < 50 else 50
    if res_count != 0:
        email_content = "<html><head></head><body><h3>nginx报错邮件最多显示50条，本次"+str(email_count)+"条</h3>"
        if res_count > 50:
            for i in range(50):
                email_content = email_content+"<p>"+res[i]+"</p>"
        else:
            for i in res:
                email_content = email_content+"<p>"+i+"</p>"

        # 准备发送邮件
        email_title = "nginx日志检查有问题"
        # print(len(res))
        email_content = email_content+"</body></html>"
        send_mail(subject=email_title, content=email_content)
    print('执行完成')


if __name__ == "__main__":
    check_error()














