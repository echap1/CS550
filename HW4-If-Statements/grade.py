"""
CS550 Homework: Basic Operations - Question 1 (Wind Chill)
Due September 14, 2018

@author: Ethan Chapman
"""

import sys
sys.path.append("..")

from libs.basicCommandLine import *


def main():
    grade_names = ["F", "D", "D+", "C-",  "C",  "C+", "B-", "B",  "B+", "A-", "A", "A+", "A+"]
    grade_values = [0,  1.5, 2,    2.5,   2.85, 3.2,  3.5,  3.85, 4.2,  4.5,  4.7, 4.85, float("inf")]

    cl = CommandLine(__file__)
    cl.add_argument(float)
    [grade_value] = cl.get_arg_values()

    if not 0 <= grade_value <= 5:
        print("Value out of range!")
        return

    grade_index = 0

    while grade_values[grade_index + 1] <= grade_value:
        grade_index += 1

    print(grade_names[grade_index])


main()
