# coding=utf-8
import os
import time
import logging
import pytest
import shutil
# from conftest import *
from conftest import REPORT_DIR
from conftest import cases_path, rerun, max_fail
from conftest import history_save

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python3 run_tests.py  (回归模式，生成HTML报告)
  > python3 run_tests.py -m debug  (调试模式)
'''
print("REPORT_DIR "+REPORT_DIR)

# cases_path = "./test_dir/"
# rerun = "3"
# max_fail = "5"
def init_env(now_time):
    """
    初始化测试报告目录
    """
    if history_save==1:
        os.mkdir(os.path.join(REPORT_DIR,now_time))
        os.mkdir(os.path.join(REPORT_DIR,now_time,"image"))
    else:
        if not os.path.exists(os.path.join(REPORT_DIR,"image")):
            os.mkdir(os.path.join(REPORT_DIR,"image"))
        else:
            shutil.rmtree(os.path.join(REPORT_DIR,"image"),ignore_errors=True)
            os.mkdir(os.path.join(REPORT_DIR,"image"))

# 增加一个后置方法，为了访问报告用
def teardown_module():
    print("-----------------------------------------后置方法")


# @click.command()
# @click.option('-m', default=None, help='输入运行模式：run 或 debug.')
def run(m):
    print("m "+m)
    if m is None or m == "run":
        logger.info("回归模式，开始执行✈✈！")
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        init_env(now_time)
        if history_save==1:   # 保留历史记录
            html_report = os.path.join(REPORT_DIR, now_time, "report.html")
            xml_report = os.path.join(REPORT_DIR, now_time, "junit-xml.xml")
        else:
            html_report = os.path.join(REPORT_DIR, "report.html")
            xml_report = os.path.join(REPORT_DIR, "junit-xml.xml")
        pytest.main(["-s", "-v",
                    # "test_dir/test_rubbish.py",
                     cases_path,
                     "--html=" + html_report,
                     "--junit-xml=" + xml_report,
                     "--self-contained-html",
                     "--maxfail", max_fail,
                     "--reruns", rerun])
        logger.info("运行结束，生成测试报告♥❤！")
    elif m == "debug":
        print("debug模式，开始执行！")
        pytest.main(["-v", "-s", cases_path])
        print("运行结束！！")


if __name__ == '__main__':
    run("run")