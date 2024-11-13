# coding = utf-8

# 图片比对
import os
from common.comfunction import com_path
from PIL import Image
import math
import operator
from functools import reduce
import time
from time import sleep,gmtime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from common.comfunction import OpenBrowser,User


# mode = 2
# overtime = 1
# driver = OpenBrowser(mode,overtime)
# User().login(driver)
#
# s = "alert('你看到我了吗')"
# img = """           // 首屏图片加载完成
#                             let mytiming = window.performance.timing;
#                             return window.lastImgLoadTime - mytiming.navigationStart ;
#                 """
# DNS = """          // DNS查询耗时
#                     let mytiming = window.performance.timing;
#                     return mytiming.domainLookupEnd - mytiming.domainLookupStart ;
#         """
# http = """let time = window.performance.timing
# return time.connectEnd - time.connectStart
# """
# ds = driver.execute_script(DNS)
# dss = driver.execute_script(http)
# print(ds)
# print(dss)












aler = "alert('test')"


loading1 = """
    let time = window.performance.timing
    return time.loadEventEnd -time.navigationStart
"""
loading2 = """
    let time = window.performance.timing
    return time.domContentLoadedEventEnd -time.navigationStart
"""
loading3 = """
    let time = window.performance.timing
    return time.responseStart -time.navigationStart
"""

loading4 = """
    let time = window.performance.timing
    return time.navigationStart
"""
loading5 = """
    let time = window.performance.timing
    return time.loadEventEnd
"""

load_iframe = """
        let iframe = arguments[0];
        let date_1 = new Date().getTime();
    iframe.onload
        
        let date_2 =new Date().getTime()
        return date_2-date_1
        return 'D'
"""
load_iframe2 = """
    
    return new Date().getTime()
    return 'C';
    return 'E';
"""



mode = 2
overtime = 1
driver = OpenBrowser(mode,overtime)
User().login(driver)
driver.find_element_by_xpath("//span[text()='146页年度报告']/..").click()
# driver.get("https://testjianyuan.fir.ai/apps/editor/openPreview/?callURL=aHR0cDovLzE5Mi4xNjguMS4yMjQ6ODA0MS9vZmZpY2Uv"
#            "Y2FsbEJhY2svP29pZD03NTM1OSZmaWxlX2lkPTAzNDcxYjBmLTBiMGUtNDcyNy04NjhjLTQ3OTBlOTIwNTRhYSZ1c2VyX2lkPTM3NSZmX"
#            "3VybD1odHRwczovL3Rlc3RjeXByZXhzdmMuZmlyLmFpL21lZGlhL3RlbXBfZmlsZS8yMDIwLTAxLTE3LzE1NzkyNDAwMjUyMDgwMi5kb"
#            "2N4Jm9wZW5fdHlwZT1vcGVuUHJldmlldyZyZXN0cmFpbj0mZGVmaW5lX3JpYmJvbj0x&sign=6885d608ec3e08bafd1966c4b4dd8f37")
# driver.execute_script(aler)



print("开始计时")
start = time.time()
print(start)
print(time.strftime("%Y-%m-%d %H:%M:%S +0000"))
WebDriverWait(driver,5,0.1).until(ec.presence_of_element_located((By.XPATH,"//iframe")))
print("第一步完毕")
print(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S +0000"))

test2 = """
var div = document.createElement("script");
div.innerHTML = 'window.onload=function(){alert("哈哈哈")}'
document.body.insertBefore(div, document.body.lastElementChild);
"""
driver.execute_script(test2)

driver.find_element_by_xpath("//span[text()='内容搜索']/..").click()
start = time.time()
sleep(0.8)
el = driver.find_element_by_xpath("//iframe")
# driver.execute_script("arguments[0].onload=alert('加载完成');",el)


# el2 = driver.find_element_by_xpath("//h1[@id='qy']")
# driver.execute_script("arguments[0].onload=alert('加载完成');",el2)
# document.body.insertBefore(div, document.body.firstElementChild);

# test2 = """
# var div = document.createElement("script");
# div.innerHTML = 'window.onload=function(){alert("哈哈哈")}'
# document.body.insertBefore(div, document.body.lastElementChild);
# """
# driver.execute_script(test2)

print(el.get_attribute("src"))

driver.get(el.get_attribute("src"))

test = """
var div = document.createElement("div");
div.innerHTML = '<h1 id="qy">哇哈哈</h1>';
div.style.textAlign="center";
document.body.insertBefore(div, document.body.lastElementChild);
"""
# driver.execute_script(test)




# frame = driver.find_element_by_xpath("//iframe")
# driver.switch_to.frame(frame)
# for i in range(100):
#     try:
#         el = driver.find_element_by_xpath("//span[@id='total_page']")
#         print(el.text)
#         if el.text=="146":
#             print(time.time()-start)
#             print("加载完毕")
#             break
#     except Exception as e:
#         # print(e)
#         sleep(0.1)



# sleep(3)
# p=1
# for i in range(100):
#     try:
#         print(i)
#         if p==1:
#             el = driver.find_element_by_xpath("//iframe")
#             driver.switch_to.frame(el)
#             print("切换完成")
#             p = 2
#         driver.find_element_by_xpath("//canvas[@id='id_target_cursor']")
#         print("加载完毕")
#         end = time.time()
#         print(end)
#         print(time.strftime("%Y-%m-%d %H:%M:%S +0000"))
#         print("统计耗时： %s 秒" % str(end-start))
#         break
#     except Exception as e:
#         print(e)
#         sleep(0.1)























# def image_contrast(img1, img2):
#
#     image1 = Image.open(img1)
#     image2 = Image.open(img2)
#
#     h1 = image1.histogram()
#     print(h1)
#     h2 = image2.histogram()
#     print(h2)
#     result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
#     return result
#
# def add(a,b):
#     return a+b
#
# if __name__ == '__main__':
#     root = "C:\\Users\\fir\\Pictures\\QQ浏览器截图\\"
#     picture_url = os.path.join(com_path(), "样本", "智能审核样本.png")
#     picture_url2 = os.path.join(com_path(), "截图", "智能审核截图.png")
#     picture1 = root+"QQ浏览器截图20200113105954.png"
#     picture2 = root+"QQ浏览器截图20200113105958.png"
#     img1 = "./1.png"  # 指定图片路径
#     img2 = "./2.png"
#     result = image_contrast(picture_url,picture_url2)
#     print(result)





