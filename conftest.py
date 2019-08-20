import os
import pytest
# from py.xml import html  # 我的python3.7上面没有这个
from py._xmlgen import html # 使用这个代替上面的
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
import time
# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 移动了配置文件，调整路径
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
REPORT_DIR = BASE_DIR + "/test_report/"
# REPORT_DIR = "C:\\work\\1测试\\1需求\\cyprex1.13\\ui\\"
############################

# 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
driver_type = "chrome"
path = "C:\\2services\\driver\\chromedriver.exe"
# 配置运行的 URL
# url = "https://www.baidu.com"
url = "https://testcyprex.fir.ai/sign-in"

# 失败重跑次数
rerun = "0"

# 当达到最大失败数，停止执行
max_fail = "1"

# 运行测试用例的目录或文件
cases_path = "./test_dir/"
# -------------我自己增加的变量


############################


# 定义基本测试环境
@pytest.fixture(scope='function')
def base_url():
    global url
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
    cells.insert(3, html.td(time.time(), class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    # print("pytest_html: ---")
    # print(pytest_html)
    outcome = yield
    report = outcome.get_result()
    # print("report----")
    # print(report)
    report.description = description_html(item.function.__doc__)
    # print("report.description----")
    # print(report.description)
    extra = getattr(report, 'extra', [])
    # print("extra-----")
    # print(extra)
    # print("report.when----")
    # print(report.when)


    case_path = report.nodeid.split("::")[-1] # 取函数的名字作为截图前缀
    # print(case_path)
    case_name_e = case_path+"-error-"+str(time.time())+".png"  # -连接截图路径
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        # print("xfail----")
        # print(xfail)
        # print("report.skipped----")
        # print(report.skipped)
        # print("report.failed---")
        # print(report.failed)
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 根据我的需要（一个用例可能截图多张），截图名需要为时间戳
            # case_path = report.nodeid.replace("::", "_") + ".png"
            # if "[" in case_path:
            #     case_name = case_path.split("-")[0] + "].png"
            # else:
            #     case_name = case_path
            print("进入失败判断")
            case_name = case_name_e
            capture_screenshot(case_name)
            # img_path = "image/" + case_name.split("/")[-1] # 根据我的需要，截图为时间戳
            img_path = "image/" + case_name
            # print("打印img_path")
            # print(img_path)
            if img_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % img_path
                extra.append(pytest_html.extras.html(html))

                # html1 = '<div><a href="%s" >"%s"</a></div>' % (img_path, case_name)
                # extra.append(pytest_html.extras.html(html1))
        report.extra = extra
    image_path = str(REPORT_DIR)+str(new_report_time())+"/image/"
    images = os.listdir(image_path)
    images.sort()
    print("获取列表中文件----")
    print(images)
    for img in images:
        img_name = img.split("-")
        if img_name[0] == case_path:  # 选择截图中当前路径的
            html = '<div><a href="%s" >"%s"</a></div>' % ("image/" + img, img_name[1])
            extra.append(pytest_html.extras.html(html))
            report.extra = extra
    # case_name = str(time.time()) + ".png"
    # capture_screenshot(case_name)
    # img_path = "image/" + case_name
    # if img_path:
    #     html1 = '<div><a href="%s" >"验证截图的我"</a></div>' % img_path
    #     extra.append(pytest_html.extras.html(html1))
    #     report.extra = extra

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
    image_path = str(REPORT_DIR) + str(new_report_time()) + "/image/"
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
    # print("图片名称: ")
    # print(case_name)
    global driver
    # file_name = case_name.split("/")[-1]
    new_report_dir = new_report_time()
    # print("图片路径 REPORT_DIR"+REPORT_DIR)
    # print("图片路径 new_report_dir---"+new_report_dir)
    if new_report_dir is None:
        raise RuntimeError('没有初始化测试目录')
    # image_dir = os.path.join(REPORT_DIR, new_report_dir, "image", file_name) # 路径拼接
    image_dir = os.path.join(REPORT_DIR, new_report_dir, "image", case_name) # 调整了图片名称
    # print("拼接路径 image_dir "+image_dir)
    driver.save_screenshot(image_dir)


def new_report_time():
    """
    获取最新报告的目录名（即运行时间，例如：2018_11_21_17_40_44）
    """
    files = os.listdir(REPORT_DIR)
    files.sort()
    # print("获取的目录：")
    # print(files)
    # print(files[-2])
    try:
        return files[-2]
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

    elif driver_type == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)

    elif driver_type == "chrome-headless":
        # chrome headless模式
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)

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


if __name__ == "__main__":
    capture_screenshot("test_dir/test_baidu_search.test_search_python.png")