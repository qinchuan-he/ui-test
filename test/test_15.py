

import requests



def add_mark():
    r_url = "https://testapp.fir.ai/api/resource/update/active_file/"
    cookie = {'fir_session_id':'dlmzigrc88lau1p72i67u04ychyxmojy'}
    file_path = r'D:\2\1870id.txt'
    file = open(file_path,'r')
    # print(file.readlines())
    for i in file.readlines():
        print(i)
        part = {'active_status':1,'oid':i}
        result = requests.post(url=r_url,data=part,cookies=cookie)
        print(result.text)
        # return

    print("test")



if __name__=="__main__":
    add_mark()










