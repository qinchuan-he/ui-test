
# 存放所有被删除的方法

def write_txt():
    s= '{"纯文本控件-0": {"content": "\\哈哈\"哇哈哈"},"纯文本控件-1": {"content": ""}, "纯文本控件-3": {"content": ""}}'
    with open(r'D:\work\1测试\9性能+安全性\数据联动\5.txt','w+',encoding='utf8') as f:
        f.write(s)
    print('----------')

def read_txt():
    s = '{"纯文本控件-0": {"content": "%s"},"纯文本控件-1": {"content": ""}, "纯文本控件-3": {"content": ""}}'
    with open(r'D:\work\1测试\9性能+安全性\数据联动\6.txt', 'r', encoding='utf8') as f:
        line = f.readlines()
        print(line[0])
        return s % line[0]
