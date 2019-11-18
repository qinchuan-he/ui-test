# coding=utf-8
# 统计平均时间
path = "D://loadingReport//"
switch_path = "D://loadingReport//switch//"
filename=['图例验证文件','146页年度报告','282页','336页','496页','625页']


# for name in filename:
#     f = open(path+name+".txt",'r')
#     count = 0
#     sum =0
#     avg = 0
#     for i in f.readlines():
#         s =i.split('\n')
#         if len(s[0])>0:
#             count+=1
#             sum += float(s[0])
#     f.close()
#     print("%.2f"%(sum/count))



for i in filename:
    f = open(path+i+".txt")
    a_list = f.readlines()
    b_list = [x.replace("\n","") for x in a_list]
    b_list = [x for x in b_list if x != '']
    sum = 0
    num = len(b_list)
    for x  in b_list:
        sum += float(x)
    # print(sum)
    # print(num)
    avg = sum / num
    print("%.2f"%avg)
    f.close()


# D://loadingReport//282页.txt











