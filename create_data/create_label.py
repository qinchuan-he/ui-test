# coding=utf-8

import requests
import time

# 创建按钮

def c_label():
    url ='https://app.fir.ai/api/resource/tag/form/'
    cookie = {'fir_session_id':'8y88ce326kedlplxbdubqwp5n9ys61lx'}
    data_s = {'name':'标签'+str(time.time())}
    print(data_s)
    res = requests.post(url=url,data=data_s,cookies=cookie)
    print(res.text)


if __name__=='__main__':
    for i in  range(100):
        c_label()













