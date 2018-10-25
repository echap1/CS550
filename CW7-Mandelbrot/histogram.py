import numpy as np


# Histogram is to equally distribute iterations over color pallete
class Histogram:
    data = []
    total = 0

    def __init__(self, max_depth):
        self.data = [0] * max_depth

    # Call histogram for certain iteration value to get distributed decimal
    def __call__(self, index):
        if type(index) is np.float_:
            f = int(np.floor(index))
            diff = index - f

            return (1 - diff) * self(f) + diff * self(f + 1)

        if type(index) is list:
            return [self(i) for i in index]

        return sum(self.data[:index - 1]) / self.total

    # Getting value in list
    def __getitem__(self, item):
        return self.data[item]

    # Setting value in list
    def __setitem__(self, key, value):
        self.data[key] = value
        self.total = sum(self.data)

    # For debugging
    def __str__(self):
        return str(self.data)
