import datetime
import json
import time


import requests
import pymysql
from pymysql.constants import CLIENT
from common.private import DB,ServerInfo,EmailProperty



def add_annotation():
    url = "https://testapp.fir.ai/api/resource/annotation/add/"
    cookie = {"fir_session_id":"1asf8rTIFKoSxcetRlVLMC5X7GkiguWE"}
    context = "Most patients are diagnosed with organ-confined prostate cancer, which can potentially be cured through locoregional therapies, such as surgery (radical prostatectomy), radiotherapy, and/or brachytherapy (19). However, approximately 30% of these patients experience a biochemical recurrence (BCR)a rise in prostate-specific antigen (PSA) serum levels—indicating prostate cancer relapse (20). At this stage of the disease, suppression of androgen production is a commonly applied therapeutic intervention that can delay further cancer progression for years (21, 22). Nevertheless, the development of resistance to androgen deprivation is inevitable, resulting in castration-resistant prostate cancer (CRPC) for which there is no cure (23). Most CRPC tumors acquire molecular features that enable active AR signaling despite low circulating androgen levels, a finding that led to the development of several highly effective AR-targeted therapies. Enzalutamide (ENZ) is one of the most frequently used AR-targeting agents, which functions through a combined mechanism of blocked AR nuclear import, diminished AR chromatin binding, and decreased transcription complex formation, effectively impairing AR-driven prostate cancer growth (24). ENZ’s potent antitumor activity has been demonstrated in multiple clinical trials, which led to its FDA approval in various prostate cancer disease stages—from metastatic CRPC (mCRPC; refs. 25, 26) to metastatic hormone-sensitive prostate cancer (mHSPC; ref. 27) and even nonmetastatic CRPC (28)—illustrating how ARtargeted therapies are being progressively introduced earlier in clinical practice. A clinical benefit of ENZ monotherapy as a neoadjuvant treatment prior to prostatectomy for patients with localized disease has not been established. Although effective in the CRPC setting, resistance to AR pathway inhibition will ultimately develop, and the management of advanced prostate cancer with this acquired resistance remains a major clinical challenge, especially since the underlying mechanisms are still not fully elucidated (29). Therefore, furthering our understanding of how ENZ affects prostate cancer biology may lead to the identification of acquired cellular vulnerabilities that could be therapeutically exploited."
    datas ={"oid":"eB0oA80aG9LRlGE7","content":context,"origin_page":1,"source_info":"{\"bgColor\":\"#EEF4FF\"}","is_excerpt_ocr":0}
    # result = requests.post(url=url,data=datas,cookies=cookie)
    # print(result.text)
    path = r'D:\2\13.txt'
    file = open(path,'rb')
    for i in file.readlines():
        rows = str(i,'utf-8')
        datas ={"oid":"eB0oA80aG9LRlGE7","content":rows,"origin_page":1,"source_info":"{\"bgColor\":\"#EEF4FF\"}","is_excerpt_ocr":0}
        result = requests.post(url=url, data=datas, cookies=cookie)
        print(result.text)


def acc():
    al = 3600*24
    # date = time.strftime('%Y-%m-%d',time.localtime(time.time()-al))
    # print(date)
    # sql = "select count(*) from (SELECT userId FROM `account_loginlog` where ctime BETWEEN '2022-09-01' and '2022-09-02' and source_type='3003' GROUP BY userId) as count_user"
    sql_list2 = []
    for i in range(28):
        date_old = time.strftime('%Y-%m-%d', time.localtime(time.time() - (i + 1) * al))
        date_new = time.strftime('%Y-%m-%d', time.localtime(time.time() - i * al))
        sql = "select count(*) from (SELECT userId FROM `account_loginlog` where ctime BETWEEN '{}' and '{}' and " \
              "source_type='3003' GROUP BY userId) as count_user".format(date_old, date_new)
        print(date_old)
        sql_list2.append(sql)


# 恢复笔记编辑器数据，传入选定的一行参数
def cut_copntent():
    # 传入参数，cookie，id（加密值），name（带后缀）
    cookie = {'fir_session_id':'1asf8rTIFKoSxcetRlVLMC5X7GkiguWE'}
    r_id = "kX3KGRaB9ap1wpYZ"
    r_name = "实验文件.doc"

    # r_url = 'https://app.fir.ai/api/resource/form/'
    r_url = 'https://testapp.fir.ai/api/resource/form/'
    r_content = ""
    path = r'D:\2\1.txt'
    file = open(path,'rb')
    for i in file.readlines():
        lins = str(i,'utf8')
        # print(lins)
        # 获取搭配content中参数
        content=lins.split('\\"content\\": \\"',2)[1].split('\\", \\"name\\":')[0]
        print(content)
        # 参数去除多余转义符号
        r_content = content.replace('\\\\u','\\u').replace('\\\\"','"')
        print(r_content)
    # r_content = '<p>hello world</p>'
    resource_list = [{"id": r_id, "content": r_content, "name": r_name}]
    print(resource_list)
    print(type(resource_list))
    # data_s = {"resource_list": json.dumps(resource_list)}
    # print(data_s)
    # data_s = {"resource_list": "".join(resource_list)}
    # print(data_s)
    # print(type(data_s))


    # 发送请求
    # result = requests.post(url=r_url,data=data_s,cookies=cookie)
    # print(result.text)



def count_may():
    print("")
    # connection_mysql
    host_name = "192.168.1.214"
    db_name = "cyprex_test7"
    db_port = 3306
    db_user = "kaifa"
    db_pwd = "kaifazufir2018518"
    client_flag = CLIENT.MULTI_STATEMENTS
    conn = pymysql.connect(host=host_name, database=db_name, port=db_port, user=db_user, password=db_pwd)
    cur = conn.cursor()
    sql_list = []
    date_list = []
    for i in range(20):
        # print(i+1)
        # 使用用户数
        sql_use =  "select count(*) FROM(SELECT user_id FROM `main_logentry` where ctime " \
                   "BETWEEN '2022-10-{}'and '2022-10-{}'GROUP BY user_id) as use_sum;".format(i+1,i+2)

        sql_user = "select count(*) from (select id from account_user where ctime BETWEEN" \
                   "'2022-10-{}'and '2022-10-{}'and `status`=1) as users;".format(i+1,i+2)

        cur.execute(sql_use)
        print(cur.fetchall()[0][0])
        # 批量执行日期
        last_date = ["2022-10-{}".format(i+1),"2022-10-{}".format(i+2)]
        date_list.append(last_date)

    sql_user = "select count(*) from (select id from account_user where ctime BETWEEN" \
               "%s and %s and `status`=1) as users;"
    # 批量执行，不行，只输出了最后一条sql的数据
    # cur.executemany(sql_user,date_list)
    # result = cur.fetchall()
    # print(result)
    cur.close()
    conn.close()








if __name__=="__main__":
    # add_annotation()
    # acc()
    # cut_copntent()
    count_may()
