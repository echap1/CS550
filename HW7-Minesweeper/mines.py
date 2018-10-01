import os, sys, inspect
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

import itertools
import random
import numpy as np

from termcolor import colored

from libs.commandLine import CommandLine, Argument


number_weights = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

number_colors = {1: colored("1", "blue"), 2: colored("2", "green"), 3: colored("3", "red"),
                 4: colored("4", "blue", attrs=["dark"]), 5: colored("5", "magenta"), 6: colored("6", "cyan"),
                 7: "7", 8: colored("8", "grey"), -1: colored("*", attrs=["bold", "reverse"]), 0: " "}


def get_grid_around(point, n, grid):
    return np.array([y[point[1] - n:point[1] + 1 + n] for y in grid[point[0] - n:point[0] + 1 + n]])


c = CommandLine(__file__)
c.add_argument("WIDTH", Argument(int, lambda x: x > 0), "Width of the grid")
c.add_argument("HEIGHT", Argument(int, lambda x: x > 0), "Height of the grid")
[w, h] = c.get_arg_values()

mines = (w * h) // 5 + 1
mine_grid = np.array([[0] * (w + 2) for _ in range(h + 2)])
num_grid = np.array([[0] * (w + 2) for _ in range(h + 2)])

for i, j in random.sample(list(itertools.product(np.arange(w) + 1, np.arange(h) + 1)), mines):
    mine_grid[j][i] = 1

for y in np.arange(w) + 1:
    for x in np.arange(h) + 1:
        around = get_grid_around([x, y], len(number_weights) // 2, mine_grid)
        num_grid[x][y] = np.sum(around * number_weights) if mine_grid[x][y] == 0 else -1

[print(*[number_colors[n] for n in y[1:-1]]) for y in num_grid[1:-1]]
