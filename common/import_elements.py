import xlrd

# 取值列表转字典
# def import_elements(sheetname):
#     path = "C:\\Users\mengl\PycharmProjects\pythonProject\data\page_elements.xls"
#     data = xlrd.open_workbook(path)
#     value = data.sheet_by_name(sheetname)
#     list = []
#     for rows in range(int(value.nrows)):
#         if rows==0:
#             continue
#         list.append(value.cell_value(rows,3))
#     dict = {}
#     for i in range(len(list)):
#         dict[i]=list[i]
#     return(dict)

def import_elements(sheetname):
    path = "C:\\Users\mengl\PycharmProjects\pythonProject\data\page_elements.xls"
    data = xlrd.open_workbook(path)
    value = data.sheet_by_name(sheetname)
    dict = {}
    for rows in range(int(value.nrows)):
        if rows == 0:     # 跳过表头
            continue
        dict[rows-1] = value.cell_value(rows,3)
    return dict

