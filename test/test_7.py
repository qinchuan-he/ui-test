#coding=utf-8

import requests
import json


# 检查线上公告和研报是否有索引,输出返回索引为空的


# 检查公告

cookie = {'fir_session_id':'bqgi8tsr6n6jwm095pixmi5zubc33853'}

def check_notice():
    # for i in range(1,21):
    #     print(i)
    for j in range(1,9):
        url = 'https://cyprex.fir.ai/api/resource/publicSearch/?url=%2Fresource%2FpublicSearch%2F&search_keywords=&' \
              'table_code=004&info_type=02&ordering=score&search_level=1&start_time=&end_time=&page_row=20' \
              '&page='+str(j)+'&author_list=%5B%5D&is_correct=true'
        res = requests.get(url=url,cookies=cookie)
        result = json.loads(res.text).get('data').get('results')[0].get('data_list')
        for i in result:
            if len(i.get('content'))==0:
                print('{},{}'.format(i.get('file_id'),i.get('content')))

# 检查研报
def check_report():
    for j in range(1,5):
        url ='https://cyprex.fir.ai/api/resource/publicSearch/?url=%2Fresource%2FpublicSearch%2F&search_keywords=' \
             '%E5%85%AC%E5%8F%B8&table_code=005&info_type=03&sub_info_type=0302&sub_info_type=0300&search_level=1' \
             '&ordering=score&start_time=&end_time=&page_row=20&page='+str(j)+'&author_list=%5B%5D&is_correct=true'
        res = requests.get(url=url, cookies=cookie)
        result = json.loads(res.text).get('data').get('results')[0].get('data_list')
        for i in result:
            if len(i.get('content')) == 0:
                print('{},{}'.format(i.get('file_id'), i.get('content')))

if __name__=='__main__':
    check_notice()
    check_report()

