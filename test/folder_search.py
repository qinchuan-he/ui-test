

from common.comfunction import *
from selenium.webdriver.common.action_chains import ActionChains
from common.comparameter import symbol

def check_foldersearch():
    """ 文件夹内搜索，特殊字符检查"""
    mode = 2
    driver = OpenBrowser(mode,5)
    User().login(driver)

    for i in symbol().english:
        if i == '*' or i == '('or i == ')'or i == '+'or i == '?'or i == '\\':
            continue
        try:
            el = driver.find_element_by_xpath("//input[@placeholder='请输入关键词']")
            for j in range(7):
                el.send_keys(Keys.BACK_SPACE)
            el.clear()
            # el.send_keys('txt')
            el.send_keys(i)
            driver.switch_to.active_element.send_keys(Keys.ENTER)
            sleep(3)
            driver.find_element_by_xpath("//div[text()='搜索结果']")
        except Exception as e:
            print("搜索出错-关键字：")
            print(i)
            break
    CloseBrowsers()


if __name__ == "__main__":
    check_foldersearch()











