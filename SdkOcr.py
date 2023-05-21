# encoding:utf-8

from aip import AipImageClassify
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.font_manager import FontProperties

import P_leaf
import P_rect
import re
import P_circle
import P_extend
import P_spherical

def sdkocr(path):
    """ 你的 APPID AK SK """
    APP_ID = '25222646'
    API_KEY = 'QokqGEipXyVgdGLxlOgIteac'
    SECRET_KEY = '25rNle6eLZYrlTQRWUAf1XfGqRssTlsp'

    client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

    """ 读取图片 """

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    # path = 'img\\9.jpg'

    # img = mpimg.imread(path)
    # plt.figure()
    # fontSet = FontProperties(fname=r"C:\Windows\Fonts\stsong.ttf", size=16)
    # plt.title(u"输入图片", color='k', fontproperties=fontSet, weight='heavy')
    # plt.imshow(img)

    image = get_file_content(path)

    """ 调用动物识别 """
    client.animalDetect(image)

    """ 如果有可选参数 """
    options = {}
    options["top_num"] = 1
    options["baike_num"] = 1

    P_circle.Circle(path)
    P_extend.Extend(path)
    P_leaf.Leaf(path)
    P_rect.Rect(path)
    P_spherical.Spherical(path)

    """ 带参数调用动物识别 """
    result = client.animalDetect(image, options)
    #print(type(result.get("result")))
    #tuple(result.keys())
    #print(tuple(result.get("result")))
    list = tuple(result.get("result"))

    # for res in list :
    #     print(res.get("name"))
    #     print(res.get("score"))

    plt.show()
    #print(json.dumps(result, ensure_ascii=False, indent=2))

    return list








