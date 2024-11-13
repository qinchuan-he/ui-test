# coding = utf-8

import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0, rootPath)

# 下午5点执行的定时任务
from test.check_mysql import check_notice

if __name__=='__main__':
    check_notice()






