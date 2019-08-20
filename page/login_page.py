from poium import Page, PageElement, PageElements


class LoginPage(Page):
    switch_login = PageElement(xpath="//div[text()='账号登录']", describe="账号登录")
    user_input = PageElement(id_="username_no", describe="用户名输入")
    pwd_input = PageElement(id_="password", describe="密码输入")
    login_button = PageElement(xpath="//*[@id='root']/div/div/div[2]/div[1]/div[3]/div[2]/form/div[3]/div/div/span",
                               describe="登录")


    # search_input = PageElement(id_="kw", describe="搜索框")
    # search_button = PageElement(id_="su", describe="搜索按钮")
    # settings = PageElement(link_text="设置", describe="设置下拉框")
    # search_setting = PageElement(css=".setpref", describe="搜索设置选项")
    # save_setting = PageElement(css=".prefpanelgo", describe="保存设置")
    #
    # # 定位一组元素
    # search_result = PageElements(xpath="//div/h3/a", describe="搜索结果")