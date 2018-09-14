# -*- coding: utf-8 -*-

import io, http.client, urllib.request, urllib.parse, urllib.error, base64
import requests
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import json
from io import BytesIO

# 文字化け問題解決
import matplotlib as mpl

import matplotlib.font_manager
from matplotlib.font_manager import FontProperties

#fonts = matplotlib.font_manager.findSystemFonts(fontpaths="/Library/Fonts", fontext='ipagp.ttf')
font_path = '/Library/Fonts/ipagp.ttf'
font_prop = FontProperties(fname=font_path)

font_path_zh ='/System/Library/Fonts/PingFang.ttc'
font_prop_zh = FontProperties(fname=font_path_zh)
#mpl.rcParams['font.family'] = font_prop.get_name()
#plt.rcParams['font.family'] = font_prop.get_name()
#print(font_prop.get_name())
#print(fonts)

x = np.linspace(-np.pi, np.pi, 101)
plt.plot(x, np.cos(x))

#fontpropertiesを明示的に指定する
plt.title("コサインカーブ", fontproperties=font_prop)
plt.xlabel("x軸", fontproperties=font_prop)
plt.ylabel("y軸", fontproperties=font_prop)

#plt.show()
#print(matplotlib.font_manager.findSystemFonts(fontpaths="/Library/Fonts", fontext='ttf'))

#plt.rcParams['font.family'] = 'IPAPGothic' #全体のフォントを設定
#mpl.rcParams['font.family'] = 'IPAPGothic'
mpl.rcParams['font.sans-serif'] = ['SimHei']
custom_vision_api_url = 'https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/da58abc8-04b1-4bbe-a8ae-f045884a9fdf/image'

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Prediction-key': 'fc8c23af2dbb419291c6d13df0a181ff',
}

params = urllib.parse.urlencode({
    # Request parameters
    'iterationId': 'cddb6ff1-98ed-4d04-85e8-47dec32f754b',
})

try:
    #conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    f = open("food3.jpg", "rb", buffering=0)
    #conn.request("POST", "/customvision/v2.0/Prediction/da58abc8-04b1-4bbe-a8ae-f045884a9fdf/image?%s" % params, f.readall(), headers)

    response = requests.post(custom_vision_api_url, params=params, headers=headers, data=f)
    #response = conn.getresponse()
    response.raise_for_status()

    #data = response.read()
    data = response.json()

    #data_json = json.loads(response, encoding="utf-8")
    #f_read = f.read()
    f_data = Image.open(f)
    print(json.dumps(data, indent=4, ensure_ascii=False))
    #print(data)
    plt.imshow(f_data)
    tag_id = ''
    tag_score = ''
    if (data["predictions"]):
        tag_id = data["predictions"][0]["tagName"].capitalize()
        tag_score =  data["predictions"][0]["probability"]
    tag_id = data["predictions"][0]["tagName"].capitalize()
    print(tag_id)
    #print(data["predictions"][0]["tagName"])
    _ = plt.title(tag_id+" Score: "+tag_score.__str__(), size="x-large", y=-0.1, color='blue', fontproperties=font_prop_zh)


    plt.axis("off")

    plt.show()
    #conn.close()
except Exception as e:
    # print("[Errno {0}] {1}".format(e.errno, e.strerror))
    print(e)
