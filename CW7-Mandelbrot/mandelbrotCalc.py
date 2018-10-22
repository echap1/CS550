from PIL import Image
from decimal import Decimal

import itertools
import numpy as np
import matplotlib.pyplot as plt

from histogram import Histogram

class Mandelbrot:
    h: Histogram

    def __init__(self):
        pass

    def __call__(self, image_size, color, max_iterations, c_bounds=(-2, -1.5, 1, 1.5), histogram=True, buildHist=True):
        if buildHist:
            self.h = Histogram(max_iterations + 1)

        iter_array = [[0] * image_size[1] for _ in range(image_size[0])]

        image = Image.new("RGB", image_size)

        print("Calculating Iterations...")

        for pos in list(itertools.product(*[range(k) for k in image_size])):
            if pos[1] == 0:
                if pos[0] % 100 == 0:
                    print(str(int(100 * (pos[0] / image_size[0]))) + "%")

            iterations = self.escape_num(Mandelbrot.get_c(pos, image_size, c_bounds), max_iterations, buildHist=buildHist)

            if histogram:
                iter_array[pos[0]][pos[1]] = iterations

            else:
                image.putpixel(pos, color(iterations / max_iterations))

        print("100%\n\nCalculating Colors...")

        if histogram:
            for pos in list(itertools.product(*[range(k) for k in image_size])):
                iterations = iter_array[pos[0]][pos[1]]

                if iterations + 1 == max_iterations:
                    image.putpixel(pos, color(1))

                else:
                    h0 = self.h(iterations)

                    # col = linear_interpolate(color(h0), color(h1), iterations - f)

                    col = color(h0)

                    image.putpixel(pos, col)

        print("Done!\n")

        return image

    def escape_num(self, c, max_iterations, r=2e8, buildHist=True):
        z = 0j
        iterations = 0

        for iterations in range(max_iterations):
            if abs(z) >= r:
                break

            z = z ** 2 + c

        if buildHist:
            self.h[iterations] += 1

        return Mandelbrot.smooth(z, iterations, max_iterations, r)

    @staticmethod
    def get_c(xy, image_size, c_bounds):
        [x, y, w, h, c_min_x, c_min_y, c_max_x, c_max_y] = [Decimal(i) for i in [*xy, *image_size, *c_bounds]]
        return complex((c_max_x - c_min_x) * x / (w - 1) + c_min_x, (c_max_y - c_min_y) * y / (h - 1) + c_min_y)

    @staticmethod
    def zoom(point, r=0.05):
        point, r = (Decimal(point[0]), Decimal(point[1])), Decimal(r)
        return (point[0] - r, point[1] - r, point[0] + r, point[1] + r)

    @staticmethod
    def smooth(z, iterations, max_iterations, r):
        if iterations + 1 == max_iterations:
            return iterations

        return iterations - np.log(np.log(abs(z))) / np.log(2)

    @staticmethod
    def plot(image_size, max_iterations, colors, coordinates=(-2.0, -1.5, 1.0, 1.5), histogram=True, buildHist=True):
        if type(colors) is not list:
            colors = [colors]

        if type(coordinates) is not list:
            coordinates = [coordinates]

        m = Mandelbrot()

        image_count = np.min((len(coordinates), len(colors)))
        images = []

        for i, c in enumerate(coordinates):
            print(f"Image {i}:")
            images += [m(image_size, colors[i], max_iterations, c, histogram, buildHist)]
            images[i].save(f"mandelbrot{i}.png", "PNG")

        row_size = int(np.ceil(np.sqrt(image_count)))

        f, axes = plt.subplots(row_size, row_size)

        for (i, j), n in zip(itertools.product(range(row_size), range(row_size)), range(image_count)):
            axes[i, j].imshow(images[n])

        plt.show()


class Optimizations:

    @staticmethod
    def cardioid_period_2(x, y):
        q = (x - 0.25) ** 2 + y ** 2

        cardioid = q * (q + (x - 0.25)) < 0.25 * (y ** 2)
        period_2 = (x + 1) ** 2 + y ** 2 < 0.0625

        return cardioid or period_2
