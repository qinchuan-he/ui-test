
class InterfaceUrl(object):
    # Base_url = 'https://cyprexsvc.fir.ai'
    login = '/account/user/signin/'  # post {'type':'account','username_no':user,'passwd':'Test123456','validCode':'','inviteCode':'','userId':'','teamId':''}
    remindMyself = '/message/document/remindMyself/' # post
    team_form = '/group/team/form/' # post 团队新建，重命名相关接口
    team_dismiss='/group/team/dismiss/' # post 解散团队
    team_invite = '/group/team/invite/' # post 发送邀请加入团队
    team_invite_accept = '/group/team/invite/validation/' # get 加入团队接口,这个接口从消息中获取url
    message = '/message/myMessage/list/?page=1&pageRow=10' # get 获取消息
    team_quit = '/group/team/quit/' # post 退出项目
    team_role ='/group/team/member/role/' #post 设置成员角色
    team_admin = '/group/team/admin/' #post 移交管理员权限
    team_remove = '/group/team/remove/' # post 团队踢出成员
    team_sendmsg = '/message/sendToMember/' # post 团队成员发送消息
    team_list = '/resource/group/list/' # post 团队列表

    upload_whole = '/resource/upload/whole/' # post 上传文件,小文件
    file_share = '/resource/personal/share/' # post 文件分享接口
    share_user = '/resource/external/share/' # post 文件分享到个人
    add_annotation = '/resource/annotation/add/' # post 添加批注

    create_space = '/resource/merge/form/' # post 添加团队协作空间
    create_mission = '/office/mission/create/' # post 新建任务
    update_mission = '/office/mission/update/' # 认领任务













