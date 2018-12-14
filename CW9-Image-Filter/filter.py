"""
CS550 Classwork: Image filter
November 12, 2018

@author: Ethan Chapman
"""

from PIL import Image
from functools import partial
from typing import List

import sys
import itertools
import multiprocessing

from commandLine import CommandLine, Argument
from imagefilter import ImageFilter

from edgedetect import EdgeDetect
from smallpalette import SmallPalette
from bulge import Bulge

filters = [Bulge(320 / 800, 200 / 600, 0.3, 0.8), SmallPalette()]

sys.argv += ["image2.jpg"]

command_line = CommandLine(__file__)
command_line.add_argument("IMAGE", Argument(str), "The image to apply the filter to")
[image_path] = command_line.get_arg_values()

image: Image.Image

try:
    image = Image.open(image_path)

except FileNotFoundError:
    print("File not found!")
    exit()

# image = image.resize((800, int(image.height * (800 / image.width))))

def image_filter(image: Image.Image, filters: List[ImageFilter]):
    image = image.copy()

    print("Loading pixels...")
    pixels = [[0] * image.height for _ in range(image.width)]
    for x in range(image.width):
        for y in range(image.height):
            pixels[x][y] = image.getpixel((x, y))

    print("Calculating new values...")
    pool = multiprocessing.Pool()

    for filter in filters:
        temp = partial(filter.filter, w=image.width, h=image.height, pixels=pixels)
        new_pixels = filter.process(pool.starmap(temp, itertools.product(range(image.width), range(image.height))))

        i, j = 0, 0

        for p in new_pixels:
            pixels[i][j] = p

            j += 1

            if j == image.height:
                j = 0
                i += 1

    print("Saving new values...")
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel((x, y), pixels[x][y])

    return image


def combine(image1: Image.Image, image2: Image.Image):
    image1 = image1.copy()

    for x in range(image.width):
        for y in range(image.height):
            val1 = image1.getpixel((x, y))
            val2 = image2.getpixel((x, y))

            val = tuple(int(sum(i) / 2) for i in zip(val1, val2))

            image1.putpixel((x, y), val)

    return image1


image1 = image_filter(image, filters)
image2 = image_filter(image1, [EdgeDetect()])

image = combine(image1, image2)

image.save(".".join(["".join(i) for i in zip(image_path.split("."), ["_new", ""])]))