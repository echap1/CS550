import colorsys

class Histogram:
    points = {}

    def __init__(self):
        pass

    def __iadd__(self, point: tuple):
        index = point[0]
        color = point[1]

        self.add_color_point(index, color)

        return self

    def __call__(self, index):
        i = 0
        p_i = 0

        for i, v in self.points.items():
            if i > index: break

            p_i = i

        color_before = self.points[p_i]
        color_after = self.points[i]

        dif = (index - p_i) / (i - p_i)

        if i - p_i == 0:
            dif = 0

        return linear_interpolate(color_before, color_after, dif)

    def add_color_point(self, index, color):
        self.points[index] = color


def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def linear_interpolate(col1, col2, dif):
    interp = lambda i: int(col2[i] * dif + col1[i] * (1 - dif))

    return (interp(0), interp(1), interp(2))