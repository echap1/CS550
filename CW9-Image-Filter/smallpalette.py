from typing import List

from imagefilter import ImageFilter


class SmallPalette(ImageFilter):
    def filter(self, x: int, y: int, w: int, h: int, pixels: List[List[tuple]]):
        return tuple(self.lower_palette(i, 4) for i in pixels[x][y])

    def process(self, new_pixels: List[tuple]):
        return new_pixels

    def lower_palette(self, n: int, colors: int):
        return int(255 * (float(int(colors * (n / 255.0))) / colors))