import numpy as np


class Histogram:
    data = []
    total = 0

    def __init__(self, max_depth):
        self.data = [0] * max_depth

    def __call__(self, index):
        if type(index) is np.float_:
            f = int(np.floor(index))
            diff = index - f

            return (1 - diff) * self(f) + diff * self(f + 1)

        if type(index) is list:
            return [self(i) for i in index]

        return sum(self.data[:index - 1]) / self.total

    def __copy__(self):
        h = Histogram(0)
        h.data = self.data.copy()
        h.total = self.total

        return h

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value
        self.total = sum(self.data)

    def __str__(self):
        return str(self.data)
