# encoding:utf-8

import requests
import json
import base64
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 获取图片base64位编码
with open('img\\zhizhu0.jpg', 'rb') as f:  #
    imgData = f.read();
    base64_data = base64.b64encode(imgData)
    img_str = str(base64_data.decode())
    print(img_str)

# 读取图片
img = mpimg.imread('img\\zhizhu0.jpg')
plt.imshow(img)

# 获取access_token
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=QokqGEipXyVgdGLxlOgIteac&client_secret=25rNle6eLZYrlTQRWUAf1XfGqRssTlsp'
response = requests.post(host)
res = response.json()
print(res)
print(res['access_token'])
access_token = str(res['access_token'])
# access_token = "24.81a66327f5c05ac766580f87890dfe94.2592000.1640334891.282335-25222646"
print(access_token)

# 图片组合识别API
request_url = "https://aip.baidubce.com/api/v1/solution/direct/imagerecognition/combination"
params = {'image': str(img_str),
          'scenes': ["animal"],
          'sceneConf': {
              'animal': {
                  "top_num": "2"
              }
          }
          }
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json;charset=utf-8'}
response = requests.post(request_url, data=json.dumps(params), headers=headers)

# 输出读取到的图片和识别信息
plt.show()
print(json.dumps(response.json(), ensure_ascii=False, indent=2))
