import requests
from io import BytesIO
from PIL import Image

#You'd need to install requests and pillow python libraries

url = input("Enter the URL of image to download: ")
r = requests.get(url)

print("Fetching image! Status code:", r.status_code)

image= Image.open(BytesIO(r.content))
print(image.size,image.format,image.mode)
path="./image1."+image.format

try:
    image.save(path,image.format)
except IOError:
    print("Can't save image!")