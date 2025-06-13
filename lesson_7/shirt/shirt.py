"""
Implement a program that expects exactly two command line arguments:
    1. in sys.argv[1], the name of a JPEG/PNG to read as input
    2. in sys.argv[2], the name of a JPEG/PNG to write as output
Program should then overlay shirt.png on the input after resizing and
cropping the input to be the same size, saving the result as its output.

Open input with Image.open, resize and crop the input with ImageOps.fit,
using default values for method, bleed, and centering, overlay the shirt
with Image.paste, and save the result with Image.save

Program should exit via sys.exit:
    * if user does not specify exactly two command-line argyments
    * if input's and output's names do not end in .jpg, .jpeg, .png
    * if input's name does not have the same extension as the output's
    * if specified input does not exist
"""

import csv
import sys
from PIL import Image, ImageOps

def file_checker(value):
    allowed = ('.png', '.jpeg', 'jpg')
    if len(value) < 2:
        sys.exit('Too few command-line arguments')
    if len(value) > 2:
        sys.exit('Too many command-line arguments')

    for item in value:
        if not item.endswith(allowed):
            sys.exit('Invalid input')

    value1 = (value[0].split('.'))[1]
    value2 = (value[1].split('.'))[1]

    if value1 != value2:
        sys.exit('Input and output have different extensions')

def main():
    file_checker(sys.argv[1:])

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with Image.open(input_file) as muppet, Image.open("shirt.png") as shirt:
            resize_muppet = ImageOps.fit(muppet, shirt.size)
            resize_muppet.paste(shirt, shirt)
            resize_muppet.save(output_file)
    except FileNotFoundError:
        sys.exit('File does not exist')



if __name__ == '__main__':
    main()
