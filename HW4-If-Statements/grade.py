"""
CS550 Homework: If Statements
Due September 14, 2018

@author: Ethan Chapman
"""

import sys

grades = [["F", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"], [0, 1.5, 2, 2.5, 2.85, 3.2, 3.5, 3.85, 4.2, 4.5, 4.7, 4.85]]
print("Out of Range!" if not 0 <= float(sys.argv[1]) <= 5 else grades[0][len([x for x in grades[1] if x <= float(sys.argv[1])])-1])
