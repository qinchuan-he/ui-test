# coding = utf-8


from common.comfunction import execBrower
from test.smart_search import search_result


mode = 1
driver = execBrower(mode)
# User().login(driver)
# search_home().lately_collection(driver)
# search_home().my_subscribe(driver)
# search_home().my_annotation(driver)
# search_result().search(driver)
search_result().check_jmeter(driver,"http://192.168.1.49:8080/jmeter/report/index.html")
driver.quit()