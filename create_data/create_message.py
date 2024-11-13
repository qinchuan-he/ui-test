
import requests
from common.private import UserProperty,InterBaseUrl
from common.comInterfaceUrl import InterfaceUrl
import time
from time import sleep
import json
from common.comfunction import url22
from common.decode import cyprex_decode
# 强提醒数据，用户A和B


# 新建代办事项

def getCookie(user):
    """ 获取cookie方法"""
    argument = {'type':'account','username_no':user,'passwd':'Test123456','validCode':'','inviteCode':'','userId':''
        ,'teamId':'','source':'3001','session_duration':'31536000','auto_login':'1'}
    print(InterBaseUrl().Base_url+InterfaceUrl().login)
    login = requests.post(InterBaseUrl().Base_url+InterfaceUrl().login,data=argument)
    print(login.text)
    print(login.cookies)
    print(requests.utils.dict_from_cookiejar(login.cookies))
    cookie_value = login.cookies[InterBaseUrl().session_key]
    cookie = {InterBaseUrl().session_key:cookie_value}
    id = json.loads(login.text).get('data').get('id')
    return cookie,id  # 发现整个流程这里返回数组比字典{'cookie':cookie,'id':id}速度要快，但是还是没有只返回cookie的速度快

def createRemindMyself(url,argument,user):
    """ 提醒当前用户,新建代办事项"""
    r = requests.post(url,data=argument,cookies=user[0])
    return r

def createTeamMessage(user1,user2 = None,dismiss=None):
    """ 团队消息：传入两个用户信息
        1.用户1创建团队，邀请用户2加入团队（站内邀请），站内成员加入,成员退出，成员再次加入
        2.成员被设置成访客，成员被设置成成员，移交管理员权限，
        3.踢出成员（原管理员），解散团队
        用户1收到消息：成员加入，退出，被踢出团队，团队解散
        用户2收到消息：角色变换（成员+访客），移交管理员，
    """
    # 创建团队
    url = InterBaseUrl().Base_url+InterfaceUrl().team_form
    argument  = {'name':'脚本'+str(time.time()),'default_permission':'1'}
    r = requests.post(url,data=argument,cookies=user1[0])
    print(json.loads(r.text).get('msg'))
    team_id = json.loads(r.text).get('data').get('id')

    # 邀请成员
    url_3 = InterBaseUrl().Base_url+InterfaceUrl().team_invite
    argument_3 ={'dst_team_id':team_id,'member_id':user2[1]}
    res_invite = requests.post(url_3,data=argument_3,cookies = user1[0])
    print(eval(res_invite.text).get('msg'))
    sleep(2)

    # 用户2加入团队
    url_4 = InterBaseUrl().Base_url+InterfaceUrl().message
    res_msg = requests.get(url_4,cookies = user2[0])
    url_5 = InterBaseUrl().Base_url+json.loads(res_msg.text).get('data').get('ait_message').get('message_list')[0].get('obj_text')
    res_accept = requests.get(url_5,cookies = user2[0])
    print(eval(res_accept.text).get('msg'))

    # 用户2,退出团队
    sleep(1)
    url_6 = InterBaseUrl().Base_url+InterfaceUrl().team_quit
    argument_4={'teamId':team_id,'opt_type':'01'}
    res_quit = requests.post(url_6,data=argument_4,cookies = user2[0])
    print(eval(res_quit.text).get('msg'))

    # 用户2 ，再次加入团队
    sleep(1)
    url_4 = InterBaseUrl().Base_url+InterfaceUrl().message
    res_msg = requests.get(url_4,cookies = user2[0])
    url_5 = InterBaseUrl().Base_url+json.loads(res_msg.text).get('data').get('ait_message').get('message_list')[0].get('obj_text')
    res_accept = requests.get(url_5,cookies = user2[0])
    print(eval(res_accept.text).get('msg'))

    # 用户1设置用户2权限,访客
    sleep(2)
    url_7 = InterBaseUrl().Base_url+InterfaceUrl().team_role
    argument_5={'team_id':team_id,'member_id_list':str([user2[1]]),'role':'00'}
    res_role = requests.post(url_7,data=argument_5,cookies = user1[0])
    print(eval(res_role.text).get('msg'))

    # 用户1设置用户2权限，成员
    sleep(2)
    argument_6 = {'team_id': team_id, 'member_id_list': str([user2[1]]),
                  'role': '01'}  # 根据member_id_list = json.loads(request.POST.get('member_id_list', "[]"))判断这里是把数组转成string了
    res_role = requests.post(url_7, data=argument_6, cookies=user1[0])
    print(eval(res_role.text).get('msg'))

    # 用户1把权限移交给用户2，移交管理员
    sleep(2)
    url_8 = InterBaseUrl().Base_url+InterfaceUrl().team_admin
    argument_7 = {'team_id':team_id,'member_id':user2[1],'action':'transfer'}
    res_admin = requests.post(url_8,data=argument_7,cookies=user1[0])
    print(eval(res_admin.text).get('msg'))

    # 用户1和用户2互相发消息
    url_11 = InterBaseUrl().Base_url+InterfaceUrl().team_sendmsg
    argument_9={'team_id':team_id,'member_list':str([user2[1]]),'content':'来自脚本的消息2,来自脚本的消息2来自脚本的消息2,来自脚本的消息2,来自脚本的消息2'}
    res_sendmsg2 = requests.post(url_11,data=argument_9,cookies=user1[0])
    print(eval(res_sendmsg2.text).get('msg'))
    argument_9 = {'team_id':team_id,'member_list':str([user1[1]]),'content':'来自脚本的消息来自脚本的消息11,来自脚本的消息1,来自脚本的消息1,来自脚本的消息1'}
    res_sendmsg1 = requests.post(url_11,data=argument_9,cookies=user2[0])
    print(eval(res_sendmsg1.text).get('msg'))

    # 用户2把用户1踢掉
    sleep(1)
    url_9 = InterBaseUrl().Base_url+InterfaceUrl().team_remove
    argument_8 = {'teamId':team_id,'uids':str([user1[1]]),'opt_type':'01'}
    res_remove = requests.post(url_9,data=argument_8,cookies=user2[0])
    print(eval(res_remove.text).get('msg'))

    # 用户2解散项目,dismiss参数控制
    if team_id and dismiss:
        # 解散团队
        url_2 = InterBaseUrl().Base_url+InterfaceUrl().team_dismiss
        argument_2 = {'teamId':team_id}
        r = requests.post(url_2,data=argument_2,cookies = user2[0])
        print(eval(r.text).get('msg'))

def createTeamTaskMessage(user1,user2):
    """ 团队任务提醒+文件分享批注提醒，传入两个用户信息
        第1个用户，团队任务，新建（3个），两个进行中，一个修订中，分别设置时间，转交编辑，转交修订
        第1个用户团队上传文件，批注@第二个用户
        第1个用户，私有找一个文件，分享给第2个用户
    """
    # 创建团队
    url = InterBaseUrl().Base_url + InterfaceUrl().team_form
    argument = {'name': '2脚本' + str(time.time()), 'default_permission': '1'}
    r = requests.post(url, data=argument, cookies=user1[0])
    print(json.loads(r.text).get('msg'))
    team_id = json.loads(r.text).get('data').get('id')

    # 邀请成员
    url_3 = InterBaseUrl().Base_url+InterfaceUrl().team_invite
    argument_3 ={'dst_team_id':team_id,'member_id':user2[1]}
    res_invite = requests.post(url_3,data=argument_3,cookies = user1[0])
    print(eval(res_invite.text).get('msg'))
    sleep(2)

    # 用户2加入团队
    url_4 = InterBaseUrl().Base_url+InterfaceUrl().message
    res_msg = requests.get(url_4,cookies = user2[0])
    url_5 = InterBaseUrl().Base_url+json.loads(res_msg.text).get('data').get('ait_message').get('message_list')[0].get('obj_text')
    res_accept = requests.get(url_5,cookies = user2[0])
    print(eval(res_accept.text).get('msg'))

    # 私有分享文件到团队，带消息.先上传文件.现在写死参数（300）
    url_2 = InterBaseUrl().Base_url+InterfaceUrl().upload_whole
    file_name = '脚本'+str(time.time())+'.pdf'
    argument_2 = {'file_info': str({'name':file_name}).replace("'",'"')}
    file = {'file':open(url22,'rb')}
    res_upload = requests.post(url_2,data=argument_2,cookies = user1[0],files = file)
    file_id = json.loads(res_upload.text).get('data').get('meta_info').get('id')
    print('上传文件成功')
        # 分享到团队
    url_6 =InterBaseUrl().Base_url+InterfaceUrl().file_share
    file_list = [{"id":file_id,"type":"info","name":file_name,"contentType":300}]
    textmsg = '这是来自脚本的消息,这是来自脚本的消息,这是来自脚本的消息,这是来自脚本的消息'
    team_list=cyprex_decode(team_id)
    argument_4 = {'src_list':str(file_list).replace("'",'"'),'team_id_list':str([team_list]),'shareAnno':'true','isShareAssociate':'false','needSendMessage':'false','messageText':textmsg}
    res_share = requests.post(url_6,data=argument_4,cookies = user1[0])
    print(json.loads(res_share.text).get('msg'))
        # 分享给个人
    url_7 = InterBaseUrl().Base_url+InterfaceUrl().share_user
    argument_5 = {'resource_id':file_id,'share_type':'0','auth_code':'','valid_time_type':'','opt_type':'1','member_ids':str([user2[1]]),'team_id':team_id}
    res_share_user = requests.post(url_7,data=argument_5,cookies=user1[0])
    if json.loads(res_share_user.text).get('msg')=='success':
        print('分享到个人成功')

    # 团队文件中增加批注
        # 获取文件列表
    url_8 = InterBaseUrl().Base_url+InterfaceUrl().team_list+'?teamId='+str(team_id)+'&ordering=-utime&include=infoCat' \
                                                           '&include=info&include=cooperation&include=cooperationCat&pageRow=50'
    res_teamlist = requests.get(url_8,cookies=user1[0])
    team_fileid = json.loads(res_teamlist.text).get('data').get('list')[0].get('id')
        # 添加批注@
    url_9 = InterBaseUrl().Base_url+InterfaceUrl().add_annotation
    text='@所有成员  这是来自脚本的批注'
    argument_6 = {'res_id':team_fileid,'content':text,'uids':str([user2[1]])}
    res_annotation = requests.post(url_9,data=argument_6,cookies=user1[0])
    print(json.loads(res_annotation.text).get('msg'))

    # 团队内新建协作空间并且，设置提醒
        # 新建协作空间
    url_11 = InterBaseUrl().Base_url+InterfaceUrl().create_space
    content = [{"id":"","name":"我的协作空间"+str(time.time()),"teamId":team_id,"type":"cooperationCat"}]
    argument_7 = {'catList':str(content).replace("'",'"')}
    res_space = requests.post(url_11,argument_7,cookies=user1[0])
    space_id = json.loads(res_space.text).get('data').get('list')[0].get('id')
    print(json.loads(res_space.text).get('msg'))
        #   创建任务,并设置提醒时间
    url_12 = InterBaseUrl().Base_url+InterfaceUrl().create_mission
    mission_name = '脚本任务'+str(time.time())+'.docx'
    dead_line = time.strftime("%Y-%m-%d %H:%M",time.localtime(time.time()+930))
    mission_list=[]
    for i in range(4):
        argument_8 = {'name':mission_name,'pId':space_id,'description':'','executor_id':'','dead_line':dead_line,'remind_minute':'15'}
        res_mission = requests.post(url_12,argument_8,cookies=user1[0])
        mission_list.append(json.loads(res_mission.text).get('data').get('id'))
    print('创建任务完成')

         # 认领两个任务
    url_13 = InterBaseUrl().Base_url+InterfaceUrl().update_mission
    argumen_9 = {'oId':mission_list[1],'executor_id':user1[1],'mission_status':'2','current_status':'1'}
    argumen_11 = {'oId': mission_list[2], 'executor_id': user1[1], 'mission_status': '3', 'current_status': '1'}
    requests.post(url_13,argumen_9,cookies=user1[0])
    requests.post(url_13, argumen_11, cookies=user1[0])
    print('任务认领完成')

        # 转交任务
    sleep(1.5)
    argumen_12 = {'oId': mission_list[1], 'executor_id': user2[1], 'mission_status': '2', 'current_status': '2'}
    argumen_13 = {'oId': mission_list[2], 'executor_id': user2[1], 'mission_status': '3', 'current_status': '3'}
    requests.post(url_13,argumen_12,cookies=user1[0])
    requests.post(url_13, argumen_13, cookies=user1[0])
    print('任务转交完成')


if __name__ == '__main__':
    user1 = getCookie(UserProperty().user)
    user2 = getCookie(UserProperty().create_u2)
    # cookie = user1[0]
    # user1_id = user1[1]
    url = InterBaseUrl().Base_url+InterfaceUrl().remindMyself

    t = time.strftime("%Y-%m-%d %H:%M",time.localtime(time.time()+61))
    argument = {'remind_time': t, 'content': '调用接口创建'}
    r = createRemindMyself(url,argument,user1) # 创建代办事项
    print('创建代办事项成功')


    createTeamMessage(user1,user2) #  团队相关消息
    createTeamTaskMessage(user1,user2) # 任务和文件分享，批注提醒
    # test(user1)














