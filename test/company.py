
import time
import requests
from time import sleep
cookie = {'fir_session_id':'d2klnfvnxpc7su9acm459zys9b999cud'}

def createUser(mobile:str):
    """ 企业后台中企业添加成员 ，需要企业管理员的session"""
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

# 删除企业员工
def delete_staff():
    """ 传入company_companystaffmapping表中的staff_id"""
    url = 'https://testcyprex.fir.ai/api/company/staff/delete/'
    data = {'staff_id_list':str([10,37,49,6,7])}
    res = requests.post(url=url,data=data,cookies = cookie)
    print(res.text)

if __name__ == "__main__":
    # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    # banned = ["hit"]
    # delete_staff()
    mobiles = ['13223652214']
    for i in mobiles:
        createUser(i)
    # for i in range(20):
    #     createlog()
    # 创建部门
    # num=100000
    # for i in range(35):
    #     num +=1
    #     createDepartment(str(num))


















