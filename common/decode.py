# coding = utf-8


import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)
from hashids import Hashids
from common.private import InterBaseUrl


# 通用解密方法
def cyprex_decode(code):
    code = str(code)
    hash_ids = Hashids(salt=InterBaseUrl().Decode_Key, min_length=16)
    result = hash_ids.decode(code)
    return result[0]

if __name__=='__main__':
    text = 'vmqkj8j4l71rbZNB'
    print(cyprex_decode(text))






