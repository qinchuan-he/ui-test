
from common.comfunction import OpenBrowser,User
from common.private import UserProperty

# 加入碎片检查

def check_frag():
    """"""
    mode = 2
    driver = OpenBrowser(mode)
    User().login(driver,UserProperty.create_u1)
    driver.get()


if __name__=="__main__":
    check_frag()





