import sys
import os

from PIL import Image

arg = sys.argv
    
inputt = arg[1]

export = arg[2]

newwidth = int(arg[3])

name = (os.path.basename(inputt))

outputt = f"{export}//{name}"


Image.MAX_IMAGE_PIXELS = None
img = Image.open(inputt)

base_width= newwidth
hsize = int(float(img.size[1]) * (base_width / float(img.size[0])))

img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
img.save(outputt)
