import json
import re
import datetime
import time
from datetime import timedelta

import requests

from common.private import EmailProperty
from common.comfunction import send_mail


def extract_ips(filename):
    with open(filename, 'r') as file:
        content = file.read()  # 读取整个文件内容
        ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", content)  # 使用正则表达式匹配IP地址
        ips = list(set(ips))  # 去重处理

    # 输出到txt文件
    with open('1013_ip.txt', 'w') as f:
        for ip in ips:
            f.write(ip + '\n')
    return ips


def feibolaqi(n):

    fib = [1, 2] + [0] * (n - 2)
    for i in range(2,n):
        fib[i] = fib[i-2]+fib[i-1]
    print(fib[n-1])

# filename = "example.txt"  # 替换为你的txt文件名
# filename = r"D:\2\1013.txt"  # 替换为你的txt文件名
# ips = extract_ips(filename)
# for ip in ips:
#     print(ip)

# 检查两段文本是否一致
def check_text():
    # pdf解析服务输出
    start = "This paper presents a general formulation of an isogeometric collocation method (IGA-C) for the parameterization of computational domains for the isogeometric analysis (IGA) using non-uniform rational B-splines (NURBS).The boundary information of desired computational domains for IGA is imposed as a Dirichlet boundary condition on a simple and smooth initial parameterization of an initial computational domain, and the final parameterization is produced based on the numerical solution of a partial differential equation (PDE) that is solved using the IGA-C method.In addition, we apply intuitive derivative constraints while solving the PDE to achieve desired properties of smoothness and uniformity of the resulting parameterization.While one may use any general PDE with any constraint, the PDEs and additional constraints selected in our case are such that the resulting solution can be efficiently solved through a system of linear equations with or without additional linear constraints.This approach is different from typical existing parameterization methods in IGA that are often solved through an expensive nonlinear optimization process.The results show that the proposed method can efficiently produce satisfactory analysis-suitable parameterizations."

    #原文中复制去除换行内容
    end =  "This paper presents a general formulation of an isogeometric collocation method (IGA-C) for the parameterization of computational domains for the isogeometric analysis (IGA) using non-uniform rational B-splines (NURBS). The boundary information of desired computational domains for IGA is imposed as a Dirichlet boundary condition on a simple and smooth initial parameterization of an initial computational domain, and the final parameterization is produced based on the numerical solution of a partial differential equation (PDE) that is solved using the IGA-C method. In addition, we apply intuitive derivative constraints while solving the PDE to achieve desired properties of smoothness and uniformity of the resulting parameterization. While one may use any general PDE with any constraint, the PDEs and additional constraints selected in our case are such that the resulting solution can be efficiently solved through a system of linear equations with or without additional linear constraints. This approach is different from typical existing parameterization methods in IGA that are often solved through an expensive nonlinear optimization process. The results show that the proposed method can efficiently produce satisfactory analysis-suitable parameterizations."

    #正则匹配
    reg = r'[, .-]+'
    re_start=re.split(reg,start)
    re_end=re.split(reg,end)
    print(re_start)
    print(re_end)
    print(len(re_start))
    print(len(re_end))
    if len(re_start)==len(re_end):
        print("长度相等")
        for i in range(len(re_start)):
            if re_start[i]==re_end[i]:
                pass
            else:
                print(re_start[i])

    else:
        print("长度不相等")

def check_context():
    path = r"D:\上传文件\pdf比对\9doi提取+智能提取+arXiv\新智能提取--2023-06\英文文档\有doi文档引用显示作者\临时存放pdf解析内容.txt"
    file1 = open(path,'r',encoding='utf-8')

    text1=file1.read()
    file1.close()
    text2 = "The isogeometric collocation method (IGA-C) was introduced as an alternative approach to conduct engineering analysis without the need of expensive numerical integrations, as required in the standard isogeometric Galerkin methods (IGA-G). The main idea of IGA-C rests on the discretization of the governing partial differential equations (PDEs) in strong form at designated collocation positions. The use of the IGA-C method leads to the use of a reduced number of evaluations needed for the formation of solution matrix to only one-per-degree of freedom and reduces the computational cost (Hughes et al., 2005; Auricchio et al., 2010, 2012). A detailed study on computation cost and accuracy of IGA-C in comparison with IGA-G was reported by Schillinger et al. (2013). The consistency and convergence properties of the IGA-C method were also studied by Lin et al. (2013). The advantage of low computational cost with promising results attracts many researchers across the globe to use IGA-C method in various applications including phase-field modeling (Gomez et al., 2014; Fedeli et al., 2019), contact problems (De Lorenzis et al., 2015; Kruse et al., 2015), nonlinear elasticity (Kruse et al., 2015), and in the context"

    # 对两个字符串进行加工
    reg = r"[ .,]+"
    list1 = re.split(reg,text1)
    list2 = re.split(reg,text2)
    for i in range(len(list2)):
        if list1[i] == list2[i]:
            pass
        else:
            print("本段验证有问题")
            print(list1[i])
            print(list2[i])
            break
    print("本段验证通过")

def check_date():
    s = '2024-03-01'
    s1 =datetime.datetime.strptime(s, '%Y-%m-%d')
    s2 = datetime.timedelta(days=90)
    print(s1+s2)
    print(time.time())

def check_url():
    url_s = "http://192.168.7.192:6060/api/TokenAuth/Authenticate"
    url_s = "https://ius-xcx.51xi.com:6060/api/TokenAuth/Authenticate"
    data_s = {"userNameOrEmailAddress":"admin","password":"Test123456","clientType":"PC"}
    json_s = {"userNameOrEmailAddress":"scan","password":"Ab123456","clientType":"PC"}
    headers_s = {"Content-Type": "application/json","tenant":"9b9dfa4d04a7e8bd55c33a14ebf0966c" }
    headers_s = {"Content-Type": "application/json","tenant":"1d0466fb60e473a9159d3a14c077b265" }
    # 登录获取token
    res = requests.post(url=url_s,json=json_s,headers=headers_s)
    print(type(res.text))
    print(res.text)
    # 设置token
    result_s = json.loads(res.text)
    token = result_s['result']['accessToken']
    print(token)
    token_s = "Bearer "+token
    print(token_s)

    url_Clean = "https://ius-xcx.51xi.com:6060/api/services/app/CleanAreaDailyManager/GetCleanAreaCharts"
    headers_clean = {"Content-Type": "application/json","tenant":"1d0466fb60e473a9159d3a14c077b265","authorization":token_s }
    res_claen = requests.get(url=url_Clean,headers=headers_clean)
    print(res_claen.text)
    status_s = json.loads(res_claen.text)['success']
    print(status_s)
    print(type(status_s))
    if status_s:
        print("成功请求到区域管理数据")

def check_mail():
    date_s = time.time()
    s = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(date_s)
    print(s)


if __name__=="__main__":
    # feibolaqi(1)
    # check_text()
    # check_context()
    # check_date()
    # check_url()
    check_mail()








