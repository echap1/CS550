import random
import numpy as np
import matplotlib.pyplot as plt

n = 100

nums = [0] * (n + 1)

for i in range(100000):
    num = 0
    for j in range(n):
        if random.randint(0, 1) == 0: num += 1

    nums[num] += 1

s_nums = sum(nums)

plt.bar(np.arange(n + 1), nums)
plt.xticks(range(n + 1))
plt.xlabel('# of Heads')
plt.ylabel('Occurrences')
plt.grid(True, axis='y')

plt.show()