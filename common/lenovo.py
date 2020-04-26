import hmac
import json
import base64
import datetime
import uuid

import requests


def gen(url, params):
    """user_id int类型  rev 版本号 不传默认为打开最新版本"""

    temp = base64.b64encode(json.dumps(params).encode("utf8"))
    api_key = '49aea739-dedf-4ad4-9a65-8356f715b3db'
    sign = hmac.new(api_key.encode('utf8'), msg=temp, digestmod="MD5").hexdigest()
    params = temp.decode()
    # print(params)
    # print(sign)

    url = "%sparams=%s&sign=%s" % (url, params, sign)
    print(url)
    return url

def test_api(file_name,file_id,rev,user_id,view_type):
    """ 测试环境使用"""
    url = "http://192.168.1.224:8061/api/file/parse?"
    params = {"file_id": file_id, "rev": rev, "opt_type": "01"}
    url_3 = gen(url, params)
    res = requests.get(url_3)
    print(res.text)
    url = "http://192.168.1.224:8060/data/fetch?"
    params = {"file_id": file_id, "view_type": view_type, "file_name": file_name, "rev": rev, "user_id": user_id}
    gen(url, params)

if __name__ == '__main__':
    # 必传rev
    # url = "http://localhost:4000/data/fetch?"
    # params = {"file_id": 141, "view_type": "preview", "file_name": "新建 Microsoft Word 文档.docx", "rev": "6dc8564a15644c8aae70774f25b5eb01", "user_id": 27}

    # 第一入口解析
    #     # url = "http://192.168.1.62:8099/api/file/parse?"
    #     # params = {"file_id": 141,  "rev": "6dc8564a15644c8aae70774f25b5eb01", "opt_type": "01"}

    # 测试环境,先调数据组接口，再生成前端页面访问接口
    # user_id = 27
    # file_name = '图例验证文件.pdf'
    # neid = 144
    # rev = '129e5cf528ea4857b11c03982a52d770'
    user_id = 27
    file_name = '表格图片.doc'
    neid = 145
    rev = '0c1466f88a124d32bb244eccc6a39217'
    # view_type = 'preview'
    view_type = 'editor'
    test_api(file_name,neid,rev,user_id,view_type)




