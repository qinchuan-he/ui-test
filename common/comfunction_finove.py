# coding = utf-8
import os,sys

from pycparser.ply.yacc import token



curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)

import requests
import json
from datetime import datetime
from common.private import EmailProperty,UserProperty


# 获取用户相关参数
class User_Parameter:

    # 获取租户id,传入租户名称,PC端
    def get_tenants(self,tname=None):
        if not tname:
            tname = UserProperty().tenant_name
        url_S = UserProperty().url+"/api/services/app/Account/IsTenantAvailable"
        json_s = {"tenancyName":tname}
        res = requests.post(url=url_S,json=json_s)
        tenants_id = json.loads(res.text)["result"]["tenantId"]
        return tenants_id

    # 登录系统，获取token, 返回惊悚类型，传入model,不传是PC，1是desktop，2是APP,返回tenants_id,token
    def get_token(self,model=None):
        date_s = datetime.now()
        # print(date_s)
        if not model:
            url_s = UserProperty().url+"/api/TokenAuth/Authenticate"
            tenants_id = self.get_tenants()
            header_s = {"Content-Type": "application/json", "tenant": tenants_id}
            json_s = {"userNameOrEmailAddress": UserProperty().user, "password": UserProperty().pwd, "clientType": UserProperty().web}
            # print(json_s)
            res = requests.post(url=url_s,headers=header_s,json=json_s)
            token_s = json.loads(res.text)['result']['accessToken']
            token_s = "Bearer " + token_s
            results = {"tenants_id":tenants_id,"token":token_s}
            return results
        elif model==1:
            url_s = UserProperty().url + "/api/TokenAuth/ExternalLoginAuthenticate"
            # tenants_id = self.get_tenants()
            header_s = {"Content-Type": "application/json"}
            json_s = {"usernameOrEmailAddress":UserProperty().user,"password":UserProperty().pwd,"tenancyName":UserProperty().tenant_name,"clientType":UserProperty().client_type,"mac":UserProperty().client_name}
            # print(json_s)
            res = requests.post(url=url_s, headers=header_s, json=json_s)
            text_s = json.loads(res.text)
            tenants_id = text_s["result"]["data"]["tenantId"]
            token_s = text_s["result"]["accessToken"]
            token_s = "Bearer " + token_s
            result = {"tenants_id": tenants_id, "token": token_s}
            # print(type(results))
            result_json = json.dumps(result)
            # print(type(result_json))
            return result_json

# 芯片查询相关,传入token
class Rfid_Search:

    # 客户端资产查询,只支持单个芯片，查询到，返回芯片id,asset_data_id
    def search(self,token=None,rfid=None):
        # 数据不全返回空
        if not token or not rfid:
            return {}
        url_s = UserProperty().url + "/api/services/app/AssetsDataClient/QueryAssetsDataHistoryByTags"
        tenants_id =json.loads(token)["tenants_id"]
        token_s = json.loads(token)["token"]
        header_s = {"Content-Type": "application/json","tenant":tenants_id,"authorization":token_s }
        json_s = {"tagCodes":[rfid]}
        res = requests.post(url=url_s,headers=header_s,json=json_s)
        res_json = json.loads(res.text)
        # print(res_json)
        detail =res_json["result"]["detailNormalItems"]
        # not_normal = res_json["result"]["notNormalItems"]
        result = len(detail)
        if result==1:
            print("查询到")
            asset_data_id = res_json["result"]["detailNormalItems"][0]["assetsDataId"]
            asset_status = res_json["result"]["detailNormalItems"][0]["assetStatus"]
            asset_name = res_json["result"]["detailNormalItems"][0]["name"]
            result_s = {"asset_data_id":asset_data_id,"asset_name":asset_name,"asset_status":asset_status}
            # print(result_s)
            return result_s
        else:
            print("未注册")
            result_s = {}
            return result_s

    # 获取所有客户信息，传入客户名，未传参返回第一个
    def get_customer(self,token=None,name=None):
        if not token:
            return {}
        url_s = UserProperty().url + "/api/services/app/CustomerInfoClient/GetAllToClient?customerType=User"
        tenants_id =json.loads(token)["tenants_id"]
        token_s = json.loads(token)["token"]
        header_s = {"Content-Type": "application/json","tenant":tenants_id,"authorization":token_s }
        res = requests.get(url=url_s, headers=header_s)
        res_json = json.loads(res.text)["result"]
        if not name:
            return res_json[0]
        for i in res_json:
            if i["name"] == name:
                return i

    # 获取包信息，传入客户id和包名称，返回特定包信息，未传参返回第一条数据
    def get_package(self,token=None,customerId=None,name=None):
        if not token:
            return {}
        url_s = UserProperty().url + "/api/services/app/PackageFileClient/QueryPackageFiles"
        tenants_id =json.loads(token)["tenants_id"]
        token_s = json.loads(token)["token"]
        header_s = {"Content-Type": "application/json","tenant":tenants_id,"authorization":token_s }
        if not customerId:
            json_s = {"customerId":None,"lastNumber":None,"sterilization":None,"packageFileType":None,"pageSize":"500","pageNum":"1"}
        else:
            json_s = {"customerId":customerId,"lastNumber":None,"sterilization":None,"packageFileType":None,"pageSize":"500","pageNum":"1"}
        res = requests.post(url=url_s, headers=header_s,json=json_s)
        res_json = json.loads(res.text)["result"]["items"]
        if not name:
            return res_json[0]
        for i in res_json:
            if i["packageFileName"] == name:
                print(i)
                return i


    # 根据输入的用户名和组织返回对应json格式id（2个id）传入客户名和组织名
    def customer_search(self,token=None,customer_name=None,organize_name=None):
        if not token or not customer_name or not organize_name:
            return {}
        url_s = UserProperty().url + "/api/services/app/CustomerOrganizationClient/GetAllOrganizationUnitListToClient?customerType=User"
        tenants_id =json.loads(token)["tenants_id"]
        token_s = json.loads(token)["token"]
        header_s = {"Content-Type": "application/json","tenant":tenants_id,"authorization":token_s }
        res = requests.get(url=url_s,headers=header_s)
        res_json = json.loads(res.text)
        # print(res_json)
        # print(type(res_json))
        # 找到对应客户的id和组织,由于组织层级存在不一致性，使用递归迭代
        customer_list = res_json["result"]
        # 递归函数，查询组织(因为多组织且层级不一致),传入组织信息是list
        def find_organize(node_list,o_name):
            for i in node_list:
                if i["name"]==o_name:
                    # 找到组织，返回(客户下组织唯一性)组织id
                    return i
                # 如果该层级目录存在children键且为真值([]、None、0 或任何其他被视为布尔 False 的值)
                if i["children"]:
                    found = find_organize(i["children"], o_name)
                    if found:
                        return found
        for i in customer_list:
            name = i["name"]
            # 找到对应客户
            if name == customer_name:
                # print(name)
                customer_id = i["id"]
                # print(customer_id)
                child_json = i["children"]
                # print("child_json : {}".format(type(child_json)))
                # print(child_json)
                # 找到客户，开始找客户下组织，调用递归函数
                organize_list = find_organize(child_json,organize_name)
                organize_id = organize_list["id"]
                return {"customer_id":customer_id,"organization_id":organize_id}

    # 查询收货类型,根据传入类型返回对应id,json形式,未传参数返回第一个
    def get_receive_type(self,token=None,receive_type=None):
        if not token:
            return {}

        url_s = UserProperty().url + "/api/services/app/InvoiceReceiveTypeClient/GetInvoiceReceiveType"
        tenants_id = json.loads(token)["tenants_id"]
        token_s = json.loads(token)["token"]
        header_s = {"Content-Type": "application/json", "tenant": tenants_id, "authorization": token_s}
        # 未传类型默认第一个类型
        if not receive_type:
            res = requests.get(url=url_s,headers=header_s)
            json_s = json.loads(res.text)
            # 返回第一个类型
            return json_s["result"][0]

        res = requests.get(url=url_s,headers=header_s)

        json_s = json.loads(res.text)
        for i in json_s["result"]:
            if i["receiveTypeName"] == receive_type:
                return i

    # 查询计件人信息，未传姓名返回第一个
    def get_piece_person(self,token=None,name=None):
        if not token:
            return {}
        url_s = UserProperty().url + "/api/services/app/PieceworkClient/QueryPiecework"
        tenants_id = json.loads(token)["tenants_id"]
        token_s = json.loads(token)["token"]
        header_s = {"Content-Type": "application/json", "tenant": tenants_id, "authorization": token_s}
        json_s = {}
        res = requests.post(url=url_s,headers=header_s,json=json_s)
        # print(res.text)
        res_json = json.loads(res.text)["result"]
        print(res_json)
        # 如果没有传入name返回第一条数据
        if not name:
            return res_json[0]
        for i in res_json:
            if i["pieceworkName"] == name:
                return i




# 芯片操作，收发货
class Rfid_Operate:

    # 发货
    def send_rfid(self,token=None,send_list=None):
        if not token or not send_list:
            return {}
        p_list = send_list

        url_s = UserProperty().url + "/api/services/app/InvoiceClient/Deliver"
        tenants_id =json.loads(token)["tenants_id"]
        token_s = json.loads(token)["token"]
        header_s = {"Content-Type": "application/json","tenant":tenants_id,"authorization":token_s }
        json_s = {"invoiceDetailIds":[],"assetsDataIds":[p_list["assetsDataIds"]],"customerId":p_list["customerId"],"customerOrganizationId":p_list["customerOrganizationId"]}
        res = requests.post(url=url_s,headers=header_s,json=json_s)
        res_json = json.loads(res.text)
        print(res_json)
    # 收货
    def recevie_rfid(self,token=None,recevie_list=None):
        if not token or not recevie_list:
            return {}
        url_s = UserProperty().url + "/api/services/app/InvoiceClient/Receive"
        tenants_id = json.loads(token)["tenants_id"]
        token_s = json.loads(token)["token"]
        header_s = {"Content-Type": "application/json", "tenant": tenants_id, "authorization": token_s}
        json_s = {"customerId":recevie_list["customerId"],"customerOrganizationId":recevie_list["customerOrganizationId"],"invoiceReceiveTypeId":recevie_list["invoiceReceiveTypeId"],"assetsDataIds":[recevie_list["assetsDataIds"]],"remark":""}
        res = requests.post(url=url_s,headers=header_s,json=json_s)
        res_json = res.text
        print(res_json)

# 包相关操作
class Rfid_Package:

    # 打包
    def create_package(self,token=None,package_list=None):
        if not token or not package_list:
            return {}
        url_s = UserProperty().url + "/api/services/app/PackageFileClient/QueryPackageFiles"
        tenants_id = json.loads(token)["tenants_id"]
        token_s = json.loads(token)["token"]
        header_s = {"Content-Type": "application/json", "tenant": tenants_id, "authorization": token_s}
        json_s = {"packageFileId":"08","sterilizationDate":"20","expiringDate":"20","packerId":package_list["packerId"],"checkerId":package_list["checkerId"],"customerId":package_list["customerId"],"assetsDataIds":[package_list["assetsDataIds"]],"count":None}
        res = requests.post(url=url_s,headers=header_s,json=json_s)
        print(res.text)




def check_1():
    tokens = User_Parameter().get_token(1)
    rfid = "E2806995000050061A757D42"
    receive_type = "常规"
    # # rfid = "E2806995000040084E44E9BC"
    # rfid_info = Rfid_Search().search(token=tokens,rfid=rfid)
    # customer_list = Rfid_Search().customer_search(token=tokens,customer_name="明心医院",organize_name="内科")
    # send_list2 = {"assetsDataIds":rfid_info["asset_data_id"],"customerId":customer_list["customer_id"],"customerOrganizationId":customer_list["organization_id"]}
    # # 发货
    # res = Rfid_Operate().send_rfid(token=tokens,send_list=send_list2)

    # Rfid_Search().get_receive_type(token=tokens,receive_type=receive_type)
    # print("---------------")
    # Rfid_Search().get_piece_person(token=tokens,name="计件人666")
    Rfid_Search().get_package(token=tokens,customerId="08dcd140-ba50-4b5e-8e76-6444eeb80852",name="一个芯片RFID包")


if __name__=="__main__":
    # user_parameter().get_token(1)
    check_1()

