# coding=utf-8

import os
import time
import math
import operator
from functools import reduce
from time import sleep
from PIL import Image
from PIL import ImageChops
from PIL.PngImagePlugin import PngImageFile
from common.comfunction import User,OpenBrowser,com_path,url31,url32
from buttonFunction.function_contractrelated import contract_Proofreading
from common.comfunction import com_operation
from buttonFunction.function_checkcontract import check_proofreading
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


mode = 2
driver = OpenBrowser(mode)
User().login(driver,"10034345659")
User().switch_navigation(driver, name="智能比对")
sleep(1)
# driver.find_element_by_xpath("//span[text()='查看明细']").click()
driver.find_element_by_xpath("//div[contains(text(),'今天')]/..//span[text()='查看明细']").click()
WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, "//div[text()='文本比对']")))
sleep(1)

com_operation().com_close_preview(driver)



# for i in range(36):
#     els = driver.find_elements_by_xpath("//div[@class='ant-row']/div[3]")
#     picture_url = os.path.join(com_path(),"样本","智能审核样本.png")
#     print(len(els))
#     print(els[1])
#     content = els[1].text
#     print(content)
#     if content=="要素快照风险报告":
#         print("审核成功")
#         break
#     elif content=="审校失败再次审校":
#         print("审核失败")
#         break
#     elif i==35:
#         print("审核超时")
#         break
#     else:
#         sleep(10)
# picture_url2 = os.path.join(com_path(),"截图","智能审核截图.png")
# driver.get_screenshot_as_file(picture_url2)
#
# image1 = Image.open(picture_url) #type:PngImageFile
# image2 = Image.open(picture_url2) # type:PngImageFile
# img1 = image1.convert("RGB")
# img2 = image2.convert("RGB")
# diff = ImageChops.difference(img1,img2)
# img_1 = image1.histogram()
# img_2 = image2.histogram()
# diff_sqrt = math.sqrt(reduce(operator.add,list(map(lambda x,y:(x-y)**2,img_1,img_2))))
# print(diff_sqrt)
# if diff.getbbox() != None:
#     if diff_sqrt>38:
#         result_url = os.path.join(com_path(),"截图","不一样.png")
#         diff.save(result_url)
#
# sleep(2)

# check_proofreading(driver,is_check="2")
driver.quit()


