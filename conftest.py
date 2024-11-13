import os
import sys
import pytest
# from py.xml import html  # 我的python3.7上面没有这个
from py._xmlgen import html # 使用这个代替上面的
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FF_Options
from common.private import UserProperty
import time
import shutil
# 引入公共参数，把url和用户信息放在一起的
from common.comfunction import url
# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 移动了配置文件，调整路径,又移动回来了
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
REPORT_DIR = os.path.join(BASE_DIR,"test_report")
############################
# 配置是否保留上一次的报告
history_save = 0 # 是否保留上次报告，1是保留，其他都不保留
# 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
# driver_type = "chrome"
driver_type = "chrome-headless"
# path = "C:\\2services\\driver\\chromedriver.exe" # 2020/01/09调整参数化
path = UserProperty().BROWER_PATH
# 配置运行的 URL, ---------改为了登录方法中控制,为
# 了切换环境时候方便
# url = "https://testcyprex.fir.ai/sign-in"
# 失败重跑次数
rerun = "1"
# 当达到最大失败数，停止执行
max_fail = "1"
# 运行测试用例的目录或文件
cases_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),"test_dir")

############################

# 定义基本测试环境
@pytest.fixture(scope='function')
def base_url():
    return url


# 设置用例描述表头
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


# 设置用例描述表格
@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(3, html.td(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), class_='col-time'))
    cells.pop()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = description_html(item.function.__doc__)
    extra = getattr(report, 'extra', [])
    case_path = report.nodeid.split("::")[-1] # 取函数的名字作为截图前缀
    case_name_e = os.path.join(case_path,"-error-",str(time.time())+".png") # -连接截图路径
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            print("进入失败判断")
            case_name = case_name_e
            capture_screenshot(case_name)
            # img_path = "image/" + case_name.split("/")[-1] # 根据我的需要，截图为时间戳
            # img_path = "image/" + case_name
            img_path = os.path.join("image",case_name) # 调整路径
            if img_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % img_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
    image_path = os.path.join(REPORT_DIR,new_report_time(),"image")
    images = os.listdir(image_path)
    images.sort()
    print("获取列表中文件----")
    print(images)
    for img in images:
        img_name = img.split("-")  # 约定，截图规则为：函数名-名称+时间戳。test_folder-1566997014.5933237.png
        if img_name[0] == case_path:  # 选择截图中当前路径的
            screen_html = '<div><a href="%s">%s</a></div>' % ("image/" + img, img_name[1])
            extra.append(pytest_html.extras.html(screen_html))
            report.extra = extra

##########################################################
# 我自己增加的方法
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("测试人: 乌鸦")])
def pytest_configure(config):
    config._metadata['测试地址'] = url

# 创建存放图片的路径
@pytest.fixture(scope='function')
def images_path():
    global image_path
    image_path = os.path.join(REPORT_DIR,new_report_time(),"image")
    return image_path
#########################################################

def description_html(desc):
    """
    将用例中的描述转成HTML对象
    :param desc: 描述
    :return:
    """
    if desc is None:
        return "No case description"
    desc_ = ""
    for i in range(len(desc)):
        if i == 0:
            pass
        elif desc[i] == '\n':
            desc_ = desc_ + ";"
        else:
            desc_ = desc_ + desc[i]

    desc_lines = desc_.split(";")
    desc_html = html.html(
        html.head(
            html.meta(name="Content-Type", value="text/html; charset=latin1")),
        html.body(
            [html.p(line) for line in desc_lines]))
    return desc_html


def capture_screenshot(case_name):
    """
    配置用例失败截图路径
    :param case_name: 用例名
    :return:
    """
    global driver
    new_report_dir = new_report_time()
    if new_report_dir is None:
        raise RuntimeError('没有初始化测试目录')
    image_name = os.path.join(REPORT_DIR, new_report_dir, "image", case_name) # 调整了图片名称
    driver.save_screenshot(image_name)  # 截图保存在当前目录下


def new_report_time():
    """
    获取最新报告的目录名（即运行时间，例如：2018_11_21_17_40_44，因为我有init文件，所以是-2）
    """
    files = os.listdir(REPORT_DIR)
    files.sort()
    try:
        if history_save==1:  # 为了可以直接访问报告，这里增加了一个判断参数
            # 为了保证路径正确，把那两个报告删了

            if os.path.exists(os.path.join(REPORT_DIR,"image")):
                shutil.rmtree(os.path.join(REPORT_DIR,"image"),ignore_errors=True)
            if os.path.exists(os.path.join(REPORT_DIR,"junit-xml.xml")):
                os.remove(os.path.join(REPORT_DIR,"junit-xml.xml"))
            if os.path.exists(os.path.join(REPORT_DIR,"report.html")):
                os.remove(os.path.join(REPORT_DIR,"report.html"))
            return files[-2]
        else:
            return ""
    except IndexError:
        return None


# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser():
    """
    全局定义浏览器驱动
    :return:
    """
    global driver
    global driver_type
    if driver_type == "chrome":
        # 本地chrome浏览器
        print("进入chrome浏览器流程")
        driver = webdriver.Chrome(path)
        driver.set_window_size(1400, 900)
        driver.implicitly_wait(15)

    elif driver_type == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)

    elif driver_type == "chrome-headless":
        # chrome headless模式
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options, executable_path=path)
        driver.implicitly_wait(30)

    elif driver_type == "firefox-headless":
        # firefox headless模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(firefox_options=firefox_options)

    # elif driver_type == "grid":
    #     # 通过远程节点运行
    #     driver = Remote(command_executor='http://10.2.16.182:4444/wd/hub',
    #                     desired_capabilities={
    #                         "browserName": "chrome",
    #                     })
    #     driver.set_window_size(1920, 1080)

    else:
        raise NameError("driver驱动类型定义错误！")

    return driver


# 关闭浏览器
@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("test end!")
