# import os
# import pytest
# # from py.xml import html # import html
# from selenium import webdriver
# from selenium.webdriver import Remote
# from selenium.webdriver.chrome.options import Options as CH_Options
# from selenium.webdriver.firefox.options import Options as FF_Options
#
# # 项目目录配置
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# REPORT_DIR = BASE_DIR + "/test_report/"
#
# ############################
#
# # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
# driver_type = "chrome"
#
# # 配置运行的 URL
# url = "https://testcyprex.fir.ai/sign-in"
# # url = "https://cyprex.fir.ai/sign-in"
#
# # 失败重跑次数
# rerun = "3"
#
# # 运行测试用例的目录或文件
# cases_path = "./test_dir/"
#
#
# ############################
#
#
# # 定义基本测试环境
# @pytest.fixture(scope='function')
# def base_url():
#     global url
#     return url
#
#
# def capture_screenshot(case_name):
#     """
#     配置用例失败截图路径
#     :param case_name: 用例名
#     :return:
#     """
#     global driver
#     file_name = case_name.split("/")[-1]
#     new_report_dir = new_report_time()
#     if new_report_dir is None:
#         raise RuntimeError('没有初始化测试目录')
#     image_dir = os.path.join(REPORT_DIR, new_report_dir, "image", file_name)
#     driver.save_screenshot(image_dir)
#
#
# def new_report_time():
#     """
#     获取最新报告的目录名（即运行时间，例如：2018_11_21_17_40_44）
#     """
#     files = os.listdir(REPORT_DIR)
#     files.sort()
#     try:
#         return files[-1]
#     except IndexError:
#         return None
#
#
# # 启动浏览器
# @pytest.fixture(scope='session', autouse=True)
# def browser():
#     """
#     全局定义浏览器驱动
#     :return:
#     """
#     global driver
#     global driver_type
#
#     if driver_type == "chrome":
#         # 本地chrome浏览器
#         driver = webdriver.Chrome()
#         driver.set_window_size(1400, 900)
#
#     elif driver_type == "firefox":
#         # 本地firefox浏览器
#         driver = webdriver.Firefox()
#         driver.set_window_size(1920, 1080)
#
#     elif driver_type == "chrome-headless":
#         # chrome headless模式
#         chrome_options = CH_Options()
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument('--disable-gpu')
#         chrome_options.add_argument("--window-size=1920x1080")
#         driver = webdriver.Chrome(options=chrome_options)
#
#     elif driver_type == "firefox-headless":
#         # firefox headless模式
#         firefox_options = FF_Options()
#         firefox_options.headless = True
#         driver = webdriver.Firefox(firefox_options=firefox_options)
#
#     elif driver_type == "grid":
#         # 通过远程节点运行
#         driver = Remote(command_executor='http://10.2.16.182:4444/wd/hub',
#                         desired_capabilities={
#                             "browserName": "chrome",
#                         })
#         driver.set_window_size(1920, 1080)
#
#     else:
#         raise NameError("driver驱动类型定义错误！")
#
#     return driver
#
#
# # 关闭浏览器
# @pytest.fixture(scope="session", autouse=True)
# def browser_close():
#     yield driver
#     driver.quit()
#     print("test end!")
#
#
# if __name__ == "__main__":
#     capture_screenshot("test_dir/test_baidu_search.test_search_python.png")