# coding = utf-8
#专门存放参数的地方

class symbol(object):
    """
    放置搜索关键字，特殊字符
    """
    number = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,99,999]
    english_symbol = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+",
                      "=", ";", ":", "'", "<", ">", ".", "?", "/", "\\", "|"]
    china_symbol = ["·", "~", "！", "@", "#", "￥", "%", "……", "&", "*", "（", "）", "——", "-", "+",
                      "=", "；", "：", "’", "《", "》", "。", "？", "、", "、", "|"]
    english = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","o","r","s","t","u","v","w","x","y"
        ,"z"]
    more = ["r,p","s,m"]
    chinese = ["公司","股份","科技","建设","集团","发现","金额","风险","证券","航天","宏图","国信证券"]