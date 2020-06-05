
import time
import requests
from time import sleep
cookie = {'fir_session_id':'r6kdefcehubwmwk8w1vml6knx5x5r1dz'}

def createUser(mobile:str):
    """ 添加成员"""
    # cookie = {'fir_session_id':'hwzotad78chhae9ykgv7ppc4sbu4naxd'}
    dates = {'mobile':mobile,'position':'测试部门','department_id_list':[]}
    url = 'https://testcyprex.fir.ai/api/company/staff/create/'
    res = requests.post(url=url,data=dates,cookies = cookie)
    print(res.text)

def createDepartment(name:str):
    """ 创建部门"""
    datas = {'pid':'','name':name}
    url = 'https://testcyprex.fir.ai/api/company/department/create/'
    res = requests.post(url=url,data=datas,cookies = cookie)
    print(res.text)

def createlog():
    """ 创建动态"""
    anme = str(time.time())
    url = 'https://testcyprex.fir.ai/api/resource/merge/form/'
    datas = {'catList':'[{"id":"n9rGO8WXYJRNa3kE","name":"'+anme+'","teamId":"AkX3KGRaedRwpYZj"}]'}
    res = requests.post(url,data=datas,cookies = cookie)
    print(datas)
    print(res.text)
    sleep(0.2)


if __name__ == "__main__":
    # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    # banned = ["hit"]
    # mobiles = ['10085632551','10058214521','17091921573','10058632541']
    # for i in mobiles:
    #     createUser(i)
    for i in range(20):
        createlog()
    # 创建部门
    # num=100000
    # for i in range(35):
    #     num +=1
    #     createDepartment(str(num))


















