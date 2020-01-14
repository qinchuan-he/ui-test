# coding = utf-8

# 图片比对

from PIL import Image
import math
import operator
from functools import reduce


def image_contrast(img1, img2):

    image1 = Image.open(img1)
    image2 = Image.open(img2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return result

if __name__ == '__main__':
    root = "C:\\Users\\fir\\Pictures\\QQ浏览器截图\\"
    picture1 = root+"QQ浏览器截图20200113105954.png"
    picture2 = root+"QQ浏览器截图20200113105958.png"
    img1 = "./1.png"  # 指定图片路径
    img2 = "./2.png"
    result = image_contrast(picture1,picture2)
    print(result)





