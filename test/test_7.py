
import time
import requests

cookie = {'fir_session_id':'hwzotad78chhae9ykgv7ppc4sbu4naxd'}

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






if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    mobiles = ['10085632551','10058214521','17091921573','10058632541']
    for i in mobiles:
        createUser(i)

    # 创建部门
    # num=100000
    # for i in range(35):
    #     num +=1
    #     createDepartment(str(num))


















