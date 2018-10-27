from pallete import PointInterpolation
from fractalCalc import Mandelbrot, BurningShip, Julia, Fractal


def set_colors(image_num):
    color = [PointInterpolation() for _ in range(image_num)]

    color[0] += (0,      (100, 0  , 7  ))
    color[0] += (0.16,   (152, 24 , 80 ))
    color[0] += (0.36,   (203, 32 , 107))
    color[0] += (0.42,   (255, 237, 255))
    color[0] += (0.6425, (0  , 255, 170))
    color[0] += (0.8575, (0  , 0  , 2  ))
    color[0] += (1,      (0  , 0  , 0  ))

    color[1] += (0,      (7  , 100, 0  ))
    color[1] += (0.16,   (80 , 152, 24 ))
    color[1] += (0.36,   (107, 203, 32 ))
    color[1] += (0.42,   (255, 255, 237))
    color[1] += (0.6425, (170, 0  , 255))
    color[1] += (0.8575, (2  , 0  , 0  ))
    color[1] += (1,      (0  , 0  , 0  ))

    color[2] += (0,      (0  , 7  , 100))
    color[2] += (0.16,   (24 , 80 , 152))
    color[2] += (0.36,   (32 , 107, 203))
    color[2] += (0.42,   (237, 255, 255))
    color[2] += (0.6425, (255, 170, 0  ))
    color[2] += (0.8575, (0  , 2  , 0  ))
    color[2] += (1,      (0  , 0  , 0  ))

    color[3] += (0,      (7  , 0  , 100))
    color[3] += (0.16,   (80 , 24 , 152))
    color[3] += (0.36,   (107, 32 , 203))
    color[3] += (0.42,   (255, 237, 255))
    color[3] += (0.6425, (170, 255, 0  ))
    color[3] += (0.8575, (2  , 0  , 0  ))
    color[3] += (1,      (0  , 0  , 0  ))

    return color


image_count = 4

colors = set_colors(image_count)

image_size = (512, 512)
max_iterations = 255

coordinates = [
    Fractal.zoom((-0.235125, 0.827215), 4.0e-5),
    Fractal.zoom((-0.7463, 0.1102), 0.005),
    Fractal.zoom((-1.15412664822215, 0.30877492767139), 3.7e-5),
    Fractal.zoom((-0.8115312340458353, 0.2014296112433656), 3.4e-5),
]

Fractal.plot(Mandelbrot(), image_size, max_iterations, colors, coordinates, lambda i: f"mandelbrot{i}")
Fractal.plot(BurningShip(), image_size, max_iterations, colors[2], Fractal.zoom((-1.762, -0.028), 0.01), lambda i: f"ship{i}")
