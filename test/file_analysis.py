# coding=utf-8

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
from time import sleep

from common.comfunction import User
from test.upload_relate import folder_analysis
from common.comfunction import up_analysis
from common.comfunction import get_urlname
from common.comfunction import highlight
from common.private import DB
import pymysql


class check_analysis:
    """ 检查pdf和word解析结果的"""
    def analysis_PDF(self,driver,image_path=None,image_prefix=None):
        """ 检查PDF后缀的文件的解析"""
        # 进入私有根目录
        User().root_private(driver)
        el1 = driver.find_element_by_xpath("//span[contains(text(),'"+folder_analysis+"')]/..")
        el1[0].click()
        file_name = get_urlname(up_analysis[0])
        driver.find_element_by_xpath("//span[text()='"+file_name+"']").click()
        sleep(0.5)
        WebDriverWait(driver, 5, 0.5).until(ec.presence_of_element_located((By.XPATH,"//iframe")))
        el2 = driver.find_element_by_xpath("//span[text()='内容搜索']/..")
        highlight(driver,el2)
        if image_path:
            driver.get_screenshot_as_file(image_path+image_prefix+"-内容搜索按钮"+".png")
        el2.click()

# 统计pdf精读一页的解析时间,目前连接线上数据库
def average_services():

    # datastorage数据库
    data_host = DB().host
    data_port = int(DB().port)
    data_name = DB().db_storage
    db_user = DB().user
    db_pwd = DB().pwd
    # cyprex数据库
    cyprex_name = DB().db_cyprex

    sql_1 = "select  file_id,cost  from jobs_extractjob  where created>'2020-12-08' and extract_code='to_html' and status='succeed'"
    conn_data = pymysql.connect(host=data_host, port=data_port, database=data_name, user=db_user, password=db_pwd,
                                charset='utf8')
    cus_data = conn_data.cursor()
    conn_cyprex = pymysql.Connect(host=data_host, port=data_port, database=cyprex_name, user=db_user, password=db_pwd,
                                  charset='utf8')
    cus_cyprex = conn_cyprex.cursor()

    try :
        cus_data.execute(sql_1)
        cost_time=0   # 总耗时，秒
        total_page=0  # 总页数
        file_list=[]
        for i in cus_data.fetchall():
            cost_time+=i[1]
            file_list.append(i[0])
        # print(cost_time)
        file_list=tuple(file_list)
        # print(file_list)
        sql_2 = "select id,total_page,`name` from resources_resource where id in(select resource_id from " \
                "resources_resourcedatads where fileId in {}) ".format(file_list)
        cus_cyprex.execute(sql_2)
        # print(cus_cyprex.fetchall())
        for j in cus_cyprex.fetchall():

            if j[1]==None:
                print('{}。未提取到页数,id为：{}'.format(j[2],j[0]))
            else:
                total_page+=j[1]
        # print(total_page)
        print(cost_time,total_page)
        print('平均一页pdf转换耗时：%.2f 秒' % (cost_time/total_page))

    except Exception as e:
        print(e)




if __name__=='__main__':
    print('--')
    average_services()








