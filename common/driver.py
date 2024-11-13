from selenium import webdriver

def driver():
    path = r"C:\2services\driver\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://ym-fat.lctest.cn/index.html?r=27396&i18n=ssssss")
    return driver