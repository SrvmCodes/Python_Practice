import PIL
from PIL import Image

img = PIL.Image.open("C:/Users/ankit/OneDrive/Desktop/SRV/Srv_img.jpg")
width , height = img.size
print(width, "*", height)