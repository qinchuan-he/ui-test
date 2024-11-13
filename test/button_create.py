# coding = utf-8
import time
from time import sleep

from common.comfunction import OpenBrowser
from common.comfunction import User
from common.comfunction import com_xpath
from common.comfunction import url22

# 按钮功能造数据
# 参数


class create_buttonfunction(object):
    """ 按钮类功能造数据"""
    def create_share(self,driver,image_path=None,image_prefix=None):
        """ 分享造数据"""
        # 进入私有创建文件夹
        User().root_private(driver)
        sharefolder = "分享"+ str(time.time())  # 分享文件夹名字
        print(sharefolder)
        User().createFolder(driver,sharefolder)
        User().into_folder(driver,sharefolder)
        url =url22
        com_xpath().com_localupload(driver,url)
        if image_path:
            driver.get_screenshot_as_file(image_path+image_prefix+str(time.time())+".png")


mode = 2
driver = OpenBrowser(mode)
User().login(driver)
create_buttonfunction().create_share(driver)



