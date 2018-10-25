from PIL import Image
from decimal import Decimal
from functools import partial

import itertools
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing

from histogram import Histogram


class Fractal:
    h: Histogram
    pool: multiprocessing.Pool

    def __call__(self, image_size, color, max_iterations, c_bounds=(-2, -1.5, 1, 1.5)):
        self.h = Histogram(max_iterations + 1)  # Create empty histogram

        image = Image.new("RGB", image_size)  # Initialize image

        print("Calculating Iterations...")

        pool = multiprocessing.Pool()  # Create the Multiprocessing pool

        # Create a partial function for finding the iterations and run it
        temp = partial(self.helper1, image_size=image_size, max_iterations=max_iterations, c_bounds=c_bounds)
        iter_array = pool.starmap(temp, itertools.product(*[range(k) for k in image_size]))

        # Update the histogram and change the iter_array to correct values
        for i in range(len(iter_array)):
            self.h[iter_array[i][1]] += 1
            iter_array[i] = iter_array[i][0]

        print("Calculating Colors...")

        # Another partial function for the colors
        temp = partial(self.helper2, image_size=image_size, color=color, max_iterations=max_iterations,
                       iter_array=iter_array, h=self.h)
        color_array = pool.starmap(temp, itertools.product(*[range(k) for k in image_size]))

        # Write the image data
        for pos in list(itertools.product(*[range(k) for k in image_size])):
            image.putpixel(pos, color_array[pos[0] + pos[1] * image_size[1]])

        print("Done!\n")

        del iter_array, color_array, temp, pool

        return image

    # Helper function for finding the number of iterations of the fractal
    def helper1(self, *pos, image_size, max_iterations, c_bounds):
        return self.escape_num(Fractal.get_c(pos, image_size, c_bounds), max_iterations)

    # Helper function for finding the color
    @staticmethod
    def helper2(*pos, image_size, color, max_iterations, iter_array, h):
        iterations = iter_array[pos[0] + pos[1] * image_size[1]]

        return color(1) if iterations + 1 == max_iterations else color(h(iterations))

    # Number of escapes of a given c and escape radius (overriden by parent class)
    def escape_num(self, c, max_iterations, r=2e8):
        pass

    # Converts (x, y, c_bounds) into complex number c
    @staticmethod
    def get_c(xy, image_size, c_bounds):
        [x, y, w, h, c_min_x, c_min_y, c_max_x, c_max_y] = [Decimal(i) for i in [*xy, *image_size, *c_bounds]]
        return complex((c_max_x - c_min_x) * x / (w - 1) + c_min_x, (c_max_y - c_min_y) * y / (h - 1) + c_min_y)

    # Function to get c bounds zoomed in on a point
    @staticmethod
    def zoom(point, r=0.05):
        point, r = (Decimal(point[0]), Decimal(point[1])), Decimal(r)
        return point[0] - r, point[1] - r, point[0] + r, point[1] + r

    # Plot and save fractals
    @staticmethod
    def plot(f, image_size, max_iterations, colors, coordinates=(-2.0, -1.5, 1.0, 1.5),
             image_names=lambda x: f"mandelbrot{x}"):
        if type(colors) is not list:
            colors = [colors]

        if type(coordinates) is not list:
            coordinates = [coordinates]

        image_count = np.min((len(coordinates), len(colors)))
        images = []

        for i in range(image_count):
            print(f"Image {i}:")
            images += [f(image_size, colors[i], max_iterations, coordinates[i])]
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

        return Mandelbrot.smooth(z, iterations, max_iterations), iterations

    # Function to smooth iterations into a continuous decimal
    @staticmethod
    def smooth(z, iterations, max_iterations):
        if iterations + 1 == max_iterations:
            return iterations

        return iterations - np.log(np.log(abs(z))) / np.log(2)


class BurningShip(Fractal):
    def __init__(self):
        pass

    def escape_num(self, c, max_iterations, r=2e8):
        z = 0j
        iterations = 0

        for iterations in range(max_iterations):
            if abs(z) >= r:
                break

            z = complex(abs(z.real), abs(z.imag)) ** 2 + c

        return iterations, iterations


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

        return iterations, iterations