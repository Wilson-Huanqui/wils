## Bulk image resizer

# This script simply resizes all the images in a folder to one-eigth their
# original size. It's useful for shrinking large cell phone pictures down
# to a size that's more manageable for model training.

# Usage: place this script in a folder of images you want to shrink,
# and then run it.

import numpy as np
import cv2
import os

from PIL import Image
import os




dir_path = os.getcwd()

for filename in os.listdir(dir_path):
    # If the images are not .JPG images, change the line below to match the image type.
    if filename.endswith(".jpg"):
        image = Image.open(filename)

        file_size = os.path.getsize(filename)
        width = image.size[0]
        height = image.size[1]
            
        print("filename: " + filename)
        print("width: " + str(width))
        print("height: " + str(height))
        print("file_size: " + str(file_size/1000) + "kb")

        centerline = width/2
        middleline = height/2

        if(width > height):
            # crop width to height
            left = centerline - middleline
            upper = 0
            right = centerline + middleline
            lower = height
        else:
            # crop height to width            
            left = 0
            upper = middleline - centerline
            right = width
            lower = middleline + centerline 




        im_crop = image.crop((left, upper, right, lower))
        resized = im_crop.resize((800, 800))
        resized.save(filename, quality=95)
        

        # image = cv2.imread(filename)
        # resized = cv2.resize(image,None,fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
        # cv2.imwrite(filename,resized)