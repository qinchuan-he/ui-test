# coding:utf-8
import os
import webbrowser
from typing import List

# 2020-05-20 关键字驱动生成结果的html
def createReportHtml(url:str,result:List):
    path = os.path.join(url)
    file = open(path, 'w+')
    part_start = """
    <html>
    <head>
        <h1>测试报告</h1>
    </head>
    <body>
    """
    part_end = """

                </table>
            </div>
        </body>

    </html>
    """

    part_2 = ''
    num = 1
    success_num = 0
    for i in result:
        # 设置
        if i[1]=='执行成功':
            success_num+=1
            color = 'style="color:#14892c"'
        else:
            color = 'style="color:#FF0000"'
        part_2_1 = """
            <tr >
                        <td> %s </td><td>%s </td><td  %s> %s </td><td> %s </td><td> %s </td><td> %s </td> <td> %s </td>
                    </tr>
        """ % (num, i[0], color, i[1], '详情' if i[1]=='执行成功' else i[4], i[2], i[3], '无' if i[1]=='执行成功'
        else '<a href='+i[5]+'>查看</a>')
        num += 1
        part_2 = part_2 + part_2_1


    part_1 = """
            <div>
                <span>测试结果：</span>
                <span style="color:#14892c"> 通过：%s ,</span>
                <span style="color:#FF0000"> 失败：%s ，</span>
                <span> 总计：%s 条用例</span>
            </div>
            <div>
                <table id="result" border="1" >
                    <tr>
                        <td width="50px">序号</td><td width="80px">用例名称</td><td width="80px">执行结果</td><td>详情</td>
                        <td width="170px">执行开始时间</td><td width="170px">执行结束时间</td><td width="50px">截图</td>
                    </tr>

    """%(success_num,len(result)-success_num,len(result))

    content = part_start+part_1 + part_2 + part_end
    file.write(content)
    file.close()

    webbrowser.open(path, new=1)





if __name__ == "__main__":
    url = "D:\\work\\1测试\\2用例\\cypress系统\\回归用例\\test.html"
    result = [['上传所有种类格式', '执行成功', '2020-05-20 15:02:15', '2020-05-20 15:02:25'], ['删除上传文件夹', '执行失败', '2020-05-20 15:02:25', '2020-05-20 15:02:41']]
    result = [['上传所有种类格式', '执行失败', '2020-05-20 16:23:26', '2020-05-20 16:23:41', 'element click intercepted: Element <span title="..." class="FileList_fileNameWrap__30lES">私有上传</span> is not clickable at point (138, 345). Other element would receive the click: <div tabindex="-1" class="ant-modal-wrap " role="dialog">...</div>\n  (Session info: headless chrome=79.0.3945.88)'], ['删除上传文件夹', '执行成功', '2020-05-20 16:23:41', '2020-05-20 16:23:59']]

    createReportHtml(url,result)




