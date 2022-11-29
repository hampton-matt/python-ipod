from PIL import Image
from pathlib import Path

image_in = Path(__file__).with_name("pod_arrow_grn.png")
image_out = Path(__file__).with_name("converted.png")
img = Image.open(image_in)
img = img.convert("RGBA")
data = img.getdata()

recoloured = []
for pixel in data:
    if pixel[1] in range(25, 255):
        recoloured.append((0,0,0,255))
    else:
        recoloured.append(pixel)

img.putdata(recoloured)
img.save(image_out)
