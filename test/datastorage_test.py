

import os
import json
import requests

# 公告和研报解析接口
def analysis():
    """ 数据组pdf公告解析接口"""
    url = 'http://192.168.1.219:8016/data/api/algorithm/algorithm'
    argument = {'algo_type':'pdf2html','pdf_type':'notice'}   # 公告
    # argument = {'algo_type':'pdf2html','pdf_type':'report'} # 研报
    # folder_path = 'D:\\上传文件\\pdf比对\\数据组--样本文件\\研报' # 研报数据
    folder_path = 'D:\\上传文件\\pdf比对\\数据组--样本文件\\' # 公告数据
    lst = []
    for i in os.listdir(os.path.join(folder_path)):
        # file_path = file_bash_pash+i
        file_path = os.path.join(folder_path,i)
        print(file_path)
        file = {'file': open(file_path, 'rb')}
        res = requests.post(url,data=argument,files=file)
        res_text=res.text
        print(res_text)
        try:
            res_j = json.loads(res_text).get('data')
            lst.append(res_j)
        except Exception as e:
            print('这个解析失败了')

    print('-------------------------------')
    print(lst)
if  __name__=='__main__':
    analysis()   # 数据组公告接口
