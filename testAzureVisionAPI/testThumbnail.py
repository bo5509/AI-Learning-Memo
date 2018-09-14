import requests
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

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

thumbnail_url = vision_base_url + "generateThumbnail"

# Set image_url to the URL of an image that you want to analyze.
image_url = "https://upload.wikimedia.org/wikipedia/commons/9/94/Bloodhound_Puppy.jpg"

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params  = {'width': '50', 'height': '50', 'smartCropping': 'true'}
data    = {'url': image_url}

original_image = Image.open(BytesIO(requests.get(image_url).content))
original_image.show()

response = requests.post(thumbnail_url, headers=headers, params=params, json=data)
response.raise_for_status()

thumbnail = Image.open(BytesIO(response.content))

#thumbnail.show()
thumbnail.save('thumbnail.jpg')
# Display the thumbnail.
plt.imshow(thumbnail)
plt.title("After", fontsize='x-large', y=-0.1, color='red')
plt.axis("off")
plt.show()

# Verify the thumbnail size.
print("Thumbnail is {0}-by-{1}".format(*thumbnail.size))