import colorsys


# Give class color points and iteration values and it turns it into a continuous spectrum
class PointInterpolation:
    points: []

    def __init__(self):
        self.points = []

    # Add a color point: color += (index, (r, g, b))
    def __iadd__(self, point: tuple):
        index = point[0]
        color = point[1]

        self.add_color_point(index, color)

        return self

    # Get an interpolated color value for a certain iteration value
    def __call__(self, index):
        after = len([i for i in self.points if i[0] < index])

        if after == 0:
            return self.points[after][1]

        point_before = self.points[after - 1]
        point_after = self.points[after]

        dif = (index - point_before[0]) / (point_after[0] - point_before[0])

        return linear_interpolate(point_before[1], point_after[1], dif)

    def add_color_point(self, index, color):
        self.points += [[index, color]]

        self.points.sort(key=lambda x: x[0])


def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def linear_interpolate(col1, col2, dif):
    def interp(i): return int(col2[i] * dif + col1[i] * (1 - dif))

    return interp(0), interp(1), interp(2)
