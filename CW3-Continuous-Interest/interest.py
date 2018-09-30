"""
CS550 Classwork: Continuous Interest
September 14, 2018

@author: Ethan Chapman
"""

import os, sys, inspect
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

from libs.commandLine import *

import numpy as np


def main():
    cl = CommandLine(__file__)

    cl.add_argument("P", Argument(float), "Principal (Starting Value)")
    cl.add_argument("R", Argument(float), "Interest Rate")
    cl.add_argument("T", Argument(float), "Time (y)")

    [p, r, t] = cl.get_arg_values()

    print(round(p * np.exp(r * t)))


main()
