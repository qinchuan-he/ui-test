# coding=utf-8

import hmac
import json
import base64
import datetime
import uuid
params = {"file_id":"569653f3-6f25-42f0-b9ef-8b0dc00d59aa", "file_name":"我要开始修订了.docx", "user_id":375}
temp = base64.b64encode(json.dumps(params).encode("utf8"))
sign = hmac.new('49aea739-dedf-4ad4-9a65-8356f715b3db'.encode('utf8'), msg=temp, digestmod="MD5").hexdigest()
params =temp.decode()
# print(params)
# print(sign)

print("""预览地址：
    http://192.168.1.224:8060/data/fetch?view_type=preview&params=%s&sign=%s""" % (params,sign))
print("""编辑地址：
    http://192.168.1.224:8060/data/fetch?view_type=editor&params=%s&sign=%s""" % (params,sign))
# print(str(uuid.uuid4()))

# print(str(datetime.datetime.now()))
# s =str(datetime.datetime.now())[:19]
# print(str(datetime.datetime.now())[1::])
# print(str(datetime.datetime.now())[1::-1]) # 从下标1开始往前，直到下标0
# print(str(datetime.datetime.now())[::-1])
# print(str(datetime.datetime.now())[:19])
# print(len(s))

# http://192.168.1.224:8060/data/fetch?view_type=editor&params=&sign=

# http://192.168.1.224:8060/data/fetch?view_type=preview&params=&sign=
