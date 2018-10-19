from PIL import Image

import matplotlib.pyplot as plt
import itertools


size = (1000, 1000)
color = lambda x: (x, 5 * (x % 25), 12 * (x % 10))
max_iterations = 255

def zoom(current_bounds, point, factor=1.3):
    [c_min_x, c_min_y, c_max_x, c_max_y] = [*current_bounds]
    [p_x, p_y] = [*point]

    c_min_x += (p_x - c_min_x) / factor
    c_min_y += (p_y - c_min_y) / factor
    c_max_x += (p_x - c_max_x) / factor
    c_max_y += (p_y - c_max_y) / factor

    return (c_min_x, c_min_y, c_max_x, c_max_y)

# zoom((-2, -2, 2, 2), (-0.75, 0))

def get_c(xy, size, c_bounds=(-2, -2, 2, 2)):
    [x, y, w, h, c_min_x, c_min_y, c_max_x, c_max_y] = [*xy, *size, *c_bounds]
    return complex((c_max_x - c_min_x) * x / (w - 1) + c_min_x, (c_max_y - c_min_y) * y / (h - 1) + c_min_y)

def escape_num(c, max_iterations, r=2):
    z = 0j

    for i in range(max_iterations):
        if abs(z) >= r: return i

        z = z ** 2 + c

    return max_iterations

def gen_image(size, color, max_iterations):
    image = Image.new("RGB", size)

    for pos in list(itertools.product(*[range(k) for k in size])):
        if pos[1] == 0:
            if pos[0] % 100 == 0:
                print(str(int(100 * (pos[0] / size[0]))) + "%")

        c = get_c(pos, size)

        image.putpixel(pos, color(escape_num(c, max_iterations)))

    return image

image = gen_image(size, color, max_iterations)

image.save("mandelbrot.png", "PNG")

plt.imshow(image)
plt.show()