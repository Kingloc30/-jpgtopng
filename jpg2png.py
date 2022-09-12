"""
My simple image converter to convert image formats
For more info check the docs
https://pillow.readthedocs.io/en/stable/reference/Image.html#functions

"""

import sys
import os
from PIL import Image, ImageFilter 

# for use by command line 
#  Grab the 1st and 2nd argument 
image_folder = sys.argv[1] # using sys module this points to folder with pics
output_folder = sys.argv[2]  # this is the destination folder where converted pics are saved

# This checks if the destination folder exists and if not creates it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# using os.listdir() to get file names
for filename in os.listdir(image_folder):
    #create new variable with f string to include folder and file name
    img = Image.open(f'{image_folder}{filename}')
    # this splits the file name at the . using indexing where 0 is the file name and 1 the extension '.jpg' etc..
    clean = os.path.splitext(filename)[0]
    # Saves image in its new format
    img.save(f'{output_folder}{clean}.png', 'png')

    print('Image has been converted...:) ')
