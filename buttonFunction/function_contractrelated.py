# coding=utf-8

# 智能比对

from common.comfunction import *



file1="D:\\上传文件\\自动化验证文档\\19种格式\\比对文件\\合同1.docx"
# file2="D:\\上传文件\\自动化验证文档\\19种格式\\比对文件\\合同1扫描件（8张合并）.pdf"

# 合同比对,传入两个url
def contract_compare(driver,url1,url2):
    # 开始动作
    User().switch_navigation(driver,name="智能比对")
    com_xpath().com_localupload(driver,url1)
    sleep(0.5)
    com_xpath().com_localupload(driver, url2,position=2)
    WebDriverWait(driver,5,0.2).until(ec.element_to_be_clickable((By.XPATH,"//span[text()='开始比对']/..")))
    driver.find_element_by_xpath("//span[text()='开始比对']/..").click()

# 智能审核
def contract_Proofreading(driver,url):
    User().switch_navigation(driver,name="智能审核")
    com_xpath().com_localupload(driver,url)
    WebDriverWait(driver,5,0.2).until(ec.element_to_be_clickable((By.XPATH,"//span[text()='智能审核']/..")))
    driver.find_element_by_xpath("//span[text()='智能审核']/..").click()

mode = 2
driver = execBrower(mode)
driver.get(url)
User().login(driver)
# contract_compare(driver,file1,file2)
contract_Proofreading(driver,file1)
sleep(7)
driver.quit()