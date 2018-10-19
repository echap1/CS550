"""
CS550 Homework: Red Image
Due October 15, 2018

@author: Ethan Chapman
"""

from PIL import Image

import numpy as np
import random

w, h = 1000, 1000

image = Image.new("RGB", (w, h))

def save_image(value, name):
    for i in range(w):
        for j in range(h):
            image.putpixel((i, j), value(i, j))

    image.save(name, "PNG")

save_image(lambda x, y: (255, 0, 0), "red.png")
save_image(lambda x, y: (int(128 * (np.sin(x * 40 / w) + 1)), int(128 * (np.sin(y * 40 / h) + 1)), 0), "sine.png")
save_image(lambda x, y: (int((x / 100) % 1 * 255), int((y / 100) % 1 * 255), int(y / h * 255)), "mod.png")
save_image(lambda x, y: (random.randrange(256), random.randrange(256), random.randrange(256)), "random.png")