"""
CS550 Classwork: Continuous Interest
September 14, 2018

@author: Ethan Chapman
"""

import numpy as np

import commandLine


def main():
    cl = commandLine.CommandLine(__file__)

    cl.add_argument("P", float, "Principal (Starting Value)")
    cl.add_argument("R", float, "Interest Rate")
    cl.add_argument("T", float, "Time (y)")

    [p, r, t] = cl.get_arg_values()

    print(round(p * np.exp(r * t)))


main()
