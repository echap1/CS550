"""
CS550 Homework: Basic Operations - Question 3 (Day of Week)
Due September 14, 2018

@author: Ethan Chapman
"""

import os, sys, inspect
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

from libs.commandLine import *


def main():
    cl = CommandLine(__file__)

    cl.add_argument("MONTH", Argument(int, lambda x: 1 <= x <= 12), "A number representing the month (ex. 1 for January, 2 for Febuary)")
    cl.add_argument("DAY", Argument(int, lambda x: 1 <= x <= 31), "The day of the year")
    cl.add_argument("YEAR", Argument(int), "The year")

    [m, d, y] = cl.get_arg_values()

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + (31 * m0) // 12) % 7
    d0 = int(d0)

    print(days[d0])


main()