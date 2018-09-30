"""
CS550 Homework: Basic Operations - Question 2 (XYZ)
Due September 14, 2018

@author: Ethan Chapman
"""

import os, sys, inspect
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

from libs.commandLine import *


def main():
    cl = CommandLine(__file__)

    cl.add_argument("X", Argument(float), "First Number")
    cl.add_argument("Y", Argument(float), "Second Number")
    cl.add_argument("Z", Argument(float), "Third Number")

    [x, y, z] = cl.get_arg_values()

    print(x < y < z or x > y > z)


main()
