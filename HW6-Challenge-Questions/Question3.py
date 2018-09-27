"""
CS550 Homework: Challenge Questions - 3
Due September 10, 2018

@author: Ethan Chapman

#Create a list of 100 randomly generated 3-digit numbers.
#Find a way to extract only the first digit from each number,
#and then arrange the resulting list in ascending order.

#Bonus: write a program to find the # of times a digit that
#occurs in the final list (there will be multiple of each) (Nico, Kai)

"""

import random

first_digits = sorted([int(str(n)[0]) for n in random.sample(range(100, 1000), 100)])
[print(str(i) + " occured " + str(first_digits.count(i)) + " times") for i in range(1, 10)]