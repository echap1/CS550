""" inspired by:
    http://anandology.com/python-practice-book/object_oriented_programming.html

    other resources:
    https://docs.python.org/3/reference/datamodel.html
    https://docs.python.org/3/library/operator.html
"""

import math


class RationalNumber:
    def __init__(self, n, d):
        g = math.gcd(n, d)

        self.n = int(n / g)
        self.d = int(d / g)

    def __add__(self, other):
        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return RationalNumber(n, d)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        return RationalNumber(self.n * other.n, self.d * other.d)

    def __neg__(self):
        return RationalNumber(-self.n, self.d)

    def __pow__(self, power, modulo=None):
        return RationalNumber(self.n ** power, self.d ** power)

    def __truediv__(self, other):
        return RationalNumber(self.n * other.d, self.d * other.n)

    def __str__(self):
        return f"{self.n}/{self.d}"

    # __repr__ = __str__  # what does this do?


def main():
    a = RationalNumber(1, 2)
    b = RationalNumber(1, 3)
    print(a)  # 1/2
    print(b)  # 1/3
    print(a + b)  # 5/6
    print(a - b)  # 1/6
    print(a * b)  # 1/6
    print(a / b)  # 3/2


main()
