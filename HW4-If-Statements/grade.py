"""
CS550 Homework: If Statements
Due September 14, 2018

@author: Ethan Chapman
"""

import sys
sys.path.append("..")

from libs.basicCommandLine import *


def main():
    grade_names = ["F", "D", "D+", "C-",  "C",  "C+", "B-", "B",  "B+", "A-", "A", "A+"]
    grade_values = [0,  1.5, 2,    2.5,   2.85, 3.2,  3.5,  3.85, 4.2,  4.5,  4.7, 4.85]

    [grade_value] = BasicCommandLine.get_arg_values([Argument(float, lambda x: 0 <= x <= 5)])

    grade_index = len([x for x in grade_values if x <= grade_value]) - 1

    print(grade_names[grade_index])


main()
