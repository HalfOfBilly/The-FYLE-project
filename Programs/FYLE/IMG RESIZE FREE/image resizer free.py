import sys
import os

from PIL import Image

arg = sys.argv
    
inputt = arg[1]

export = arg[2]

newwidth = int(arg[3])
newheight = int(arg[4])

name = (os.path.basename(inputt))

outputt = f"{export}//{name}"


Image.MAX_IMAGE_PIXELS = None
img = Image.open(inputt)

img = img.resize((newwidth, newheight), Image.Resampling.LANCZOS)
img.save(outputt)
