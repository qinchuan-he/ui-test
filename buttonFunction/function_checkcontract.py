# coding=utf-8

from common.comfunction import *
import time

# 合同比对和审校的检查，设计是一小时之前执行了创建数据

#检查合同比对，传入driver和image_path
def check_compare(driver, image_path=None,image_prefix=None,is_check=None):
    '''检查当日比对'''
    User().switch_navigation(driver, name="智能比对")
    sleep(1)
    if is_check: # 执行检查，截图
        driver.get_screenshot_as_file(os.path.join(com_path(),"截图","智能比对列表截图.png"))
    if image_path:
        driver.get_screenshot_as_file(os.path.join(image_path,image_prefix,"-合同防伪列表",str(time.time())+".png"))
    driver.find_element_by_xpath("//div[contains(text(),'今天')]/..//span[text()='查看明细']").click()
    WebDriverWait(driver, 10, 0.5).until(ec.presence_of_element_located((By.XPATH, "//div[text()='文本比对']")))
    sleep(1)
    if image_path:
        driver.get_screenshot_as_file(os.path.join(image_path,image_prefix,"-比对结果",str(time.time())+".png"))
    com_operation().com_close_preview(driver)
    # 2020-01-26功能变更，比对不生成报告了
    # sleep(1)
    # driver.find_element_by_xpath("//div[contains(text(),'今天')]/..//span[text()='查看报告']").click()
    #
    # WebDriverWait(driver, 15, 0.5).until(ec.presence_of_element_located((By.XPATH, "//div[text()='查看报告']")))
    # if image_path:
    #     driver.get_screenshot_as_file(image_path + image_prefix + "-比对报告" + str(time.time()) + ".png")
    # com_operation().com_close_preview(driver)



def check_proofreading(driver,image_path=None,image_prefix=None,is_check=None):
    '''检查当日审校'''
    User().root_private(driver)
    User().switch_navigation(driver,name="智能审核")
    # 下面的循环不适用目前的检查，目前比对和审校一起的
    # for i in range(36):
    #     els = driver.find_elements_by_xpath("//div[@class='ant-row']/div[3]")
    #     print(len(els))
    #     print(els[1])
    #     content = els[1].text
    #     print(content)
    #     if content == "要素快照风险报告":
    #         print("审核成功")
    #         break
    #     elif content == "审校失败再次审校":
    #         print("审核失败")
    #         break
    #     elif i == 35:
    #         print("审核超时")
    #         break
    #     else:
    #         sleep(10)
    sleep(0.5)
    if is_check: # 执行检查，截图
        driver.get_screenshot_as_file(os.path.join(com_path(),"截图","智能审核列表截图.png"))
    if image_path:
        driver.get_screenshot_as_file(os.path.join(image_path,image_prefix,"-审校列表",str(time.time())+".png"))
    driver.find_element_by_xpath("//div[contains(text(),'今天')]/../..//span[text()='要素快照']").click()
    sleep(0.5)
    if image_path:
        driver.get_screenshot_as_file(os.path.join(image_path,image_prefix,"-要素快照",str(time.time())+".png"))
# 2020-01-15增加图片比对功能
    driver.find_element_by_xpath("//div[text()='合同主体']").click()
    sleep(1)
    driver.get_screenshot_as_file(os.path.join(com_path(),"截图","合同要素.png"))

    driver.find_element_by_xpath("//span[@class='ant-modal-close-x']/..").click()
    sleep(0.5)
    driver.find_element_by_xpath("//div[contains(text(),'今天')]/../..//span[text()='风险报告']").click()
    WebDriverWait(driver,10,0.5).until(ec.presence_of_element_located((By.XPATH,"//div[text()='查看报告']")))
    sleep(0.5)
    if image_path:
        driver.get_screenshot_as_file(image_path+image_prefix+"-风险报告"+str(time.time())+".png")
    com_operation().com_close_preview(driver)





#
# mode = 2
# driver = OpenBrowser(mode)
# driver.get(url)
# User().login(driver)
# # image_path=""
# check_compare(driver)
