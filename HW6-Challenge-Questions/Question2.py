"""
CS550 Homework: Challenge Questions - 2
Due September 10, 2018

@author: Ethan Chapman

#Generate  a  list  of  100  numbers,  1  to  100,  without  using  a  traditional
#looping  technique  (investigate  list  comprehensions).  Shuffle  the  list  up
#so  the  numbers  are  not  in  order.  (Ms.  Healey)

"""

import random
import numpy as np

print(random.sample(list(np.arange(100) + 1), 100))