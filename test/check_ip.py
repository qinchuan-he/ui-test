

import requests
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)
from common.comfunction import send_mail
from common.private import network
import time
from  time import sleep


#获取公司服务器外网ip地址，报告中获取会受到ucloud权限限制，不好使，单独写一个，配置一个当前ip,company_ip
#2023-06-16 修改获取ip网址为https://myip.ipip.net/，2024-01-26发现该网站无法使用
#2024-01-26 使用获取ip网站为：https://www.ipuu.net/ipuu/user/getIP
def get_firip():
    company_ip = '223.166.96.231'  # 2023-09-04 公司ip
    company_ip = network().company_ip  # 2023-11-13 公司ip写入配置文件

    url = "https://2023.ip138.com/"
    url = "https://myip.ipip.net/"
    url = "https://www.ipuu.net/ipuu/user/getIP"
    payload = ""
    headers = {
        'User-Agent': "PostmanRuntime/7.11.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "55e7be78-cf66-4180-990f-d34b60ad2805,5232b4fd-a299-4eca-b0b0-28c711211734",
        'Host': "2023.ip138.com",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    # 补充一个逻辑，第一次没有正常响应之后5分钟之后再发一次请求
    count = 1
    while count < 2:
        # response = requests.request("GET", url, data=payload, headers=headers)
        response = requests.request("GET", url)
        result_code = response.status_code
        result_ip = response.text
        print(result_ip)
        count = count+1
        # 请求成功跳出循环
        if str(result_code) == '200':
            print('响应正常')
            break
        else:
            print('响应code非200，再请求一次')
            sleep(100)

    # now_ip = result_ip.split("IP：", 2)[1].split("来自于", 2)[0].strip()
    # 224-01-26调整
    now_ip = result_ip.split('"data":"', 2)[1].split('"', 2)[0].strip()

    print(now_ip)

    # return ip
    # print(company_ip)
    # print(now_ip)
    if now_ip == company_ip:
        print("ip没变")
    else:
        print("ip变了")
        subject = "公司ip地址变更通知"
        content = "<hmtl><header></header><body><div>{}<div></body></html>".format(result_ip)
        send_mail(subject, content=content)
        print("邮件发送完成")
    #为了保险增加了一个2小时发送一次的机制
    # time_array = [8, 10, 12, 14, 16, 18, 20, 22]
    # nowtime = time.strftime('%y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # nowtime_h = int(nowtime.split(' ')[1].split(':')[0])
    # nowtime_m = int(nowtime.split(' ')[1].split(':')[1])
    # if nowtime_m < 25 and nowtime_h in time_array:
    #     subject = "ip地址"
    #     content = "<hmtl><header></header><body><div>{}<div></body></html>".format(result_ip)
    #     send_mail(subject, content=content)
    #     print("邮件发送完成")


if __name__=='__main__':
    get_firip()









