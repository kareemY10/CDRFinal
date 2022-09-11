from PIL import Image
from PIL.ExifTags import TAGS


# path to the image or video
imagename = "image.jpg"

# read the image data using PIL
image = Image.open(imagename)


# extract EXIF data
exifdata = image.getexif()

