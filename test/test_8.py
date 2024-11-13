#coding=utf-8
import requests
import datetime
from time  import sleep

#八皇后问题
def queen(A, cur=0):
    print(cur)
    print(A)
    if cur == len(A):
        print(A)
        return 0
    for col in range(len(A)):  # 遍历当前行的所有位置
        A[cur] = col
        for row in range(cur):  # 检查当前位置是否相克
            # print('col 当前行皇后的位置（列）:',col)
            # print('A[row] 前面行皇后的位置（列）: ', A[row])
            # print('cur 当前行号 ', cur)
            # print('row 前面行号', row)
            if A[row] == col or abs(col - A[row]) == cur - row:
                break
            # print('校验通过')
            # print(A)
        else:  # 如果完成了整个遍历，则说明位置没有相克
            # print('-----------------------------------------------')
            # print(cur)
            queen(A, cur+1)  # 计算下一行的位置

def abc():
    abb()
    print('-------------')

def abb():
    return False

def baidu():
    file = r'D:\work\11运维\网络服务\log.txt'
    url = "https://www.baidu.com/s?wd=ip&rsv_spt=1&rsv_iqid=0xc259f8fd00039e72&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=02049043_33_pg&rsv_enter=1&rsv_dl=tb&oq=ip&rsv_btype=t&inputT=500&rsv_t=5c46kq7Lyy7sEapogyul3VrL9WlC7HN%2FyfmeguANU9%2FNi8VyBpV%2Bj9xyHK5CYAeB7HMpIJY&rsv_pq=82cc47b4000156be&rsv_sug3=7&rsv_sug1=8&rsv_sug7=100&rsv_sug2=0&rsv_sug4=500"
    while str(datetime.datetime.now())[:19 ]<'2021-07-14 10:17:48':
        rd = open(file, 'a+', encoding='utf-8')
        try:
            t1 = datetime.datetime.now()
            res = requests.get(url=url)
            t2 = datetime.datetime.now().timestamp()
            # rd = open(file, 'a+', encoding='utf-8')
            # rd.write('\n')
            rd.write('请求时间=' + str(t1))
            # rd.write('\n')
            rd.write('=耗时=' + str(t2 - t1.timestamp()))
            rd.write('\n')
            print('请求时间:', t1)
            print(':耗时:', t2 - t1.timestamp())

        except:
            rd.write('报错了，忽略')
            rd.write('\n')
            print('报错了，忽略')
        rd.close()

        sleep(20)

def accc():
    cookie = {"fir_session_id":"0ieoyck5buysagx75ygw6eeo27jm9trn"}
    url = 'https://testapp.fir.ai/api/resource/search/?search_keywords=&search_type=001&start_time=&end_time=&is_correct=true&table_code=001&only_associate=0&pid=-1&ordering=score'

    result = requests.get(url=url,cookies=cookie)
    print(result.text)





if __name__=="__main__":
    # queen([None]*4)
    # abc()
    # baidu()
    accc()