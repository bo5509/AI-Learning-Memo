import requests
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import json

# Replace <Subscription Key> with your valid subscription key.
subscription_key = "c2625dbf28bc4b9ab0595ea26637a5d1"
assert subscription_key

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the westcentralus region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
vision_base_url = "https://japaneast.api.cognitive.microsoft.com/vision/v1.0/"

landmark_analyze_url = vision_base_url + "models/landmarks/analyze"

# Set image_url to the URL of an image that you want to analyze.
#image_url = "https://upload.wikimedia.org/wikipedia/commons/f/f6/" + \
 #   "Bunker_Hill_Monument_2005.jpg"

#image_url = "https://upload.wikimedia.org/wikipedia/ja/thumb/3/3e/MtFuji_FujiCity.jpg/320px-MtFuji_FujiCity.jpg"
#image_url = "https://i.ytimg.com/vi/Fs1W5WrGTjE/hqdefault.jpg"
image_url = "https://clicktraveltips.com/wp-content/uploads/2013/04/Golden-Gate-Bridge.jpg"
image_url = "https://cdntct.com/tct/pic/china-tour-pic/beijing/tiananmen-04.jpg"
#image_url = "https://cache-graphicslib.viator.com/graphicslib/thumbs360x240/7845/SITours/%E3%82%A8%E3%83%83%E3%83%95%E3%82%A7%E3%83%AB%E5%A1%94%E3%81%B8%E3%81%AE%E5%84%AA%E5%85%88%E5%85%A5%E5%A0%B4%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%EF%BC%88%E3%83%9B%E3%82%B9%E3%83%88%E4%BB%98%E3%81%8D%EF%BC%89-in-paris-299567.jpg"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params  = {'model': 'landmarks'}
data    = {'url': image_url}
response = requests.post(
    landmark_analyze_url, headers=headers, params=params, json=data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The
# most relevant landmark for the image is obtained from the 'result' property.
analysis = response.json()
assert analysis["result"]["landmarks"] is not []
print(json.dumps(analysis, indent=4))
landmark_name = ''
if(analysis["result"]["landmarks"]) :
    landmark_name = analysis["result"]["landmarks"][0]["name"].capitalize()

# Display the image and overlay it with the landmark name.
image = Image.open(BytesIO(requests.get(image_url).content))

#image.show()
image.save('landmark.jpg')
plt.imshow(image)
plt.axis("off")
_ = plt.title(landmark_name, size="x-large", y=-0.1, color='blue')

plt.show()