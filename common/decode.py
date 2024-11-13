# coding = utf-8


import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)
from hashids import Hashids
from common.private import InterBaseUrl
from Crypto.Cipher import AES


# 通用解密方法
def cyprex_decode(code):
    code = str(code)
    hash_ids = Hashids(salt=InterBaseUrl().Decode_Key, min_length=16)
    result = hash_ids.decode(code)
    return result[0]

# 通用加密方法
def encrypt_id(oid):
    """通用id加密方法"""
    if not oid:
        return oid
    hash_ids = Hashids(salt=InterBaseUrl().Decode_Key, min_length=16)
    print("------------")
    return hash_ids.encode(oid)

# 文件级别解密
# def aes_decrypt(crypto, key=constant.AES_KEY, iv=constant.AES_IV):
def aes_decrypt(crypto):
    """AES CBC PKCS7 解密"""
    key='NJY1ODG1MDU0MZMW'
    iv='ODI5MJGZNZCWMDE5'
    path = r'C:\Users\qy\Downloads\orginal.doc'
    file = open(path,'r',encoding='utf-8')
    crypto1=file.readlines()
    # print(crypto1)
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    block = aes.decrypt(crypto1)
    unpad = lambda s: s[0:-ord(s[-1:])]  # 去除PKCS7填充物
    print(unpad(block))
    return unpad(block)



if __name__=='__main__':
    text = 'WkaXG1QlNOxRNdEw'
    id = 4646374
    print(cyprex_decode(text))
    print(encrypt_id(id))







