

import openpyxl
from openpyxl.styles import PatternFill
from common.comfunction import *
from time import sleep




#增加关键字驱动模块
# 1.读取Excel（xlsx格式），进行轮询取出每一行
# 2.每一行根据关键字执行

def open():
    """ test Excel执行"""
    # wb = openpyxl.load_workbook('D:\\work\\1测试\\7设计\\关键字对照表.xlsx')
    file = 'D:\\work\\1测试\\2用例\\cypress系统\\回归用例\\私有文件用例.xlsx'
    exec_path = os.path.join(os.path.dirname(file),'执行结果')
    if not os.path.exists(exec_path):
        os.mkdir(exec_path)
    file_path = os.path.abspath(file)
    file_split = os.path.splitext(os.path.basename(file_path))
    wb = openpyxl.load_workbook(os.path.abspath(file_path))
    sheet = wb.worksheets
    all = []
    for i in sheet:
        j = i.max_row
        k = i.max_column
        # 清除执行时间和执行结果
        # if i != sheet[2]:
        #     continue
        for q in range(2,j+2):
            i.cell(q,7).value=''
        for row in range(2,j+1):
            rows = []
            column_s=''
            for column in range(1,k+1):
                cell = i.cell(row,column).value
                column_s = column
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
                i.cell(row, column_s-1).value = time.strftime('%Y_%m_%d %H:%M:%S',time.localtime(time.time()))
                fill_color = PatternFill(fgColor='1E90FF',fill_type='solid')
                i.cell(row,column_s).value = '通过'
                i.cell(row, column_s).fill = fill_color
            except Exception as e:
                print('执行出错，终止')
                i.cell(row, column_s - 1).value = time.strftime('%Y_%m_%d %H:%M:%S', time.localtime(time.time()))
                i.cell(row,column_s).value = '失败'
                fill_color = PatternFill(fgColor='FF3E96',fill_type='solid')
                i.cell(row, column_s).fill = fill_color
                print(e)
                CloseBrowsers() # 执行出错，终止并关闭浏览器
                break
    print(all)
    print('执行完毕')
    date = time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
    wb.save(os.path.join(exec_path,file_split[0]+'_执行_'+date+file_split[1]))




if __name__=='__main__':
    open()
































