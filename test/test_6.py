from common.comfunction import  *


driver = OpenBrowser(mode=2)
User().login()
sharefolder = "分享" + str(time.time())  # 分享文件夹名字
print(sharefolder)
User().createFolder(folder=sharefolder)
User().into_folder(driver, sharefolder)






