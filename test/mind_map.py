# 2022-07-19 处理思维导图






# 恢复思维导图
import json


def revcovery_mindmap():
    a = '{"asctime":"2022-06-16 20:17:24,041","thread":140519778805504,"request_id":"0d863c17e6744bbe84a3d4af2c3513db","lineno":325,"module":"enter_log","level":"INFO","msg":"{"remote_ip":"211.137.203.178","type":"request","method":"POST","path":"/resource/anno/update_xmind/","user":15610145335,"userId":44627,"source":9999,"get_params":{},"post_params":{"id": [1852601], "new_xmind": ["{\"content\":{\"root\":{\"data\":{\"id\":\"8zC1cMDUXwqlrhAo\",\"text\":\" Epicardial Fat Expansion in Diabetic and\\n Obese Patients With Heart Failure and Preserved\\n Ejection Fraction-A Specific HFpEF Phenotype\"},\"children\":[{\"data\":{\"id\":\"ckrjo4gxgwo0\",\"created\":1655381225297,\"text\":\"序言\"},\"children\":[{\"data\":{\"id\":\"ckrjocp3rb40\",\"created\":1655381243206,\"text\":\"流行病学\"},\"children\":[]},{\"data\":{\"id\":\"ckrjojfrs540\",\"created\":1655381257879,\"text\":\"血流动力学特点\"},\"children\":[]},{\"data\":{\"id\":\"ckrjooyk37c0\",\"created\":1655381269899,\"text\":\"病因\"},\"children\":[{\"data\":{\"id\":\"ckrjotkdm800\",\"created\":1655381279925,\"text\":\"肥胖与二型糖尿病\"},\"children\":[{\"data\":{\"id\":\"ckrjp2qo4fs0\",\"created\":1655381299897,\"text\":\"EAT\"},\"children\":[]}]}]}]},{\"data\":{\"id\":\"ckrjp7indxs0\",\"created\":1655381310296,\"text\":\"肥胖型\"},\"children\":[{\"data\":{\"id\":\"ckrjpnk4fxc0\",\"created\":1655381345213,\"text\":\"HFpEF与炎症的机制\"},\"children\":[]},{\"data\":{\"id\":\"ckrjpz5j0jk0\",\"created\":1655381370452,\"text\":\"肥胖与炎症\"},\"children\":[]},{\"data\":{\"id\":\"ckrjq3eza400\",\"created\":1655381379731,\"text\":\"肥胖与HFpEF\"},\"children\":[]},{\"data\":{\"id\":\"ckrjq9dt0eo0\",\"created\":1655381392720,\"text\":\"肥胖与非肥胖患者比较\"},\"children\":[]}]},{\"data\":{\"id\":\"ckrjqisndpc0\",\"created\":1655381413209,\"text\":\"糖尿病型\"},\"children\":[{\"data\":{\"id\":\"ckrjqp5v7lk0\",\"created\":1655381427069,\"text\":\"二型糖尿病导致HFpEF的机制\"},\"children\":[]},{\"data\":{\"id\":\"ckrjr6rfvts0\",\"created\":1655381465379,\"text\":\"二型糖尿病相关的射血分数保留型心衰与糖尿病型心脏病（射血分数降低）鉴别\"},\"children\":[]}]},{\"data\":{\"id\":\"ckrjs9pwrdc0\",\"created\":1655381550181,\"text\":\"心外膜脂肪组织对伴有糖尿病或肥胖的HFpEF的影响\"},\"children\":[{\"data\":{\"id\":\"ckrjt02zjg80\",\"created\":1655381607568,\"text\":\"肥胖\"},\"children\":[{\"data\":{\"id\":\"ckrjtktc8e00\",\"created\":1655381652697,\"text\":\"与非肥胖患者比较EAT\"},\"children\":[]},{\"data\":{\"id\":\"ckrjtvteg1k0\",\"created\":1655381676645,\"text\":\"炎症因子\"},\"children\":[]}]},{\"data\":{\"id\":\"ckrjt5bh0080\",\"created\":1655381618965,\"text\":\"糖尿病\"},\"children\":[{\"data\":{\"id\":\"ckrju7nqvk00\",\"created\":1655381702425,\"text\":\"炎症\"},\"children\":[]}]},{\"data\":{\"id\":\"ckrjuh7ltgo0\",\"created\":1655381723216,\"text\":\"EAT\"},\"children\":[{\"data\":{\"id\":\"ckrjul4kokw0\",\"created\":1655381731740},\"children\":[]}]}]},{\"data\":{\"id\":\"ckrjvmzuk1c0\",\"created\":1655381814172,\"text\":\"诊断\"},\"children\":[{\"data\":{\"id\":\"ckrjvphw4w80\",\"created\":1655381819617,\"text\":\"经胸超声心动图，CMR，CT\"},\"children\":[]}]}]},\"template\":\"right\",\"theme\":\"fresh-green\",\"version\":\"1.4.43\",\"pageBg\":\"grid\"}}"]}}"}'
    info = a.replace('\\"','"')
    # 针对侧边栏思维导图的参数处理
    xmind_info = info.split('"new_xmind": [')[1][1:-6]

    print(xmind_info)





if __name__ == "__main__":
    revcovery_mindmap()







