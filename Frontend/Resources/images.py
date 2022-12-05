from PIL import Image
from PIL import ImageColor
from math import ceil
from pathlib import Path

DIR_IMAGES = Path(__file__).parent / "files"
IMG_ARROW = "img_arrow.png"
IMG_PAUSE = "img_pause.png"
IMG_PLAY = "img_play.png"
IMG_TIMELINE = "img_timeline.png"
IMG_WIFI = "img_wifi.png"
IMG_NO_WIFI = "img_no_wifi.png"
IMG_BLANK = "img_space.png"
IMG_ARROW = "img_arrow.png"

def get_image(image, fg="#1DB954", bg="#000000"):
    img_file = DIR_IMAGES / image                                               # Get Image File using Path Directory
    img = Image.open(img_file)
    if fg != "#1DB954":                                                         # Check if foreground is different to default
        img = recolour(img, "#1DB954", fg)
    if bg != "#000000" and bg != "#000":                                         # Same check but for background
        img = recolour(img, "#000000", bg)
    
    return img

# Takes an open image file and converts the find hex to the replace hex
def recolour(image, find, replace):
    find_rgb = ImageColor.getrgb(find)
    replace_rgb = ImageColor.getrgb(replace)                 
    image.convert("RGBA")
    recoloured = []
    for pixel in image.getdata():
        if pixel[0:3] == find_rgb:
            recoloured.append(replace_rgb + (pixel[3],))
        else:
            recoloured.append(pixel)
    image.putdata(recoloured)
    return image

def resize(image, width=None, height=None):
    w, h = image.size
    resized = image
    if width is None and height is not None:
        temp = int((height/h) * w)
        resized = image.resize((temp, height), Image.Resampling.LANCZOS)
    elif width is not None and height is None:
        temp = int((width/w) * h)
        resized = image.resize((width, temp), Image.Resampling.LANCZOS)
    elif width is not None and height is not None:
        resized = image.resize((width, height), Image.Resampling.LANCZOS)
    return resized

# Debugging
if __name__ == "__main__":
   test = get_image(IMG_ARROW, "#FFF")
   test.show()
   
if __name__ == "don't run":
   temp = get_image("img_wifi.png")
   temp.convert("RGBA")
   temp2 = get_image("temp.png")
   test = temp2.convert("RGBA")
   temp.paste(test,(0,0))
   temp.save(DIR_IMAGES / "new.png")