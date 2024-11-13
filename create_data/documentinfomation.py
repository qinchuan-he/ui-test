# coding = utf-8

import requests
import json

# 获取文献信息,提取文献信息
def get_documentinfo():
    cookie = {'fir_session_id':'9209gwvaw0wg3vpcubluqqhn1uzakb2t'}
    url1 = 'https://testapp.fir.ai/api/resource/personal/list/?ordering=-shareUserName&include=infoCat&include=info&pageRow=50&pId=nW4wNRD3LE8MlqXJ'

    url2 = "https://testapp.fir.ai/api/resource/documentation/info/remote/"

    # 获取文件列表
    folder = []
    res = requests.get(url=url1,cookies=cookie)
    li = json.loads(res.text)
    for i in li.get("data").get("list"):
        if i.get("contentType")==301 or i.get("contentType")==300:
            # folder.append(i.get("id"))
            # 触发请求，提取文献信息
            data_2 = {"oid":i.get("id")}
            res2 = requests.post(url=url2,data=data_2,cookies=cookie)
            print(json.loads(res2.text).get("msg"))

    # print(folder)
    # print(li.get("data").get("list"))





if __name__=="__main__":
    get_documentinfo()


