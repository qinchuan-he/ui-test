#coding=utf-8
from selenium.webdriver.common.keys import Keys

from common.comfunction import OpenBrowser,User,team
from time import sleep

# 创建word，并且输入内容
def create_word():
    ''' 登录系统'''
    mode = 1
    driver = OpenBrowser(mode)
    try:
        # 登录
        User().login(driver)
        # 进入团队
        team().check_team(driver, team_name='创建word文档')
        # 进入文件夹
        User().into_folder(driver,button_name='1112')
        # driver.find_element_by_xpath("//span[text()='0922']").click()
        # 新建文件
        User().create_file(driver,file_type='协作文档(.docx)')
        sleep(7)
        iframeid = driver.find_element_by_xpath("//iframe")
        driver.switch_to.frame(iframeid)
        dom = driver.switch_to.active_element
        dom.send_keys("我是一个验证文件，目前就只有这么多内容，后期会增加输入内容")
        dom.send_keys(Keys.ENTER)
        sleep(1)
        for i in range(3):
            dom.send_keys("【整体观点】我们维持2018年下半年到2020年底是投资5G通信设备产业链黄金期的判断。从通信(申万)指数上看,5G第一阶段主题投资行情从去年下半年到今年3月底基本告一段落,我们认为Q3季度预计是第二阶段业绩驱动5G行业的开始、也更加聚焦确定性大幅受益5G的核心标的。我们判断Q2阶段则属于上述两个阶段的过渡,6月6日5G牌照的发放属于第一阶段主题投资尾声的波澜,不代表短期趋势性行情,但消除了5G未来大规模投资的不确定性。4月中旬以来,经历了大盘调整及中美贸易摩擦、美国对华为出口限制扰动,通信行业(申万)指数也有约15％的调整,建议积极关注。")
            sleep(1)
            dom.send_keys(Keys.ENTER)
            dom.send_keys(Keys.ENTER)
            dom.send_keys(
                "关于运营商在5G共建共享政策趋势方面的观点。由三大运营商大部分铁塔资源转移合资组建的中国铁塔,成立于2014年,2015年开始承接新建铁塔、重点场所室分系统建设；2015年10月31日,三家电信企业将存量铁塔相关资产注入中国铁塔。基于工信部对5G网络共建共享的要求,我们认为有利于推动5G时代在铁塔、室分系统方面的共建共享,重点利好中国铁塔。对于基站设备的共建共享,我们认为中国广电未来依托中移动、部分地区基站设备共享以商用5G是可行的方案；对于中国联通等电信运营商的基站共享,我们认为在西部极个别不盈利的地区,可能以地市为单位试点基站共享,大部分地区不具有执行落地的可行性(中国移动具有明显的基站数量优势,我们认为其共享动力不足。对于其余运营商,我们认为强行推动基站共享从根本上会冲击网络体验差异化竞争、导致价格竞争的单一性,可能不利于产业良性发展)。")
            sleep(1)
            dom.send_keys(Keys.ENTER)
            dom.send_keys(Keys.ENTER)
            dom.send_keys(
                "5G电信设备侧产业链,A股相关板块无线基站设备、PCB、基站滤波器＆天线、光模块,基于行业格局、受益5G增量业绩弹性较大、确定性高；重点推荐:中兴通讯、世嘉科技、深南电路、以及中际旭创、通宇通讯；华为产业链关键器件进口替代关注圣邦股份(模拟器件)、紫光国微(FPGA)、华正新材/生益科技(高频CCL)。H股、美股相关标的,关注:中兴通讯(00763.HK)、中国铁塔(00788.HK)、爱立信(ERIC.US)、赛灵思(XLNX.US)、科锐(CREE.US)、II-VI(IIVI.US)等5G产业链全球各细分领域龙头企业。")
            sleep(1)
            dom.send_keys(Keys.ENTER)
            dom.send_keys(Keys.ENTER)
            dom.send_keys(
                "北美云计算服务巨头资本开支增长幅度2018年下半年整体放缓,此外根据LightCounting最新季度市场报告,2019年一季度排名前15位的云服务公司季度支出有所下滑。但我们预计2019下半年全球整体云计算投资增速有望再次回升；国内二线云计算服务企业积极加大资本投入,华为事件助将推政企客户降低对美国传统占优的IT架构生态体系依赖、加速上云。泛云计算方向(资本开支相关、网络可视化、云通讯、IDC等),重点推荐星网锐捷、紫光股份、中新赛克、中际旭创、亿联网络、光环新网,其次关注深信服、迪普科技、金山软件(03888.HK)、万国数据(GDS.US)等。")
            dom.send_keys(Keys.ENTER)
            dom.send_keys(Keys.ENTER)
            dom.send_keys(
                "中国移动将在上海正式发布“5G+计划“。根据中国移动官方微博消息,6月25日中国移动将在上海正式发布“5G+计划“,届时发布5G标识、5G+硬核能力体系、5G终端先行者升级计划、5G+行业应用等系列内容。三大运营商5月的运营数据已尽数披露,中国移动4G用户增长500万、一改4月份负增长的颓势,同时在净增4G用户及宽带用户均保持了较为明显的优势。我们认为中国移动作为行业引领者,在5G建设及应用中将发挥先导作用,此次“5G+计划“发布有望更进一步推动5G加快发展。")
            sleep(1)
            dom.send_keys(Keys.ENTER)
            dom.send_keys(Keys.ENTER)
            dom.send_keys(
                "华为计划五年内投资1000亿美元,对网络架构进行重构。2019年6月17日,在美国学者与任正非的咖啡对话中,任正非提到未来几年公司可能会减产,销售收入会比计划下降300亿美元,2019-2020年的销售收入预计都在1000亿美元左右(2018年华为年报披露营收约为1050亿美元),2021年华为可能会重新焕发出勃勃生机。同时任正非提到公司计划五年内投资1000亿美元,对网络架构进行重构,使其更简单、更快捷、更安全、更可信、隐私保护至少达到欧洲GDPR标准。")
            sleep(1)
            dom.send_keys(Keys.ENTER)
            dom.send_keys(Keys.ENTER)

        driver.switch_to.default_content()
        # 退出编辑
        sleep(5)
        driver.find_element_by_xpath("//span[contains(@class,'editor_backBtnImg')]").click()
    except Exception as e:
        print(e)
    driver.quit()
















if __name__=='__main__':
    for i in range(20):
        create_word()


















