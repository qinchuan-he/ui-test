# coding=utf-8

# 智能比对

from common.comfunction import *
from common.private import EmailProperty



file1="D:\\上传文件\\自动化验证文档\\19种格式\\比对文件\\合同1.docx"
# file2="D:\\上传文件\\自动化验证文档\\19种格式\\比对文件\\合同1扫描件（8张合并）.pdf"

# 合同比对,传入两个url
def contract_compare(driver,url1,url2):
    # 开始动作
    User().switch_navigation(driver,name="智能比对")
    com_xpath().com_localupload(driver,url1)
    sleep(0.5)
    com_xpath().com_localupload(driver, url2,position=2)
    sleep(1)
    WebDriverWait(driver,5,0.2).until(ec.element_to_be_clickable((By.XPATH,"//span[text()='开始比对']/..")))
    driver.find_element_by_xpath("//span[text()='开始比对']/..").click()

# 智能审核，传入一个url
def contract_Proofreading(driver,url):
    User().switch_navigation(driver,name="智能审核")
    com_xpath().com_localupload(driver,url)
    sleep(1)
    WebDriverWait(driver,5,0.2).until(ec.element_to_be_clickable((By.XPATH,"//span[text()='智能审核']/..")))
    driver.find_element_by_xpath("//span[text()='智能审核']/..").click()


# 合同拆分
def contratc_split(driver,url):
    """
    合同拆分
    :param driver:
    :param url:
    :return:
    """
    # 创建拆分协作空间，默认进入团队根目录
    User().switch_navigation(driver, name="智能编写")
    sleep(1)
    team().check_team(driver)
    space_name = "拆分"+str(time.time())
    team().create_cooperation(driver,space_name)
    # 进行拆分
    driver.find_element_by_xpath("//span[text()='智能分拆任务']/..").click()
    sleep(0.5)
    el = driver.find_elements_by_xpath("//input[@type='file']")
    el[1].send_keys(url)
    sleep(3)
    el2 = driver.find_element_by_xpath("//span[text()='开始分拆']/..")
    if el2.is_enabled():
        el2.click()
        sleep(3)
        for i in range(20):
            sleep(6)
            try:
                el = driver.find_elements_by_xpath("//span[contains(@class,'WorkSpaceTasks_taskItemTitle')]")
                if len(el)>1: # 拆分成功
                    print("拆分成功")
                    break
                else:# 拆分失败
                    print("拆分失败")
                    # 截图
                    driver.get_screenshot_as_file(os.path.join(com_path(),"截图","拆分失败截图.png"))
                    send_mail("拆分检查邮件",EmailProperty().EMAIL_SPLIT,os.path.join(com_path(),"截图","拆分失败截图.png"),"split.png")
                    break
            except Exception as e:
                print(e)
    else:
        print("上传超时")
        sleep(1)
        # 截图
        driver.get_screenshot_as_file(os.path.join(com_path(),"截图","拆分上传截图.png"))
        send_mail("拆分检查邮件", EmailProperty().EMAIL_SPLIT, os.path.join(com_path(),"截图","拆分上传截图.png"), "upload_file.png")
    sleep(1)

# 协作空间合并
def contract_combine(driver,url1,url2,url3):
    """
    协作空间中合并文档,四合一
    :param driver:
    :param url1:
    :param url2:
    :return:
    """
    # 创建拆分协作空间，默认进入团队根目录
    User().switch_navigation(driver, name="智能编写")
    sleep(1)
    team().check_team(driver)
    space_name = "合并"+str(time.time())
    team().create_cooperation(driver,space_name)
    sleep(0.5)
    driver.find_element_by_xpath("//input[@type='file']").send_keys(url1)
    driver.find_element_by_xpath("//input[@type='file']").send_keys(url2)
    driver.find_element_by_xpath("//input[@type='file']").send_keys(url3)
    sleep(10)
    driver.find_element_by_xpath("//input[@type='checkbox']").click()
    sleep(1)
    # el = driver.find_element_by_xpath("//div[text()='合并任务文档']")
    el = driver.find_element_by_xpath("//i[@class='anticon anticon-cluster']")
    if el.is_enabled():
        el.click()
        sleep(0.5)
        driver.find_element_by_xpath("//span[text()='确 定']/..").click()
        sleep(1)
        for i in range(15):
            sleep(6)
            try:
                el = driver.find_element_by_xpath("//div[contains(@class,'WorkSpaceTasks_taskFileNameBox')]")
                print("合并成功")
                break
            except Exception as e:
                print(e)
                if i==14:
                    # 截图
                    driver.get_screenshot_as_file(os.path.join(com_path(),"截图","合并失败截图.png"))
                    send_mail("合并检查邮件", EmailProperty().EMAIL_COMBINE, os.path.join(com_path(),"截图","合并失败截图.png"),
                              "combine.png")
    else:
        print("上传超时导致没有选中")
        # 截图
        driver.get_screenshot_as_file(os.path.join(com_path(),"截图","合并上传截图.png"))
        send_mail("合并检查邮件", EmailProperty().EMAIL_COMBINE, os.path.join(com_path(),"截图","合并上传截图.png"),
                  "upload_file.png")
    sleep(1)



# mode = 2
# driver = OpenBrowser(mode)
# driver.get(url)
# User().login(driver)
# # contratc_split(driver,url25)
# # # contract_compare(driver,file1,file2)
# # contract_Proofreading(driver,file1)
# # contract_combine(driver,url26,url27,url28)
# team().dismiss_team(driver,"验证的团队")
# sleep(7)
# driver.quit()