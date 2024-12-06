# coding=utf-8

from datetime import datetime

import requests
import json
import os,sys
import time


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)

from common.private import EmailProperty,UserProperty
from common.comfunction import send_mail

# 检查权限列表
def check_menulist():
    # 检查时间点
    date_s = datetime.now()
    print(date_s)
    # 设置权限列表，更新与2024-12-04
    s_menu_list = ['Pages', 'Pages.Tenant.Dashboard', 'Pages.CustomerManager', 'Pages.CustomerManager.CirculateGroup', 'Pages.CustomerManager.CirculateGroup.Create', 'Pages.CustomerManager.CirculateGroup.Edit', 'Pages.CustomerManager.CirculateGroup.Delete', 'Pages.CustomerManager.CirculateGroup.Query', 'Pages.CustomerInfo.Node', 'Pages.CustomerInfo.Query', 'Pages.CustomerInfo.Create', 'Pages.CustomerInfo.Edit', 'Pages.CustomerInfo.Delete', 'Pages.CustomerInfo.BatchDelete', 'Pages.CustomerInfo.ExportExcel', 'Pages.CustomerInfo.ComboboxItems', 'Pages.CustomerOrganization.Node', 'Pages.CustomerOrganization.Query', 'Pages.CustomerOrganization.Create', 'Pages.CustomerOrganization.Edit', 'Pages.CustomerOrganization.Delete', 'Pages.CustomerOrganization.ExportExcel', 'Pages.JobPosition.Node', 'Pages.JobPosition.Query', 'Pages.JobPosition.Create', 'Pages.JobPosition.Edit', 'Pages.JobPosition.Delete', 'Pages.JobPosition.BatchDelete', 'Pages.JobPosition.ExportExcel', 'Pages.CustomerManager.Employee.Node', 'Pages.CustomerManager.Employee.Query', 'Pages.CustomerManager.Employee.Create', 'Pages.CustomerManager.Employee.Edit', 'Pages.CustomerManager.Employee.Delete', 'Pages.CustomerManager.Employee.Depart', 'Pages.CustomerManager.Employee.BatchDelete', 'Pages.CustomerManager.Employee.ExportExcel', 'Pages.CustomerManager.Employee.ImportExcel', 'Pages.Warehouse.Node', 'Pages.Warehouse.Query', 'Pages.Warehouse.Create', 'Pages.Warehouse.Edit', 'Pages.Warehouse.Delete', 'Pages.Warehouse.BatchDelete', 'Pages.Warehouse.ExportExcel', 'Pages.CustomerManager.Manufacturer.Node', 'Pages.CustomerManager.Manufacturer.Query', 'Pages.CustomerManager.Manufacturer.Create', 'Pages.CustomerManager.Manufacturer.Edit', 'Pages.CustomerManager.Manufacturer.Delete', 'Pages.CustomerManager.Manufacturer.BatchDelete', 'Pages.CustomerManager.Manufacturer.ExportExcel', 'Pages.Piecework.Node', 'Pages.Piecework.Query', 'Pages.Piecework.Create', 'Pages.Piecework.Edit', 'Pages.Piecework.Delete', 'Pages.Piecework.BatchDelete', 'Pages.Piecework.ExportExcel', 'Pages.CustomerManager.BusinessScenario.Node', 'Pages.CustomerManager.BusinessScenario.Query', 'Pages.CustomerManager.BusinessScenario.Create', 'Pages.CustomerManager.BusinessScenario.Edit', 'Pages.CustomerManager.BusinessScenario.Delete', 'Pages.CustomerManager.BusinessScenario.Copy', 'Pages.CustomerManager.BusinessScenario.Permissions', 'Pages.CustomerManager.PrintTemplate.Node', 'Pages.CustomerManager.PrintTemplate.Query', 'Pages.CustomerManager.PrintTemplate.Create', 'Pages.CustomerManager.PrintTemplate.Edit', 'Pages.CustomerManager.PrintTemplate.Delete', 'Pages.CustomerManager.PrintTemplate.BatchDelete', 'Pages.CustomerManager.PrintTemplate.ExportExcel', 'Pages.CustomerManager.PrintTemplate.ImportExcel', 'Pages.CustomerManager.PrintTemplate.Copy', 'Pages.CustomerManager.PrintTemplate.PermanentlyDelete', 'Pages.DevicesManager', 'Pages.DevicesManager.Sterilizer.Node', 'Pages.DevicesManager.Sterilizer.Query', 'Pages.DevicesManager.Sterilizer.Create', 'Pages.DevicesManager.Sterilizer.Edit', 'Pages.DevicesManager.Sterilizer.Delete', 'Pages.DevicesManager.Sterilizer.BatchDelete', 'Pages.DevicesManager.Sterilizer.ExportExcel', 'Pages.BasicDataManager', 'Pages.BasicDataManager.Alias', 'Pages.BasicDataManager.Alias.Query', 'Pages.BasicDataManager.Alias.Edit', 'Pages.BasicDataManager.SortingGrid', 'Pages.BasicDataManager.SortingGrid.Query', 'Pages.BasicDataManager.SortingGrid.Create', 'Pages.BasicDataManager.SortingGrid.Edit', 'Pages.BasicDataManager.SortingGrid.Delete', 'Pages.BasicDataManager.SortingGrid.Active', 'Pages.BasicDataManager.SortingGrid.Settings', 'Pages.BasicDataManager.AssetsClass.Node', 'Pages.BasicDataManager.AssetsClass.Query', 'Pages.BasicDataManager.AssetsClass.Create', 'Pages.BasicDataManager.AssetsClass.Edit', 'Pages.BasicDataManager.AssetsClass.Delete', 'Pages.BasicDataManager.AssetsClass.BatchDelete', 'Pages.BasicDataManager.AssetsClass.ExportExcel', 'Pages.BasicDataManager.Assets.Node', 'Pages.BasicDataManager.Assets.Query', 'Pages.BasicDataManager.Assets.Create', 'Pages.BasicDataManager.Assets.Edit', 'Pages.BasicDataManager.Assets.Delete', 'Pages.BasicDataManager.Assets.BatchDelete', 'Pages.BasicDataManager.Assets.ExportExcel', 'Pages.BasicDataManager.Assets.ImportExcel', 'Pages.BasicDataManager.Assets.Copy', 'Pages.BasicDataManager.AssetAttributes.Node', 'Pages.BasicDataManager.AssetAttributes.Query', 'Pages.BasicDataManager.AssetAttributes.Create', 'Pages.BasicDataManager.AssetAttributes.Edit', 'Pages.BasicDataManager.AssetAttributes.Delete', 'Pages.BasicDataManager.AssetAttributes.ExportExcel', 'Pages.BasicDataManager.AssetAttributes.Enabled', 'Pages.BasicDataManager.AssetAttributes.Detail.Create', 'Pages.BasicDataManager.AssetAttributes.Detail.Edit', 'Pages.BasicDataManager.AssetAttributes.Detail.Enabled', 'Pages.BasicDataManager.AssetAttributes.Detail.Delete', 'Pages.BasicDataManager.AssetAttributes.Detail.Order', 'Pages.BasicDataManager.AssetAttributes.Order', 'Pages.BasicDataManager.PackageFile.Node', 'Pages.BasicDataManager.PackageFile.Query', 'Pages.BasicDataManager.PackageFile.Create', 'Pages.BasicDataManager.PackageFile.Edit', 'Pages.BasicDataManager.PackageFile.Delete', 'Pages.BasicDataManager.PackageFile.BatchDelete', 'Pages.BasicDataManager.PackageFile.ExportExcel', 'Pages.InvoiceReceiveType.Node', 'Pages.InvoiceReceiveType.Query', 'Pages.InvoiceReceiveType.Create', 'Pages.InvoiceReceiveType.Edit', 'Pages.InvoiceReceiveType.Delete', 'Pages.InvoiceReceiveType.BatchDelete', 'Pages.InvoiceReceiveType.ExportExcel', 'Pages.BasicDataManager.LampInspectionParam.Node', 'Pages.BasicDataManager.LampInspectionParam.Query', 'Pages.BasicDataManager.LampInspectionParam.Create', 'Pages.BasicDataManager.LampInspectionParam.Edit', 'Pages.BasicDataManager.LampInspectionParam.Delete', 'Pages.BasicDataManager.LampInspectionParam.BatchDelete', 'Pages.BasicDataManager.LampInspectionParam.ExportExcel', 'Pages.BasicDataManager.SterilizerData.Node', 'Pages.BasicDataManager.SterilizerData.Query', 'Pages.BasicDataManager.SterilizerData.Create', 'Pages.BasicDataManager.SterilizerData.Edit', 'Pages.BasicDataManager.SterilizerData.Delete', 'Pages.BasicDataManager.SterilizerData.BatchDelete', 'Pages.BasicDataManager.SterilizerData.ExportExcel', 'Pages.BasicDataManager.ScrapParam.Node', 'Pages.BasicDataManager.ScrapParam.Query', 'Pages.BasicDataManager.ScrapParam.Create', 'Pages.BasicDataManager.ScrapParam.Edit', 'Pages.BasicDataManager.ScrapParam.Delete', 'Pages.BasicDataManager.ScrapParam.BatchDelete', 'Pages.BasicDataManager.ScrapParam.ExportExcel', 'Pages.BasicDataManager.TraceConfig.Node', 'Pages.BasicDataManager.TraceConfig.Query', 'Pages.BasicDataManager.TraceConfig.Edit', 'Pages.BasicDataManager.AssetsManageTag.Node', 'Pages.BasicDataManager.AssetsManageTag.Query', 'Pages.BasicDataManager.AssetsManageTag.Create', 'Pages.BasicDataManager.AssetsManageTag.Edit', 'Pages.BasicDataManager.AssetsManageTag.Delete', 'Pages.BasicDataManager.AssetsManageTag.BatchDelete', 'Pages.BasicDataManager.AssetsManageTag.ExportExcel', 'Pages.OrderManager', 'Pages.OrderManager.PurchaseOrder.Node', 'Pages.OrderManager.PurchaseOrder.Query', 'Pages.OrderManager.PurchaseOrder.Create', 'Pages.OrderManager.PurchaseOrder.Edit', 'Pages.OrderManager.PurchaseOrder.Delete', 'Pages.OrderManager.PurchaseOrder.BatchDelete', 'Pages.OrderManager.PurchaseOrder.ExportExcel', 'Pages.OrderManager.WashingOrder.Node', 'Pages.OrderManager.WashingOrder.Query', 'Pages.OrderManager.WashingOrder.Create', 'Pages.OrderManager.WashingOrder.Edit', 'Pages.OrderManager.WashingOrder.Delete', 'Pages.OrderManager.WashingOrder.BatchDelete', 'Pages.OrderManager.WashingOrder.ExportExcel', 'Pages.OperateManager', 'Pages.OperateManager.PackageProductionScheduling', 'Pages.OperateManager.PackageProductionScheduling.Query', 'Pages.OperateManager.PackageProductionScheduling.Print', 'Pages.OperateManager.PackageProductionScheduling.ProductionScheduling', 'Pages.OperateManager.PackageProductionScheduling.PackProductionScheduling', 'Pages.OperateManager.Sign', 'Pages.OperateManager.Sign.Query', 'Pages.OperateManager.Sign.Create', 'Pages.OperateManager.Scrap', 'Pages.OperateManager.Scrap.Query', 'Pages.OperateManager.Scrap.Create', 'Pages.OperateManager.Lose', 'Pages.OperateManager.Lose.Query', 'Pages.OperateManager.Lose.Create', 'Pages.OperateManager.OperationTrace', 'Pages.OperateManager.OperationTrace.Query', 'Pages.OperateManager.OperationTrace.Repeal', 'Pages.OperateManager.OperationTrace.PermanentlyLost', 'Pages.OperateManager.OperationTrace.Commit', 'Pages.ReportStatistics', 'Pages.RegistnSum.Node', 'Pages.RegistnSum.Query', 'Pages.Receive.Node', 'Pages.Receive.Query', 'Pages.Send.Node', 'Pages.Send.Query', 'Pages.Administration', 'Pages.Administration.Roles', 'Pages.Administration.Roles.Query', 'Pages.Administration.Roles.Create', 'Pages.Administration.Roles.Edit', 'Pages.Administration.Roles.Delete', 'Pages.Administration.Users', 'Pages.Administration.Users.Query', 'Pages.Administration.Users.Create', 'Pages.Administration.Users.Edit', 'Pages.Administration.Users.Delete', 'Pages.Administration.Users.BatchDelete', 'Pages.Administration.Users.ChangePermissions', 'Pages.Administration.Users.Impersonation', 'Pages.Administration.Users.ResetPassword', 'Pages.Administration.Users.Unlock', 'Pages.UserExtension.ImportExcel', 'Pages.UserExtension.ExportToExcel', 'Pages.UserGroup.Node', 'Pages.UserGroup.Query', 'Pages.UserGroup.Create', 'Pages.UserGroup.Edit', 'Pages.UserGroup.Delete', 'Pages.UserGroup.BatchDelete', 'Pages.UserGroup.ExportExcel', 'Pages.Administration.CustomerOrganizationUserUserGroup.Node', 'Pages.Administration.CustomerOrganizationUserUserGroup.Query', 'Pages.Administration.CustomerOrganizationUserUserGroup.Create', 'Pages.Administration.CustomerOrganizationUserUserGroup.Edit', 'Pages.Administration.CustomerOrganizationUserUserGroup.Delete', 'Pages.Administration.CustomerOrganizationUserUserGroup.ExportExcel', 'Pages.Administration.CollectNode.Node', 'Pages.Administration.CollectNode.Query', 'Pages.Administration.CollectNode.Create', 'Pages.Administration.CollectNode.Edit', 'Pages.Administration.CollectNode.Delete', 'Pages.Administration.CollectNode.BatchDelete', 'Pages.Administration.CollectNode.CreateStation', 'Pages.Administration.CollectNode.EditStation', 'Pages.Administration.CollectNode.DeleteStation', 'Pages.Administration.CollectNode.CreateService', 'Pages.Administration.CollectNode.EditService', 'Pages.Administration.CollectNode.DeleteService', 'Pages.Administration.AppConfig.Node', 'Pages.Administration.AppConfig.Query', 'Pages.Administration.AppConfig.Create', 'Pages.Administration.AppConfig.Edit', 'Pages.Administration.AppConfig.Delete', 'Pages.Administration.AppConfig.BatchDelete', 'Pages.Administration.AppConfig.ExportExcel', 'Pages.SystemManager', 'Pages.Administration.Languages', 'Pages.Administration.Languages.Query', 'Pages.Administration.Languages.Create', 'Pages.Administration.Languages.Edit', 'Pages.Administration.Languages.Delete', 'Pages.Administration.Languages.ChangeTexts', 'Pages.Administration.AuditLogs', 'Pages.Administration.Tenant.Settings', 'Pages.SysFile', 'Pages.SysFile.Query', 'Pages.SysFile.Create', 'Pages.SysFile.Edit', 'Pages.SysFile.Delete', 'Pages.SysFile.BatchDelete', 'Pages.SysFile.ExportExcel', 'Pages.Administration.Users.Online', 'Pages.Administration.Users.Downline', 'Pages.Administration.LoginLogs', 'Pages.Administration.LoginLogs.Query', 'Pages.Administration.LoginLogs.LogingLogs', 'Pages.Administration.LoginLogs.LoginStatistics', 'Pages.CacheState.Node', 'Pages.CacheState.Query', 'Pages.CacheState.Delete', 'Pages.CacheState.FlushDb', 'Pages.FinancialManager', 'Pages.FinancialManager.WashingOrderSettlement', 'Pages.FinancialManager.WashingOrderSettlement.Query', 'Pages.FinancialManager.WashingOrderSettlement.Node', 'Pages.FinancialManager.WashingOrderSettlement.Mail', 'Pages.FinancialManager.WashingOrderSettlement.TakeEffect', 'Pages.FinancialManager.WashingOrderSettlement.Nullify', 'Pages.FinancialManager.WashingOrderSettlement.ExportExcel', 'Pages.CleanAreaDailyManager', 'Pages.CleanAreaDailyManager.Charts', 'Pages.CleanAreaDailyManager.CleanAreaDaily', 'Client', 'Client.Home', 'Client.Home.Dashboard', 'Client.AssetsManager', 'Client.AssetsManager.StockManager', 'Client.AssetsManager.SignInStockIn', 'Client.AssetsManager.SignInPutIn', 'Client.AssetsManager.SignInDeliver', 'Client.AssetsManager.ReplaceTag', 'Client.AssetsManager.AssetLogout', 'Client.AssetsManager.AssetChange', 'Client.AssetsManager.AssetQueryHistory', 'Client.Operate', 'Client.Operate.Receive', 'Client.Operate.Delivery', 'Client.Operate.PutIn', 'Client.Operate.ScanningScene', 'Client.Operate.LampInspection', 'Client.Operate.Pack', 'Client.Operate.Sterilization', 'Client.Operate.EnterFactory', 'Client.Operate.DepartFactory', 'Client.Operate.DirtyAssetSorting', 'Client.Operate.RewashSorting', 'Client.Operate.CleanArea', 'Client.Operate.PackageCollocation', 'Client.Operate.BundleUp', 'Client.Operate.OrderSummary', 'MobileApp', 'MobileApp.Home', 'MobileApp.Home.Receive', 'MobileApp.Home.Receive.Query', 'MobileApp.Home.Receive.Submit', 'MobileApp.Home.Receive.Repeal', 'MobileApp.Home.Receive.Print', 'MobileApp.Home.Delivery', 'MobileApp.Home.Delivery.Query', 'MobileApp.Home.Delivery.Submit', 'MobileApp.Home.Delivery.Repeal', 'MobileApp.Home.Delivery.Print', 'MobileApp.Home.PackageDeliver', 'MobileApp.Home.PackageDeliver.Query', 'MobileApp.Home.PackageDeliver.Submit', 'MobileApp.Home.PackageDeliver.Repeal', 'MobileApp.Home.PackageDeliver.Print', 'MobileApp.Home.PackageDistribution', 'MobileApp.Home.PackageDistribution.Query', 'MobileApp.Home.PackageDistribution.Submit', 'MobileApp.Home.PackageDistribution.Repeal', 'MobileApp.Home.PackageDistribution.Print', 'MobileApp.Home.ScanningAndTallying', 'MobileApp.Home.AssetInquiry', 'MobileApp.Home.AssetInquiry.Query', 'MobileApp.Invoice', 'MobileApp.Invoice.Receive', 'MobileApp.Invoice.Receive.Query', 'MobileApp.Invoice.Receive.QueryDetail', 'MobileApp.Invoice.Receive.Print', 'MobileApp.Invoice.Receive.SignFor', 'MobileApp.Invoice.Delivery', 'MobileApp.Invoice.Delivery.Query', 'MobileApp.Invoice.Delivery.QueryDetail', 'MobileApp.Invoice.Delivery.Print', 'MobileApp.Invoice.Delivery.SignFor', 'MobileApp.Invoice.PackageDeliver', 'MobileApp.Invoice.PackageDeliver.Query', 'MobileApp.Invoice.PackageDeliver.QueryDetail', 'MobileApp.Invoice.PackageDeliver.Print', 'MobileApp.Invoice.PackageDeliver.SignFor', 'MobileApp.Invoice.PackageDistribution', 'MobileApp.Invoice.PackageDistribution.Query', 'MobileApp.Invoice.PackageDistribution.QueryDetail', 'MobileApp.Invoice.PackageDistribution.Print', 'NodeApp', 'NodeApp.NodeConfig', 'NodeApp.SterilizationRecord', 'SmallApp', 'SmallApp.Home', 'SmallApp.Home.IndentDelivery', 'SmallApp.Bill', 'SmallApp.Bill.IndentDelivery', 'SmallApp.Bill.IndentDelivery.UnlockEdit', 'SmallApp.Bill.IndentDelivery.Resubmit', 'SmallApp.Bill.IndentDelivery.Nullify', 'SmallApp.Bill.IndentDelivery.Approved', 'SmallApp.Bill.IndentDelivery.ApprovalRejected', 'SmallApp.Bill.IndentDelivery.AcceptOrders', 'SmallApp.Bill.IndentDelivery.RefundOrder', 'SmallApp.Bill.IndentDelivery.SignFor', 'SmallApp.Bill.IndentDelivery.RefusalToSend', 'SmallApp.Bill.IndentDelivery.WithdrawDraft', 'SmallApp.Bill.IndentDelivery.ProxySignature', 'SmallApp.Bill.IndentDelivery.AnotherOrder', 'SmallApp.Bill.IndentDelivery.Evaluate', 'SmallApp.Bill.IndentDelivery.Print', 'SmallApp.Statistics', 'SmallApp.Statistics.MonthlyBill', 'SmallApp.Statistics.DailySendAndReceiveStatistics']




    # 登录系统获取token后查询角色中权限
    try:
        url_s = UserProperty().url + "/api/TokenAuth/Authenticate"
        json_s = {"userNameOrEmailAddress": UserProperty().user, "password": UserProperty().pwd, "clientType": "PC"}
        # 直接传递tenant租户id，不用调用租户接口
        headers_s = {"Content-Type": "application/json", "tenant": UserProperty().tenant_id}
        # 登录获取token

        res = requests.post(url=url_s,json=json_s,headers=headers_s)
        # print(type(res.text))
        # print(res.text)
        # 设置token
        result_s = json.loads(res.text)
        token = result_s['result']['accessToken']
        # print(token)
        token_s = "Bearer "+token
        # print(token_s)
        # 请求权限列表
        url_menu = UserProperty().url + "/api/services/app/Permission/GetAllPermissions?platfrom="
        headers_menu = {"Content-Type": "application/json", "tenant": UserProperty().tenant_id,
                         "authorization": token_s}
        res_p = requests.get(url=url_menu,headers=headers_menu)
        res_list = json.loads(res_p.text)["result"]
        # print(res_list)
        # print(type(res_list))
        menu_list = res_list["items"]
        # print(type(menu_list))
        name_list = []
        for i in menu_list:
            # print(i["name"])
            # 排除自建扫描场景-针对desktop里面
            if i["parentName"] == "Client.Operate.ScanningScene":
                # print(i)
                continue
            # 排除自建扫描场景-对应APP中扫描清点功能，扫描清点需要建立一个场景
            if i["parentName"] == "MobileApp.Home.ScanningAndTallying":
                # print(i)
                continue
            name_list.append(i["name"])
        # print(name_list)
        # print(len(name_list))
        if name_list == s_menu_list:
            print("权限列表一致")
        else:
            for i in name_list:
                if i not in s_menu_list:
                    print(i)
            print("两边权限列表不一致，发送邮件")
            email_title = "权限列表检查"
            email_content = '<html> <head><title>check report</title></head> <body> <h3>iUS权限列表检查：{}</h3> <div>权限列表检查权限不匹配</div><div>url：https://x.51xi.com</div></body> </html>'.format(
                date_s)
            send_mail(subject=email_title, content=email_content, receive=EmailProperty().RECEVI_EMAIL2)



    except Exception as e:
        print("请求发生异常，发送邮件")
        print(e)
        email_title = "权限列表检查"
        email_content = '<html> <head><title>check report</title></head> <body> <h3>iUS权限列表检查：{}</h3> <div>权限列表检查请求出现问题，需要查看</div><div>url：https://x.51xi.com</div></body> </html>'.format(
            date_s)
        send_mail(subject=email_title, content=email_content, receive=EmailProperty().RECEVI_EMAIL2)



if __name__=="__main__":
    check_menulist()

