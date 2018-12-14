from typing import List

import numpy as np
import itertools

from imagefilter import ImageFilter


class EdgeDetect(ImageFilter):
    def filter(self, x: int, y: int, w: int, h: int, pixels: List[List[tuple]]):
        return EdgeDetect.standard_deviation(EdgeDetect.pixels_around(pixels, x, y, w, h, 5))

    def process(self, new_pixels: List[tuple]):
        max_val = 0

        for p in new_pixels:
            for i in p:
                if i > max_val:
                    max_val = i

        k = 255 / max_val

        for i in range(len(new_pixels)):
            new_pixels[i] = tuple(int(i * k) for i in new_pixels[i])

        return new_pixels

    @staticmethod
    def pixels_around(pixels, x, y, w, h, s):
        possible = list(itertools.product(range(-s, s + 1), repeat=2))
        possible = [(p[0] + x, p[1] + y) for p in possible]

        positions = [(x, y) for x, y in possible if 0 <= x < w and 0 <= y < h]

        colors = [pixels[xy[0]][xy[1]] for xy in positions]

        return colors

    @staticmethod
    def avg_color(colors):
        return tuple(int(sum([i[n] for i in colors]) / len(colors)) for n in range(3))

    @staticmethod
    def standard_deviation(colors):
        return tuple(int(i) for i in np.std(colors, axis=0))