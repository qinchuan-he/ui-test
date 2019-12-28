# coding=utf-8

from common.newcomfunction import new_user
from test.upload_relate import upload_all

class Test_checkData:
    """ 数据检查"""
    def test_checkupload(self,browser,base_url,images_path):
        """ 检查上传功能和显示"""
        new_user().new_login(browser,base_url)
        driver = browser
        upload_all(driver,images_path,image_prefix='test_checkupload')

        # 增加分享和版本冲突验证





