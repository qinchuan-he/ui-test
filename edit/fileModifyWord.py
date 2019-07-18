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
from selenium.webdriver.chrome.options import Options
from time import sleep
import time   #生成时间戳用
import os    #上传autoit用

"""解决vscode中不能引用别的模块的问题"""
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


# 调用公共方法
from common.comfunction import team
from common.comfunction import com_share

# 上传word，修改word（未用边写边搜），下载word, 20190716增加了分享功能

opt=Options()
opt.add_argument('--disable-gpu')
opt.add_argument('--headless')
path="C:\\2services\\driver\\chromedriver.exe"
driver=webdriver.Chrome(path)
# driver=webdriver.Chrome(options=opt,executable_path=path)   #无头模式

search="股份"
picturePath="C:\\work\\1测试\\10自动化\\截图保存\\编辑文件截图\\"
waitTime=2
url="https://testcyprex.fir.ai/sign-in"
# url="https://cyprex.fir.ai/sign-in"
# url = "http://firai-test.gjzqth.com:4680/sign-in"
user="13248131618"
pwd="Test123456"
uploadPath="C:\\work\\1测试\\10自动化\\word插入图片脚本\\upfile.exe"

driver.set_window_size(1400,900) 



driver.implicitly_wait(20)

driver.get(url)
driver.find_element_by_xpath("//div[text()='账号登录']").click() 
driver.find_element_by_id("username_no").send_keys(user)
driver.find_element_by_id("password").send_keys(pwd)
driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div[1]/div[3]/div[2]/form/div[3]/div/div/span").click()   # 登录，好像伪类中的文字不能识别
WebDriverWait(driver,10,0.2).until(ec.presence_of_element_located((By.XPATH,"//span[text()='艾玛同学']")))

team_name = team().check_team(driver)
driver.find_element_by_xpath("//a[contains(@class,'GlobalHeader_logo')]").click()
sleep(1)

# 创建文件夹，以当前时间命名
el1=driver.find_element_by_xpath("//span[text()='新建']")
sleep(waitTime)
ActionChains(driver).move_to_element(el1).perform()
driver.find_element_by_xpath("//li[text()='新建文件夹']").click()
folder1=int(time.time())
print(folder1)
driver.switch_to.active_element.send_keys(folder1)
driver.switch_to.active_element.send_keys(Keys.ENTER)

# 进入文件夹
driver.find_element_by_xpath("//span[text()="+str(folder1)+"]").click()
sleep(waitTime)
# 新建文件
ActionChains(driver).move_to_element(el1).perform()
driver.find_element_by_xpath("//li[text()='新建文档']").click()
WebDriverWait(driver,10,0.5).until(ec.presence_of_element_located((By.XPATH,"//iframe")))
nameaddress=driver.find_element_by_xpath("//input[contains(@class,'ant-input FileToolbar_fileTitle__')]")
# nameaddress.send_keys(Keys.CONTROL,'a')
# nameaddress.send_keys(Keys.BACK_SPACE)
# nameaddress.send_keys("自动化")
sleep(waitTime)
# 编辑内容：
iframeid=driver.find_element_by_xpath("//iframe").get_attribute("id")
print(iframeid)

driver.switch_to.frame(iframeid)

el5=driver.find_elements_by_xpath("//p/br[@data-mce-bogus='1']")

# print(el5)

dom1=driver.switch_to.active_element

dom1.send_keys("我是一个验证文件，目前就只有这么多内容，后期会增加输入内容")

dom1.send_keys(Keys.ENTER)

dom1.send_keys("【整体观点】我们维持2018年下半年到2020年底是投资5G通信设备产业链黄金期的判断。从通信(申万)指数上看,5G第一阶段主题投资行情从去年下半年到今年3月底基本告一段落,我们认为Q3季度预计是第二阶段业绩驱动5G行业的开始、也更加聚焦确定性大幅受益5G的核心标的。我们判断Q2阶段则属于上述两个阶段的过渡,6月6日5G牌照的发放属于第一阶段主题投资尾声的波澜,不代表短期趋势性行情,但消除了5G未来大规模投资的不确定性。4月中旬以来,经历了大盘调整及中美贸易摩擦、美国对华为出口限制扰动,通信行业(申万)指数也有约15％的调整,建议积极关注。")
dom1.send_keys(Keys.ENTER)
dom1.send_keys(Keys.ENTER)
dom1.send_keys("关于运营商在5G共建共享政策趋势方面的观点。由三大运营商大部分铁塔资源转移合资组建的中国铁塔,成立于2014年,2015年开始承接新建铁塔、重点场所室分系统建设；2015年10月31日,三家电信企业将存量铁塔相关资产注入中国铁塔。基于工信部对5G网络共建共享的要求,我们认为有利于推动5G时代在铁塔、室分系统方面的共建共享,重点利好中国铁塔。对于基站设备的共建共享,我们认为中国广电未来依托中移动、部分地区基站设备共享以商用5G是可行的方案；对于中国联通等电信运营商的基站共享,我们认为在西部极个别不盈利的地区,可能以地市为单位试点基站共享,大部分地区不具有执行落地的可行性(中国移动具有明显的基站数量优势,我们认为其共享动力不足。对于其余运营商,我们认为强行推动基站共享从根本上会冲击网络体验差异化竞争、导致价格竞争的单一性,可能不利于产业良性发展)。")
dom1.send_keys(Keys.ENTER)
dom1.send_keys(Keys.ENTER)
dom1.send_keys("5G电信设备侧产业链,A股相关板块无线基站设备、PCB、基站滤波器＆天线、光模块,基于行业格局、受益5G增量业绩弹性较大、确定性高；重点推荐:中兴通讯、世嘉科技、深南电路、以及中际旭创、通宇通讯；华为产业链关键器件进口替代关注圣邦股份(模拟器件)、紫光国微(FPGA)、华正新材/生益科技(高频CCL)。H股、美股相关标的,关注:中兴通讯(00763.HK)、中国铁塔(00788.HK)、爱立信(ERIC.US)、赛灵思(XLNX.US)、科锐(CREE.US)、II-VI(IIVI.US)等5G产业链全球各细分领域龙头企业。")
dom1.send_keys(Keys.ENTER)
dom1.send_keys(Keys.ENTER)
dom1.send_keys("北美云计算服务巨头资本开支增长幅度2018年下半年整体放缓,此外根据LightCounting最新季度市场报告,2019年一季度排名前15位的云服务公司季度支出有所下滑。但我们预计2019下半年全球整体云计算投资增速有望再次回升；国内二线云计算服务企业积极加大资本投入,华为事件助将推政企客户降低对美国传统占优的IT架构生态体系依赖、加速上云。泛云计算方向(资本开支相关、网络可视化、云通讯、IDC等),重点推荐星网锐捷、紫光股份、中新赛克、中际旭创、亿联网络、光环新网,其次关注深信服、迪普科技、金山软件(03888.HK)、万国数据(GDS.US)等。")
dom1.send_keys(Keys.ENTER)
dom1.send_keys(Keys.ENTER)
dom1.send_keys("中国移动将在上海正式发布“5G+计划“。根据中国移动官方微博消息,6月25日中国移动将在上海正式发布“5G+计划“,届时发布5G标识、5G+硬核能力体系、5G终端先行者升级计划、5G+行业应用等系列内容。三大运营商5月的运营数据已尽数披露,中国移动4G用户增长500万、一改4月份负增长的颓势,同时在净增4G用户及宽带用户均保持了较为明显的优势。我们认为中国移动作为行业引领者,在5G建设及应用中将发挥先导作用,此次“5G+计划“发布有望更进一步推动5G加快发展。")
dom1.send_keys(Keys.ENTER)
dom1.send_keys(Keys.ENTER)
dom1.send_keys("华为计划五年内投资1000亿美元,对网络架构进行重构。2019年6月17日,在美国学者与任正非的咖啡对话中,任正非提到未来几年公司可能会减产,销售收入会比计划下降300亿美元,2019-2020年的销售收入预计都在1000亿美元左右(2018年华为年报披露营收约为1050亿美元),2021年华为可能会重新焕发出勃勃生机。同时任正非提到公司计划五年内投资1000亿美元,对网络架构进行重构,使其更简单、更快捷、更安全、更可信、隐私保护至少达到欧洲GDPR标准。")
dom1.send_keys(Keys.ENTER)
dom1.send_keys(Keys.ENTER)
for i1 in range(5):
    dom1.send_keys(Keys.ENTER)
    dom1.send_keys(Keys.UP)

dom1.send_keys("新建表格")
dom1.send_keys(Keys.ENTER)
# 插入表格
# 点击按钮,需要先脱离当前iframe
driver.switch_to.default_content()
driver.find_element_by_xpath("//button[@aria-label='表格']").click()
WebDriverWait(driver,5,0.5).until(ec.visibility_of_element_located((By.XPATH,"//div[@title='表格']")))

table1=driver.find_element_by_xpath("//div[@title='表格']")
ActionChains(driver).move_to_element(table1).perform()

WebDriverWait(driver,5,0.2).until(ec.presence_of_element_located((By.XPATH,"//div[@class='tox-tiered-menu']/div[2]/div/div/div/div[@role='button']")))

table2=driver.find_element_by_xpath("//div[@class='tox-tiered-menu']/div[2]/div/div/div/div[@role='button'][25]")
ActionChains(driver).move_to_element(table2).perform()
table2.click()

driver.switch_to.frame(iframeid)

dom1.send_keys("项目")
dom1.send_keys(Keys.RIGHT)
dom1.send_keys("公司")
dom1.send_keys(Keys.RIGHT)
dom1.send_keys("银行")
dom1.send_keys(Keys.RIGHT)
dom1.send_keys("金额")
dom1.send_keys(Keys.RIGHT)
dom1.send_keys("到期日期")

dom1.send_keys(Keys.DOWN)
for i3 in range(4):
    dom1.send_keys(Keys.LEFT)


dom1.send_keys("信用证保证金")
dom1.send_keys(Keys.RIGHT)
dom1.send_keys("蓝帆医疗股份有限公司")
dom1.send_keys(Keys.RIGHT)
dom1.send_keys("中国银行淄博临淄支行")
dom1.send_keys(Keys.RIGHT)
dom1.send_keys("252,618,3.00")
dom1.send_keys(Keys.RIGHT)
dom1.send_keys("已到期")

dom1.send_keys(Keys.DOWN)
for i3 in range(4):
    dom1.send_keys(Keys.LEFT)

dom1.send_keys("信用证保证金")
dom1.send_keys(Keys.RIGHT)
dom1.send_keys("山东蓝帆新材料有限公司")
dom1.send_keys(Keys.RIGHT)
dom1.send_keys("中国农业银行临朐支行")
dom1.send_keys(Keys.RIGHT)
dom1.send_keys("3,550,000.00")
dom1.send_keys(Keys.RIGHT)
dom1.send_keys("201901.02")
dom1.send_keys(Keys.DOWN)

# 插入图片
# 退出iframe
driver.switch_to.default_content()

# nowhandle=driver.current_window_handle
# print("原来的窗口句柄：%s" %nowhandle)
driver.find_element_by_xpath("//button[@title='插入图片']").click()
sleep(waitTime)   # 等待弹窗加载
# nowhandle2=driver.current_window_handle
# print("现在的窗口句柄：%s" %nowhandle2)
os.system(uploadPath)
sleep(waitTime)
driver.switch_to.frame(iframeid)
dom1.send_keys(Keys.ENTER)
dom1.send_keys("本次编辑完成")
dom1.send_keys(Keys.ENTER)
sleep(waitTime)
picture=str(int(time.time()))
driver.get_screenshot_as_file(picturePath+"边写边搜截图"+str(int(time.time()))+".png")

# 下载
driver.switch_to.default_content()
driver.find_element_by_xpath("//i[@class='anticon anticon-download']").click()

# 下载之后增加分享功能
# 调用团队验证方法
driver.find_element_by_xpath("//i[@class='anticon anticon-share-alt']").click()

# 点击之后，调用分享弹框公共方法
version = "保留两者"
print_name = "文件夹内搜索分享"
pic_path = picturePath
com_share(team_name, version, print_name, pic_path, driver)

# 等待下载时间
sleep(waitTime)
sleep(waitTime)
sleep(waitTime)

# 退出编辑
driver.switch_to.default_content()
driver.find_element_by_xpath("//span[contains(text(),'返回')]/..").click()
driver.get_screenshot_as_file(picturePath+"边写边搜返回截图"+str(int(time.time()))+".png")

sleep(15)
driver.quit()






