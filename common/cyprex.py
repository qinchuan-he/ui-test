#coding=utf-8

import requests


# 触发会员到期提醒接口：post方式,每天中午12点定时推送消息，手动发送消息,该接口是全局发送的，扫描全系库
def expiration():
    cookie = {'fir_session_id':'o973xm5wb1ayiafb80ksqhqeyl8o8meq'}
    url = 'https://testapp.fir.ai/api/send/vipExpirationRemind/'
    res = requests.post(url=url,cookies=cookie)
    print(res.text)



if __name__=='__main__':
    expiration()





