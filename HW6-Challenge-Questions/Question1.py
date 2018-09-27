"""
CS550 Homework: Challenge Questions - 1
Due September 10, 2018

@author: Ethan Chapman

#Generate  a  list  of  10  random  numbers  between  0  and  100.
#Get  them  in order  from  largest  to  smallest,
#removing  numbers  divisible  by  3.  (Ms. Healey)

"""

import random

print(sorted([n for n in random.sample(range(101), 10) if n % 3 != 0], key=lambda a: -a))