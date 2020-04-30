

import openpyxl
from common.comfunction import *
from time import sleep




#增加关键字驱动模块
# 1.读取Excel（xlsx格式），进行轮询取出每一行
# 2.每一行根据关键字执行

def open():
    """ test Excel执行"""
    wb = openpyxl.load_workbook('D:\\work\\1测试\\7设计\\关键字对照表.xlsx')
    sheet = wb.worksheets

    # for  i in sheet:
    i = sheet[1]
    j = i.max_row
    k = i.max_column
    all = []
    for row in range(2,j+1):
        rows = []
        for cloumn in range(1,k+1):
            cell = i.cell(row,cloumn).value
            rows.append(cell)
        if rows[2] and rows[3] and rows[4]:
            s = str(rows[2])+'('+'"'+str(rows[3])+'"'+','+'"'+str(rows[4])+'"'+')'
        elif rows[2] and rows[3]:
            s = str(rows[2])+'('+'"'+str(rows[3])+'"'+')'
        elif rows[2] and rows[4]:
            s = str(rows[2])+'('+str(rows[4])+')'
        elif rows[2]:
            s = str(rows[2])+'('+')'
        else:
            s = ''
        print(s)
        all.append(s)
        try:
            eval(s)
        except Exception as e:
            print('执行出错，终止')
            print(e)
            break
    print(all)

        # print(i.cell(2,2).value)





if __name__=='__main__':
    open()
































