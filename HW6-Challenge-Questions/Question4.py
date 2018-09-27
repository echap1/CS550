"""
CS550 Homework: Challenge Questions - 4
Due September 10, 2018

@author: Ethan Chapman

#Generate a random list of 6 multiples of 13 that are within 270 and
#do not have any number with the digit 6 (Eric, Tilden, Ethan)

"""

import random
import numpy as np

print(random.sample([n for n in 13 * (np.arange(270 // 13) + 1) if "6" not in str(n)], 6))