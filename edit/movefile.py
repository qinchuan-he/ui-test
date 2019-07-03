#coding=utf-8
import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#2019-06-18，增加了cookie设置，不需要每次登录
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import time

"""上传word，修改word（未用边写边搜），下载word"""

path="C:\\2services\\driver\\chromedriver.exe"
driver=webdriver.Chrome(path)

driver.implicitly_wait(15)

driver.get("https://testcyprex.fir.ai/sign-in")
driver.find_element_by_xpath("//div[text()='账号登录']").click() 
driver.find_element_by_id("username_no").send_keys("19958966366")
driver.find_element_by_id("password").send_keys("Test123456")
driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div[1]/div[3]/div[2]/form/div[3]/div/div/span").click()   # 登录，好像伪类中的文字不能识别


# 创建文件夹，以当前时间命名
el1=driver.find_element_by_xpath("//span[text()='新建']")
sleep(2)
ActionChains(driver).move_to_element(el1).perform()
driver.find_element_by_xpath("//li[text()='新建文件夹']").click()
folder1=int(time.time())
print(folder1)
driver.switch_to.active_element.send_keys(folder1)
driver.switch_to.active_element.send_keys(Keys.ENTER)

# 进入文件夹
driver.find_element_by_xpath("//span[text()="+str(folder1)+"]").click()
sleep(2)
# 新建文件
ActionChains(driver).move_to_element(el1).perform()
driver.find_element_by_xpath("//li[text()='新建文档']").click()
sleep(2)

# 编辑内容：
el6=driver.find_element_by_xpath("//iframe").get_attribute("id")
print(el6)

driver.switch_to.frame(el6)

el5=driver.find_elements_by_xpath("//p/br[@data-mce-bogus='1']")

# print(el5)

driver.switch_to.active_element.send_keys("我是一个验证文件")

driver.switch_to.active_element.send_keys(Keys.ENTER)

# 退出编辑
driver.switch_to.default_content()
driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()


# 上传文件
driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\fir\\Desktop\\上传文件\\自动化验证文档\\回归的word文档.docx")

# sleep(10)

# el9=driver.find_element_by_xpath("//span[text()='回归的word文档']/../../../../a").get_attribute("href")
# el9=driver.find_element_by_xpath("//*[@id='file-list-wrapper']/div[1]/span/div/span/div/div/div[2]/div/div[2]/a").get_attribute("href")
# print("el9: %s" %el9)

start=int(time.time())


# WebDriverWait(driver,10,0.5).until(ec.element_to_be_clickable((By.XPATH,"//span[text()='回归的word文档']")))
for i in range(30):
    sleep(1)
    el9=driver.find_element_by_xpath("//span[text()='回归的word文档']/../../../../..").get_attribute("href")
    # print("el9: %s" %el9)
    if el9 != 'https://testcyprex.fir.ai/' :
        break
            

end=int(time.time())
print('用时  %d  秒' %(end-start))

# 进入文档
driver.find_element_by_xpath("//span[text()='回归的word文档']").click()
# sleep(3)
# WebDriverWait(driver,10,0.5).until(ec.presence_of_element_located((By.XPATH,"//span[text()='边写边搜']")))
WebDriverWait(driver,10,0.5).until(ec.element_to_be_clickable((By.XPATH,"//span[text()='边写边搜']")))

# 切换iframe
id2=driver.find_element_by_xpath("//iframe").get_attribute("id")

driver.switch_to.frame(id2)

dom1=driver.switch_to.active_element
# 键盘往上一行
dom1.send_keys(Keys.ENTER)
dom1.send_keys(Keys.UP)

# 输入文字
driver.switch_to.active_element.send_keys("我修改过")

dom1.send_keys(Keys.ENTER)
for i1 in range(5):
    dom1.send_keys(Keys.ENTER)
    dom1.send_keys(Keys.UP)
# 插入表格
driver.find_element_by_xpath("//button[@title='表格']").click()
table=driver.find_element_by_xpath("//div[@title='表格']")


# driver.switch_to.active_element.send_keys(Keys.ENTER)
# driver.find_elements_by_tag_name("p")[1].send_keys("我是何秦川")

# driver.quit()









