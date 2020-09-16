
import requests
import os
import time
import re

host = 'http://192.168.1.57'
# 批量解析
def single_parse():
    url = host+'/apis/pdf2html/'

    dir_path = r'D:\上传文件\pdf比对\1专业数据\数据组--公告'
    files = os.listdir(dir_path)
    print(files)
    for i in files:
        if os.path.splitext(i)[1]=='.pdf' or os.path.splitext(i)[1]=='.PDF':
            file_url=os.path.join(dir_path,i)
            datas = {"filename": i, "url": ""}
            file = {'file':open(file_url,'rb')}
            res = requests.post(url=url,data=datas,files = file)
            print(res.text)

# PDF解析单个
def single_two():
    url = host+'/apis/pdf2html/'

    # dir_path = r'D:\上传文件\pdf比对\1专业数据\识别结果问题数据\公告\f2783c17-7b3a-4940-b779-bdd984fb7dea.PDF' # 失败文件
    dir_path = r'D:\上传文件\pdf比对\1专业数据\数据组--公告\SAAS供应链管理软件(1).pdf'
    name = os.path.split(dir_path)[1]
    file_url = dir_path
    datas = {"filename": name, "url": ""}
    print(name)
    datas = {"filename": name}
    file = {'file': open(dir_path, 'rb')}
    print(time.strftime('%y-%m-%d_%H_%M_%S',time.localtime(time.time())))
    res = requests.post(url=url, data=datas, files=file)
    print(res.text)

# 上传图片
def upload_image():
    url = host+'/upload/'
    filepath = r'C:\Users\fir\Pictures\QQ浏览器截图\QQ浏览器截图20200708152743.png'
    # filepath = r'C:\Users\fir\Pictures\QQ浏览器截图\QQ浏览器截图20200709095451.png'
    file = {'file':open(filepath,'rb')}
    res = requests.post(url=url,files=file)
    print(res.text)
    print(host+'/show/?id='+re.findall('"id":"(.*?)"',res.text)[0])

if __name__=="__main__":
    single_parse()
    # single_two()
    # upload_image()








