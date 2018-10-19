from PIL import Image

import matplotlib.pyplot as plt
import itertools
import numpy as np

from pallete import Histogram, linear_interpolate

color = Histogram()

color += (0, (0, 0, 80))
color += (128, (255, 255, 255))
color += (250, (100, 100, 255))
color += (255, (0, 0, 0))

image_size = (1000, 1000)
# color = lambda x: hsv2rgb(x / 256, 0.5, 0.5 if x < 255 else 0)
max_iterations = 255

# def zoom(current_bounds, point, factor=1.3):
#     [c_min_x, c_min_y, c_max_x, c_max_y] = [*current_bounds]
#     [p_x, p_y] = [*point]
#
#     c_min_x += (p_x - c_min_x) / factor
#     c_min_y += (p_y - c_min_y) / factor
#     c_max_x += (p_x - c_max_x) / factor
#     c_max_y += (p_y - c_max_y) / factor
#
#     return (c_min_x, c_min_y, c_max_x, c_max_y)

# zoom((-2, -2, 2, 2), (-0.75, 0))

def get_c(xy, image_size, c_bounds=(-2, -1.5, 1, 1.5)):
    [x, y, w, h, c_min_x, c_min_y, c_max_x, c_max_y] = [*xy, *image_size, *c_bounds]
    return complex((c_max_x - c_min_x) * x / (w - 1) + c_min_x, (c_max_y - c_min_y) * y / (h - 1) + c_min_y)

def escape_num(c, max_iterations, r=200):
    z = 0j
    iterations = 0

    for i in range(max_iterations):
        if abs(z) >= r:
            iterations = i
            break

        z = z ** 2 + c

    if iterations == 0: iterations = max_iterations

    if iterations < max_iterations:
        log_zn = np.log(z.real ** 2 + z.imag ** 2) / 2
        nu = np.log(log_zn / np.log(2)) / np.log(2)
        iterations = iterations + 1 - nu

    return iterations

def gen_image(image_size, color, max_iterations):
    image = Image.new("RGB", image_size)

    for pos in list(itertools.product(*[range(k) for k in image_size])):
        if pos[1] == 0:
            if pos[0] % 100 == 0:
                print(str(int(100 * (pos[0] / image_size[0]))) + "%")

        iterations = escape_num(get_c(pos, image_size), max_iterations)

        col1, col2 = color(np.floor(iterations)), color(np.ceil(iterations))

        col = linear_interpolate(col1, col2, iterations - np.floor(iterations))

        image.putpixel(pos, col)

    return image

image = gen_image(image_size, color, max_iterations)

image.save("mandelbrot.png", "PNG")

plt.imshow(image)
plt.show()