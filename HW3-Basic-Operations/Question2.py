"""
CS550 Homework: Basic Operations - Question 2 (XYZ)
Due September 14, 2018

@author: Ethan Chapman
"""

import commandLine


def main():
    cl = commandLine.CommandLine(__file__)

    cl.add_argument("X", float, "First Number")
    cl.add_argument("Y", float, "Second Number")
    cl.add_argument("Z", float, "Third Number")

    [x, y, z] = cl.get_arg_values()

    print(x < y < z or x > y > z)


main()
