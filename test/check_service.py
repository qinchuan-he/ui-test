#coding=utf-8

import socket
from common.private import network
from common.comfunction import send_mail
# 检查服务方面的，如果出现问题及时报警或者重启服务--目前预计的2服务放入check_report——twohours服务


def check_hk_network():
    ip = network().hk_ip
    port = 80  # 请求端口，80或者443都行
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # 创建套接字
    s.settimeout(5)  # 设置超时时间
    result = s.connect_ex((ip,port))  # 创建套接字连接
    if result == 0:
        print('连接畅通')
    else:
        print('连接不上')

    return result

def get_report():
    ip_check = check_hk_network()
    if ip_check != 0:
        #  有问题准备发邮件
        result = '阿里云香港服务器网络连通异常'
        subject = "服务相关检查"
        content = "<hmtl><header></header><body><div>{}<div><div>香港ip为{}，端口是80<div></body></html>".format(result,network().hk_ip)
        send_mail(subject, content=content)


if __name__=='__main__':
    # check_hk_network()
    get_report()
