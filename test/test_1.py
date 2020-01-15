# coding = utf-8

# 图片比对
import os
from common.comfunction import com_path
from PIL import Image
import math
import operator
from functools import reduce


def image_contrast(img1, img2):

    image1 = Image.open(img1)
    image2 = Image.open(img2)

    h1 = image1.histogram()
    print(h1)
    h2 = image2.histogram()
    print(h2)
    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return result

def add(a,b):
    return a+b

if __name__ == '__main__':
    root = "C:\\Users\\fir\\Pictures\\QQ浏览器截图\\"
    picture_url = os.path.join(com_path(), "样本", "智能审核样本.png")
    picture_url2 = os.path.join(com_path(), "截图", "智能审核截图.png")
    picture1 = root+"QQ浏览器截图20200113105954.png"
    picture2 = root+"QQ浏览器截图20200113105958.png"
    img1 = "./1.png"  # 指定图片路径
    img2 = "./2.png"
    result = image_contrast(picture_url,picture_url2)
    print(result)





