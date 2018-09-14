"""
CS550 Classwork: Commands
September 10, 2018

@author: Ethan Chapman

Sources:
    sys.argv: https://docs.python.org/3/library/sys.html

Bonus Questions:
    1: The Working Directory
    2: len(sys.argv) - 1
    3: More - Ignored, Fewer - Errors
"""

import sys


def main():
    arguments = sys.argv
    arguments.pop(0)

    greeting = "Hello, "

    for i in range(len(arguments)):
        greeting += arguments[i]
        if i == len(arguments) - 1:
            greeting += "."
        else:
            greeting += " and "

    print(greeting)


main()
