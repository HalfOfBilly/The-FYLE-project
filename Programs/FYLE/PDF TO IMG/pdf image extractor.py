import sys
import os

from pdf2image import convert_from_path

arg = sys.argv

pdf_in = arg[1]

image_out = arg[2]
name = (os.path.basename(pdf_in)).split(".")[0]

ext = arg[3]

OUTEXT = ext.upper()
   
pages = convert_from_path(pdf_in)
r = -1
for page in pages:
    r += 1
    no = '{:0002}'.format(r)
    page.save(f"{image_out}//{name}_{no}.{ext}", OUTEXT)

sys.exit(0)
