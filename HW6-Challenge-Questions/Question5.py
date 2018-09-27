"""
CS550 Homework: Challenge Questions - 4
Due September 10, 2018

@author: Ethan Chapman

#Generate a random list with its items being integer from 1 to 30,
#the list should be 30 items long. then print only those values
#whose digit sum equals 5. (Oleh, Justin, Jackson)

"""

import numpy as np

print([i for i in np.arange(30) + 1 if sum([int(j) for j in list(str(i))]) == 5])