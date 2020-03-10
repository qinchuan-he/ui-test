# coding = utf-8

import os
# import time
# from time import sleep
# from common.comfunction import execBrower,User,com_path
# from test.smart_search import search_home,search_result
# from buttonFunction.function_checkcontract import check_proofreading
# from common.comfunction import Image_Processing

# from PIL import Image
# from PIL import ImageChops
# import xlrd
# import xlwt
import shutil
# import pandas
# import openpyxl
# import openpyxl.cell.cell
import sys
# from robotide import main
# from robotide import run
# print(sys.path)

# 通用解密方法
from hashids import Hashids
text='ZnbexRpp6dRVqwJW'
hash_ids = Hashids(salt='&-yx879yzi99tmum0s(e3+st85_+2g=u$e7cie2n$s_%@h@*k)9', min_length=16)
result = hash_ids.decode(text)

print(result)
print('---------------')






















a1 = (100+1200)*(1.1+1.06)*(50+1)
a2 = (100+1200)*(1.1+1.06)*(50+10)
a3 = (100+1200)*(1.1+1.06)*(50+50)
a4 = (100+1200)*(1.1+1.06)*(50+200)
a5 = (100+1200)*(1.1+1.06)*(50+600)
a6 = (100+1200)*(1.1+1.06)*(50+1500)
a7 = (100+1200)*(1.1+1.06)*(50+3000)
a_6 = (100+2000+2434)*(1.1+1.07+1.5)*(50+1500)/10000
a_7 = (100+2000+2434)*(1.1+1.07+1.5)*(50+3000)/10000

a_x = (100+4500+15624)*(1.1+3.4+2.9)*(50+56000)/10000/10000
a_x1 = (100+4500+10021)*(1.1+3.4+2.6)*(50+72000)/10000/10000
a_y = (100+4500+15624)*(1.1+3.4+2.9)*(50+72000)/10000/10000
a_y1 = (100+4500+15624)*(1.1+3.4+2.9)*(50+88000)/10000/10000
print(a_y-a_x)
print(a_y1-a_y)

print(int(a_6))

print(int(a_7))


a_list1 = [a1,a2,a3,a4,a5,a6,a7]
a_list = []
for i in range(7):
    a_list.append('%.2f'%(a_list1[i]/10000))
for i in a_list1:
    print("%.2f" %(i/10000))

for i in range(len(a_list)):
    if i<len(a_list)-1:
        s1 = float(a_list[i])
        s2 = float(a_list[i+1])
        print('第%d级别和第%d级别倍数差距：%.2f'%(i+2,i+1,s2/s1))
print('-----------------------')
for i in range(len(a_list)):
    s1 = float(a_list[i])
    s2 = float(a_list[-1])
    print('第%d级别和第%d级别倍数差距：%.2f' % (7, i + 1, s2 / s1))

print(140*36)

# fp="D:\\121.xlsx"
#
# shutil.copyfile(fp,"D:\\1212.xlsx")

# f = pandas.read_excel(fp,sheet_name=0)
# print(f.head())

# ws = openpyxl.load_workbook("D:\\1212.xlsx")
#
# ws2 = ws.active
# s = ws2['A1':'M5'] #type:tuple
#
# print(s[0])
# for i in s:
#     for j in i:
#         print(j.value)
# print(ws.active)
# # ws.active.title = '我重命名的'
# print(ws.active)
# print(ws.active['D3'].value)
# # print(ws.sheetnames)
# sleep(100)
# sheet = ws['Sheet1']
# num = 3
# posi = 'D'
# position = posi+str(num)
# s = sheet[position] #type:openpyxl.cell.cell.Cell
# p = s.value
# print(p)
# sheet['D3'] = '哇哈哈'
# print(sheet['D3'].value)
# ws.save("D:\\1212.xlsx")





# wk = xlwt.Workbook()
# ws = wk.add_sheet('test') #type:xlwt.Worksheet
# ws.write(0,0,'你好哇啊哈哈哈哈哈')
# wk.save('D:\\2.xls')
# print(type(ws))
# a = ['1','2','3']
# print(type(a))






# fp = xlrd.open_workbook('D:\\121.xlsx')
# # fp2 = xlrd.count_records('D:\\121.xlsx')
# # fp = open("D:\\1.txt")
#
# print(fp.sheet_by_index(0).row_values(1,1,5))
# print("---")
# # print(fp.read())















