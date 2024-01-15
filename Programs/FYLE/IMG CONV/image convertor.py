import sys
import os

import PIL.Image as PIL
import pillow_avif

image_in = sys.argv[1]

ext = sys.argv[3]

alpha = int(sys.argv[4])

image_out = f'{sys.argv[2]}\\{os.path.basename(image_in).split(".")[0]}.{ext}'
 
img = PIL.open(image_in)
if alpha: 
    img.convert("RGBA")
else:
    img = img.convert("RGB")
img.save(image_out)

