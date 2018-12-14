from typing import List

import numpy as np

from imagefilter import ImageFilter


class Bulge(ImageFilter):
    x: int
    y: int
    size: float
    strength: float
    pinch: bool

    def __init__(self, x, y, size, strength, pinch=False):
        self.x = x
        self.y = y
        self.size = size
        self.strength = strength
        self.pinch = pinch

    def filter(self, x: int, y: int, w: int, h: int, pixels: List[List[tuple]]):
        new_pos = self.displace(x, y, w, h)

        return pixels[new_pos[0]][new_pos[1]]

    def process(self, new_pixels: List[tuple]):
        return new_pixels

    def displace(self, x, y, w, h):
        if x == self.x * w and y == self.y * h:
            return (x, y)

        dist_vec = complex(x, y) - complex(self.x * w, self.y * h)

        dist_vec *= 1 if self.pinch else -1

        d = self.displacement_function(abs(dist_vec), w, h)

        res_vec = complex(x, y) + d * dist_vec

        return (int(res_vec.real), int(res_vec.imag))

    def displacement_function(self, dist, w, h):
        x = dist / (abs(complex(w, h)) * self.size)

        return self.strength * np.exp(-np.power(x, 2))
