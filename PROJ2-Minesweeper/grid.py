import numpy as np
import random
import itertools

from libs.color import *

class Grid:
    num_grid: np.array
    visible_grid: np.array

    n = 2
    add_array = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

    w: int
    h: int
    mines: int

    def __init__(self, w, h, mines):
        self.w, self.h, self.mines = w, h, mines

        self.num_grid = np.array([[0] * (w + 2 * self.n) for _ in range(h + 2 * self.n)])
        self.visible_grid = np.array([[0] * (w + 2 * self.n) for _ in range(h + 2 * self.n)])
        self.flagged_grid = np.array([[0] * (w + 2 * self.n) for _ in range(h + 2 * self.n)])

        for i, j in random.sample(list(itertools.product(np.arange(w) + self.n, np.arange(h) + self.n)), mines):
            self.num_grid[j][i] = -1
            self.num_grid = Grid.add_at(j - 1, i - 1, self.add_array, self.num_grid)

    def __str__(self):
        number_colors = {1: bold(blue("1")), 2: bold(green("2")), 3: bold(red("3")), 4: bold(dark(blue("4"))),
                         5: bold(magenta("5")), 6: bold(cyan("6")), 7: bold("7"), 8: bold(grey("8")),
                         -1: bold(reverse("*")), 0: " ", -2: reverse(red("F")), -3: "#"}

        flagged_nums = np.array([[0] * (self.w + 2 * self.n) for _ in range(self.h + 2 * self.n)])

        for i in range(len(self.num_grid)):
            for j in range(len(self.num_grid[0])):
                flagged_nums[i][j] = self.num_grid[i][j] if self.flagged_grid[i][j] == 0 else -2

        visible_nums = flagged_nums - (1 - self.visible_grid) * 11
        visible_nums = [[-2 if x == -13 else x for x in y] for y in visible_nums]

        ret = [[number_colors[x] if x >= -2 else number_colors[-3] for x in y[self.n:-self.n]] for y in visible_nums[self.n:-self.n]]

        n = len(ret[0])

        top = " " * len(str(len(ret))) + " " + " ".join([str(i // 10) if i % 10 == 0 and i > 0 else " " for i in range(n)])
        top += "\n " + " " * len(str(len(ret))) + underline(bold(" ".join([str(i % 10) for i in range(n)])))

        rows = [" ".join(r) for r in ret]
        rows = [" " * (len(str(len(ret))) - len(str(r))) + bold(str(r) + "|") + rows[r] for r in range(len(ret))]

        return top + "\n" + "\n".join(rows) + "\n"

    def get_num(self, x, y):
        return self.num_grid[self.n + y][self.n + x]

    def set_num(self, x, y, n):
        self.num_grid[self.n + y][self.n + x] = int(n)

    def get_visible(self, x, y):
        return bool(self.visible_grid[self.n + y][self.n + x])

    def set_visible(self, x, y, v: bool):
        self.visible_grid[self.n + y][self.n + x] = int(v)

        if self.get_num(x, y) == 0:
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if not(i == 0 and j == 0) and not(self.get_visible(x + i, y + j)):
                        if 0 <= x < self.w and 0 <= y < self.h:
                            self.set_visible(x + i, y + j, True)

    def check_win(self):
        a = []

        for i in range(self.w):
            for j in range(self.h):
                a += [self.get_visible(i, j) or (self.get_flagged(i, j) and self.get_num(i, j) == -1)]

        return all(a)

    def get_flagged(self, x, y):
        return bool(self.flagged_grid[self.n + y][self.n + x])

    def set_flagged(self, x, y, f: bool):
        self.flagged_grid[self.n + y][self.n + x] = int(f)

    @staticmethod
    def add_at(x, y, a, b):
        for i in range(len(a)):
            for j in range(len(a[0])):
                b[i + x][j + y] += a[i][j] if b[i + x][j + y] >= 0 else 0
        return b