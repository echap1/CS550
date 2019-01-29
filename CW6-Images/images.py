from PIL import Image

import random
import itertools

from libs.commandLine import open

def checker(checkers, a=(0, 0, 0), b=(255, 255, 255), w=1000, h=1000):
    image = Image.new("RGB", (w, h))
    image.putdata([255 * (((x % 2) + (y % 2)) % 2) for x, y in itertools.product(range(w), range(h))])
    image.save("checker.png", "PNG")
    open("checker.png")


def fuzzy(lines, w=1000, h=1000):
    image = Image.new("RGB", (w, h))

    for _ in range(lines):
        color = (random.randrange(256), random.randrange(256), random.randrange(256))

        c_x, c_y = random.randrange(w), 0

        while 0 <= c_x < w and 0 <= c_y < h:
            image.putpixel((c_x, c_y), color)

            c_x, c_y = c_x + random.randint(-1, 1), c_y + 1

    image.save("fuzzy.png", "PNG")

    open("fuzzy.png")

    