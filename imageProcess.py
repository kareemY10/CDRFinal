from PIL import Image
from PIL.ExifTags import TAGS
from pytesseract import pytesseract
import os
import sys

# path to the image or video
imagename = "sample.jpeg"

# read the image data using PIL
image = Image.open(imagename)

text = pytesseract. image_to_string(image)

# extract EXIF data
exifdata = image.getexif()

with open ("ImageText" , 'w') as f:
    f.write(text)
    f.close()