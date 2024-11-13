#coding=utf-8




# 统计用户行为，

from common.private import DB
from test.check_day import EveryDayMethod
import datetime
from common.private import DB,ServerInfo

#
def conn_linux_list():

    # print(EveryDayMethod.)
    print(ServerInfo.host)




def download_count():
    file_download_count = 0  # 统计下载文件次数
    annotation_download_count = 0  # 统计下载文件次数
    d = datetime.timedelta(days=-1)
    count_day = (datetime.datetime.now()+d).strftime('%Y-%m-%d')
    # 统计语句，进入服务器对应路径
    log_url = 'cd /data/srcpd/cyprex/cyprex/log/cyprex'
    # 下载文件次数
    file_download_shell = "cat cyprex.log.{} | grep '/resource/download/' | wc -l".format(count_day)
    #下载摘录笔记次数
    annotation_download_shell = "cat cyprex.log.{} | grep '/annotation/download/'  | wc -l".format(count_day)
    shell_all = [log_url,file_download_shell,annotation_download_shell]
    doi = EveryDayMethod()
    result = doi.conn_linux(shell_all)
    file_download_count = result[0]
    annotation_download_count = result[1]
    print('----------------统计日期：',count_day,'--------------')
    print(int(file_download_count/2),int(annotation_download_count/2))




if __name__ == "__main__":
    download_count()
    # conn_linux_list()











