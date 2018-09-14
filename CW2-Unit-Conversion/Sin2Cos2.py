"""
CS550 Classwork: Unit Conversion
September 10, 2018

@author: Ethan Chapman
"""

import random
import numpy as np


def main():
    def sin2cos2(theta): return pow(np.sin(theta), 2) + pow(np.cos(theta), 2)

    trys = int(input("Amount to try: "))

    for i in range(trys):
        theta = random.random() * np.pi * 2
        print(str(theta) + ": " + str(sin2cos2(theta)))


main()
