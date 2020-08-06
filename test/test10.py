
import requests
import os
import threading
import time

def dd(file_url=None):
    if not file_url:
        file_url = r'D:\上传文件\pdf比对\投标样本\华尔街\公告\天齐锂业股东大会决议.PDF'
    file_name = os.path.split(file_url)[1]
    url = 'http://124.77.120.212:10151/v2/files/databox/第一个文件夹/'+file_name+'?X-LENOVO-SESS-ID=e84htk5ps920sa8g7jtv49i5d5&S=D03F2ADD&uid=27&overwrite=true&source=file&language=zh&t=&path_type=ent&1593506087757'
    # cookie = {'X-LENOVO-SESS-ID':'e84htk5ps920sa8g7jtv49i5d5'}
    url_2 = 'http://124.77.120.212:10151/v2/files/databox/第二个文件夹/'+file_name+'?X-LENOVO-SESS-ID=e84htk5ps920sa8g7jtv49i5d5&S=D03F2ADD&uid=27&overwrite=true&source=file&language=zh&t=&path_type=ent&1593506087757'
    url_3 = 'http://124.77.120.212:10151/v2/files/databox/第三个文件夹/'+file_name+'?X-LENOVO-SESS-ID=e84htk5ps920sa8g7jtv49i5d5&S=D03F2ADD&uid=27&overwrite=true&source=file&language=zh&t=&path_type=ent&1593506087757'

    file = {'file':open(file_url,'rb')}
    file_2 = {'file': open(file_url, 'rb')}
    file_3 = {'file': open(file_url, 'rb')}
    try:
        res = requests.post(url=url,files = file)
        res_2 = requests.post(url=url_2, files=file_2)
        res_3 = requests.post(url=url_3, files=file_3)
        print(res.text)
        print(res_2.text)
        print(res_3.text)
    except Exception as e:
        print(e)

class Mythread(threading.Thread):

    def __init__(self,file_url):
        threading.Thread.__init__(self)
        self.file_url = file_url
    def run(self) -> None:
        dd(self.file_url)



if __name__=="__main__":
    dd()

