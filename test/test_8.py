

from common.comfunction import send_mail
import os
from common.comfunction import OpenBrowser
from time import sleep
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from common.private import EmailProperty,folder_path


# sendemail

def sendemail1():
    """ send email test"""
    file_url = r'D:\work\1测试\6接口\3服务器检查脚本\report\index.html'
    image_path = r'D:\上传文件\pdf比对\1专业数据\新建文件夹'
    image_path = os.path.join(image_path)
    email_subject = 'test email'
    url = 'http://192.168.1.223:8077/jmeter/report2/index.html'
    url = 'D:/work/1测试/6接口/3服务器检查脚本/report2/index.html'
    # send_mail()



    # 启动一个浏览器
    driver = OpenBrowser(mode=2)
    driver.get(url)
    sleep(0.5)
    el = driver.find_elements_by_xpath("//div[@style='font-size:8pt;text-align:center;padding:2px;color:white;']")

    # print('准备截图')
    # els = driver.find_elements_by_xpath("//div[@class='panel-body']")
    # for i in range(len(els)):
    #     ActionChains(driver).move_to_element(els[i]).perform()
    #     image = driver.get_screenshot_as_file(image_path + '\\' + str(time.time()) + '.png')
    # print('截图完成')

    el3s = driver.find_elements_by_xpath("//div[@class='tablesorter-header-inner']")
    for i in range(len(el3s)):
        if 'Error' in el3s[i].text:
            if '%' in el3s[i].text:
                ActionChains(driver).move_to_element(el3s[i]).perform()
                ActionChains(driver).double_click(el3s[i]).perform()
                ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()




    print(len(el3s))
    el2s = driver.find_elements_by_xpath("//tr[@role='row']/td[3]")
    # for i in range(len(el2s)):
    #     print(el2s[i].text)
    #     if el2s[i].text !=0:
    #         ActionChains(driver).move_to_element(el2s[i]).perform()





    sleep(1)
    driver.quit()

def yousee():
    image_path = os.path.join(folder_path, '截图', 'jmeter报告')
    print(os.path.exists(image_path))
    if os.path.exists(image_path):
        print(os.listdir(image_path))
        for i in os.listdir(image_path):
            os.remove(os.path.join(image_path,i))
    else:
        os.mkdir(image_path)




if __name__=='__main__':
    # sendemail1()
    yousee()








































