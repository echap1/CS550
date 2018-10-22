from PIL import Image
from decimal import Decimal

import itertools
import numpy as np
import matplotlib.pyplot as plt

from histogram import Histogram

class Fractal:
    h: Histogram

    def __call__(self, image_size, color, max_iterations, c_bounds=(-2, -1.5, 1, 1.5), histogram=True):
        self.h = Histogram(max_iterations + 1)

        iter_array = [[0] * image_size[1] for _ in range(image_size[0])]

        image = Image.new("RGB", image_size)

        print("Calculating Iterations...")

        for pos in list(itertools.product(*[range(k) for k in image_size])):
            if pos[1] == 0:
                if pos[0] % 100 == 0:
                    print(str(int(100 * (pos[0] / image_size[0]))) + "%")

            iterations = self.escape_num(Fractal.get_c(pos, image_size, c_bounds), max_iterations)

            if histogram:
                iter_array[pos[0]][pos[1]] = iterations

            else:
                image.putpixel(pos, color(iterations / max_iterations))

        print("100%\n\nCalculating Colors...")

        if histogram:
            for pos in list(itertools.product(*[range(k) for k in image_size])):
                iterations = iter_array[pos[0]][pos[1]]

                image.putpixel(pos, color(1) if iterations + 1 == max_iterations else color(self.h(iterations)))

        print("Done!\n")

        return image

    def escape_num(self, c, max_iterations, r=2e8):
        pass

    @staticmethod
    def get_c(xy, image_size, c_bounds):
        [x, y, w, h, c_min_x, c_min_y, c_max_x, c_max_y] = [Decimal(i) for i in [*xy, *image_size, *c_bounds]]
        return complex((c_max_x - c_min_x) * x / (w - 1) + c_min_x, (c_max_y - c_min_y) * y / (h - 1) + c_min_y)

    @staticmethod
    def zoom(point, r=0.05):
        point, r = (Decimal(point[0]), Decimal(point[1])), Decimal(r)
        return point[0] - r, point[1] - r, point[0] + r, point[1] + r

    @staticmethod
    def smooth(z, iterations, max_iterations, r):
        pass

    @staticmethod
    def plot(f, image_size, max_iterations, colors, coordinates=(-2.0, -1.5, 1.0, 1.5),
             image_names=lambda x: f"mandelbrot{x}", histogram=True):
        if type(colors) is not list:
            colors = [colors]

        if type(coordinates) is not list:
            coordinates = [coordinates]

        image_count = np.min((len(coordinates), len(colors)))
        images = []

        for i in range(image_count):
            print(f"Image {i}:")
            images += [f(image_size, colors[i], max_iterations, coordinates[i], histogram)]
            images[i].save(f"{image_names(i)}.png", "PNG")

        if image_count == 1:
            plt.imshow(images[0])
            plt.show()

        else:
            row_size = int(np.ceil(np.sqrt(image_count)))

            f, axes = plt.subplots(row_size, row_size)

            for (i, j), n in zip(itertools.product(range(row_size), range(row_size)), range(image_count)):
                axes[i, j].imshow(images[n])

            plt.show()


class Mandelbrot(Fractal):
    def __init__(self):
        pass

    def escape_num(self, c, max_iterations, r=2e8):
        z = 0j
        iterations = 0

        for iterations in range(max_iterations):
            if abs(z) >= r:
                break

            z = z ** 2 + c

        self.h[iterations] += 1

        return Mandelbrot.smooth(z, iterations, max_iterations, r)

    @staticmethod
    def smooth(z, iterations, max_iterations, r):
        if iterations + 1 == max_iterations:
            return iterations

        return iterations - np.log(np.log(abs(z))) / np.log(2)


class Julia(Fractal):
    equ: callable(complex)

    def __init__(self, equ=lambda z: z ** 2 - 1):
        self.equ = equ

    def escape_num(self, z, max_iterations, r=2e8):
        iterations = 0

        for iterations in range(max_iterations):
            if abs(z) >= r:
                break

            z = self.equ(z)

        self.h[iterations] += 1

        return Mandelbrot.smooth(z, iterations, max_iterations, r)

    @staticmethod
    def smooth(z, iterations, max_iterations, r):
        return iterations