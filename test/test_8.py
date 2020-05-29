

import openpyxl
from openpyxl.styles import PatternFill
from common.comfunction import *
from time import sleep
from test.keyword_report import createReportHtml




#增加关键字驱动模块
# 1.读取Excel（xlsx格式），进行轮询取出每一行
# 2.每一行根据关键字执行

def open():
    """ test Excel执行"""
    # wb = openpyxl.load_workbook('D:\\work\\1测试\\7设计\\关键字对照表.xlsx')
    file = 'D:\\work\\1测试\\2用例\\cypress系统\\回归用例\\私有文件_上传验证_用例.xlsx'
    exec_path = os.path.join(os.path.dirname(file),'执行结果')
    report_path = os.path.join(os.path.dirname(file),'执行结果'+time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))+'report.html')
    if not os.path.exists(exec_path):
        os.mkdir(exec_path)
    file_path = os.path.abspath(file)
    file_split = os.path.splitext(os.path.basename(file_path))
    wb = openpyxl.load_workbook(os.path.abspath(file_path))
    sheet = wb.worksheets
    all = []
    result = [] # 存放执行结果
    for i in sheet:
        print(i.title)





if __name__=='__main__':
    open()
































